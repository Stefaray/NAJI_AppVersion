from flask import Flask
from flask import request
#解决跨域问题
from flask_cors import CORS
#引用加密库
from hashlib import sha1
#能够使用数据库语言
import pymysql
#对象和字符串转换
import json
#阿里云短信生成验证码
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
#生成四位随机验证码
import random
#生成当前日期
from datetime import datetime
# 生成时间戳
import time

from PIL import Image
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
# import time
import os
# from strUtil import Pic_str
import base64


app=Flask(__name__)
# 传入服务器
cors=CORS(app)

user_id = ""

#连接本地数据库
connectDB=pymysql.Connect(
    host='localhost',
    user='root',
    port=3306,
    password='ray34allen',
    database='uniapp',
    autocommit = True,        #新增
)


@app.route("/")
def index():
    return "(a:1,b:2)"
#


@app.route("/getUID")
def getUID():
    global user_id
    user_id = request.args.get("user_id")
    returnmsg={"status":0,"desc":"UID接收成功","user_id":user_id}
    return returnmsg
# 登录页面开始
@app.route("/user/login")
def login():
    account=request.args.get("account")
    password=request.args.get("password")
    #加密密码
    # password=sha1(password.encode()).hexdigest()
    #进行数据库查询
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select `user`.`user_id` AS `user_id`,`user`.`username` AS `username`,`user`.`phone` AS `phone`,`user`.`avatar` AS `avatar`,`user`.`create_date` AS `create_date`,`user`.`last_login_date` AS `last_login_date`,`user`.`password` AS `password` from `user` where (`user`.`password` = '"+str(password)+"')")
    result=cursor.fetchall()
    #结果放在result中
    returnmsg={"status":0,"desc":"登陆成功","user_id":1}
    
    if(len(result)==0):
        returnmsg["status"]=1
        returnmsg["desc"]="用户名和密码不匹配"
        returnmsg["user_id"]=0
    else:
        returnmsg["user_id"]=result[0]["user_id"]
        returnmsg["info"]=result[0]
    
    return returnmsg
# 登录页面结束
#用验证码注册页面开始————————点击验证码按钮
@app.route("/user/register_cha")
def getsms():
#点击验证码部分
    returnmsg={}
    client=AcsClient('LTAI4GDi1naCAPKMPbsrnmnS','CwM5eMsusKmISdzyRjKkrJBGxN5yyv','cn-hangzhou')
    phone_number=request.args.get("phone_number")
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    #查询手机号是否已经注册过账户了
    cursor.execute("select * from user where phone = '"+str(phone_number)+"'")
    result=cursor.fetchall()
    if (len(result)!=0):
        returnmsg={"status":1,"desc":"该手机号码已注册","sms_id":-1}
    else:
    #查询手机号是否已经注册过验证码了
        cursor.execute("select `sms`.`sms_id` AS `sms_id`,`sms`.`phone` AS `phone`,`sms`.`code` AS `code` from `sms` where (`sms`.`phone` = '"+str(phone_number)+"')")
        result=cursor.fetchall()
        if (len(result)==0):
            isnew=1
        else:
            isnew=2

        # password=request.args.get("password")
        # captcha=request.args.get("captcha")
        cha_num=str(random.randint(1000,9999))
        #进行短信验证开始
        req1 = CommonRequest()
        req1.set_accept_format('json')
        req1.set_domain('dysmsapi.aliyuncs.com')
        req1.set_method('POST')
        req1.set_protocol_type('https') # https | http
        req1.set_version('2017-05-25')
        req1.set_action_name('SendSms')
        req1.add_query_param('RegionId', "cn-hangzhou")
        req1.add_query_param('PhoneNumbers', phone_number)
        req1.add_query_param('SignName', "NAJI纳己")
        req1.add_query_param('TemplateCode', "SMS_190727303")
        req1.add_query_param('TemplateParam', "{\"code\":\""+cha_num+"\"}")
        # res1 = client.do_action(req1)
        # # python2:  print(response) 
        # print(res1)
        #进行短信验证结束
        returnmsg={"status":0,"desc":"验证码可以发送"}
        if(phone_number == ""):
            if(cha_num == ""):
                returnmsg={"status":404,"desc":"不好意思，管理员的短信服务到期了~~~"}
            else:
                returnmsg={"status":1,"desc":"手机号码不能为空~"}
            return returnmsg
        #进行验证码的数据库插入
        else:
            if (isnew==1):
                cursor.execute('INSERT INTO sms (phone,code) VALUES ("'+str(phone_number)+'","'+cha_num+'")')
            else:
                cursor.execute('UPDATE sms SET code = "'+cha_num+'"WHERE phone = "'+str(phone_number)+'"')
    
    return returnmsg

#用验证码注册页面结束————————点击验证码按钮

#用验证码登录页面开始————————点击验证码按钮
@app.route("/user/login_sms")
def getsmsLogin():
#点击验证码部分
    returnmsg={}
    client=AcsClient('LTAI4GDi1naCAPKMPbsrnmnS','CwM5eMsusKmISdzyRjKkrJBGxN5yyv','cn-hangzhou')
    phone_number=request.args.get("phone_number")
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    #查询手机号是否已经注册过账户了
    cursor.execute("select * from user where phone = '"+str(phone_number)+"'")
    result=cursor.fetchall()
    if (len(result)==0):
        returnmsg={"status":1,"desc":"该手机号码未被注册过","sms_id":-1}
    else:
    #查询手机号是否已经注册过验证码了
        cursor.execute("select `sms`.`sms_id` AS `sms_id`,`sms`.`phone` AS `phone`,`sms`.`code` AS `code` from `sms` where (`sms`.`phone` = '"+str(phone_number)+"')")
        result=cursor.fetchall()
        if (len(result)==0):
            isnew=1
        else:
            isnew=2

        # password=request.args.get("password")
        # captcha=request.args.get("captcha")
        cha_num=str(random.randint(1000,9999))
        #进行短信验证开始
        req1 = CommonRequest()
        req1.set_accept_format('json')
        req1.set_domain('dysmsapi.aliyuncs.com')
        req1.set_method('POST')
        req1.set_protocol_type('https') # https | http
        req1.set_version('2017-05-25')
        req1.set_action_name('SendSms')
        req1.add_query_param('RegionId', "cn-hangzhou")
        req1.add_query_param('PhoneNumbers', phone_number)
        req1.add_query_param('SignName', "NAJI纳己")
        req1.add_query_param('TemplateCode', "SMS_190727303")
        req1.add_query_param('TemplateParam', "{\"code\":\""+cha_num+"\"}")
        # res1 = client.do_action(req1)
        # # python2:  print(response) 
        # print(res1)
        #进行短信验证结束
        returnmsg={"status":0,"desc":"验证码可以发送"}
        if(phone_number == ""):
            if(cha_num == ""):
                returnmsg={"status":404,"desc":"不好意思，管理员的短信服务到期了~~~"}
            else:
                returnmsg={"status":1,"desc":"手机号码不能为空~"}
            return returnmsg
        #进行验证码的数据库插入
        else:
            if (isnew==1):
                cursor.execute('INSERT INTO sms (phone,code) VALUES ("'+str(phone_number)+'","'+cha_num+'")')
            else:
                cursor.execute('UPDATE sms SET code = "'+cha_num+'"WHERE phone = "'+str(phone_number)+'"')
    
    return returnmsg
#用验证码登录页面结束————————点击验证码按钮

#用验证码注册页面开始————————点击注册按钮
# 点击注册部分
@app.route("/user/phone_register")
def phone_register():

    phone_number=request.args.get("phone_number")
    password=request.args.get("password")
    captcha=str(request.args.get("captcha"))

    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute("select * from sms where code = '"+captcha+"' and phone = '"+str(phone_number)+"'")
    result=cursor.fetchall()

    returnmsg_rg={"status":0,"desc":"注册成功","user_id":-1}
    
    if(len(result)==0):
        returnmsg_rg["status"]=1
        returnmsg_rg["desc"]="验证码输入错误"
    elif(len(password)<6):
        returnmsg_rg["status"]=1
        returnmsg_rg["desc"]="密码长度不能小于6位数"
    else:
        today = str(datetime.now()).split( )[0]
        cursor.execute('INSERT INTO user (username,phone,create_date,last_login_date,password) VALUES ("'+str(phone_number)+'","'+str(phone_number)+'","'+today+'","'+today+'","'+password+'")')
        cursor.execute("select user_id from user where phone = '"+str(phone_number)+"'")
        result2=cursor.fetchall()
        returnmsg_rg["user_id"]=result2[0]["user_id"]

    return returnmsg_rg
#用验证码注册页面结束————————点击注册按钮

#用验证码登录页面开始————————点击登录按钮
@app.route("/user/phone_login")
def phone_login():

    phone_number=request.args.get("phone_number")
    captcha=str(request.args.get("captcha"))

    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute("select * from sms where code = '"+captcha+"' and phone = '"+str(phone_number)+"'")
    result=cursor.fetchall()

    returnmsg={"status":0,"desc":"登陆成功","user_id":-1}
    
    if(len(result)==0):
        returnmsg["status"]=1
        returnmsg["desc"]="用户名和验证码不匹配"
        returnmsg["user_id"]=0
    else:
        returnmsg["user_id"]=result[0]["user_id"]
        returnmsg["info"]=result[0]
    

    return returnmsg_rg
#用验证码登录页面结束————————点击登录按钮

# -----------------  暂时省略开始    -------------------------
@app.route("/user/register_pw")
def register_pw():
    phone_number=request.args.get("phone_number")
    password=request.args.get("password")
    
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)

    cursor.execute("select * from user where phone = '"+str(phone_number)+"'")
    result=cursor.fetchall()
    if (len(result)!=0):
        returnmsg_rg={"status":1,"desc":"该手机号码已注册","user_id":-1}
    else:


        today = str(datetime.now()).split( )[0]
        returnmsg_rg={"status":0,"desc":"注册成功","user_id":-1}
        cursor.execute('INSERT INTO user (username,phone,create_date,last_login_date,password) VALUES ("'+str(phone_number)+'","'+str(phone_number)+'","'+today+'","'+today+'","'+str(password)+'")')

        cursor.execute("select user_id from user where phone = '"+str(phone_number)+"'")
        result2=cursor.fetchall()
        returnmsg_rg["user_id"]=result2[0]["user_id"]

    return returnmsg_rg
# -----------------  暂时省略结束    -------------------------


# 情绪爆炸页记录
@app.route("/moodBoom")
def moodBoomRecord():
# 生成时间戳
    user_id = request.args.get("user_id")
    user_id = str(user_id)
    tmp = str(int(time.time()))
    moodboom_id = tmp + str(random.randint(10000,99999))

    returnmsg_rg={"status":0,"desc":"记录成功","new":{} }
    timeString=request.args.get("timeString")   
    whichExpression=request.args.get("whichExpression")
    tagidText=request.args.get("tagidText")   
    moodNote=request.args.get("moodNote")   
    print(str(moodNote))
    if( str(whichExpression) == '0' and str(moodNote)== '' ):
        returnmsg_rg["status"]=-1
        returnmsg_rg["desc"]="记录失败"
    else:
        cursor=connectDB.cursor(pymysql.cursors.DictCursor)
        cursor.execute('INSERT INTO moodBoom (timeString,whichExpression,tagidText,moodNote,moodboom_id,user_id) VALUES ("'+str(timeString)+'","'+str(whichExpression)+'","'+str(tagidText)+'","'+str(moodNote)+'",'+moodboom_id+',"'+user_id+'")')

        cursor.execute('SELECT * FROM moodBoom WHERE moodboom_id =' + str(moodboom_id) )
        result=cursor.fetchall()
        returnmsg_rg["new"] = result

    return returnmsg_rg


# 每日小结页记录
@app.route("/dayRemind")
def dayRemindRecord():
# 生成时间戳
    user_id = request.args.get("user_id")
    user_id = str(user_id)
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)



    returnmsg_rg={"status":0,"desc":"记录成功","new":"","old":"" }


    dayString=request.args.get("dayString")   
    targetOption=request.args.get("targetOption")
    notedata1=request.args.get("notedata1")   
    notedata2=request.args.get("notedata2")
    notedata3=request.args.get("notedata3")
    dayNote=request.args.get("dayNote")   
    notedata = str(notedata1)+str(notedata2)+str(notedata3)
    # print(str(moodNote))

# 判断是更新还是新生成
    cursor.execute('SELECT * FROM dayremind WHERE dayString = "'+str(dayString)+'"')
    result=cursor.fetchall()

    judge_day = len(result)
    # print(len(result))

    tmp = str(int(time.time()))
    dayRemind_id = tmp + str(random.randint(10000,99999)) 
    s = str(targetOption).split(' ')
    print(s)
    print(str(dayNote))
    print(notedata)


    print(targetOption+'----targetOption')
    if( str(targetOption) == '0 0 0 0 0' and str(dayNote)== '' and notedata ==''):
        returnmsg_rg["status"]=-2   
        returnmsg_rg["desc"]="记录失败"
    elif( str(targetOption) == '0 0 0 0 0' and str(dayNote)== '' and notedata !=''):
        returnmsg_rg["status"]=-1
        returnmsg_rg["desc"]="记录成功"
        if(judge_day == 0):
            cursor.execute('INSERT INTO dayremind (dayRemind_id,dayString,targetOption,notedata1,notedata2,notedata3,dayNote,user_id) VALUES ("'+str(dayRemind_id)+'","'+str(dayString)+'","'+str(targetOption)+'","'+str(notedata1)+'","'+str(notedata2)+'","'+str(notedata3)+'","'+str(dayNote)+'","'+str(user_id)+'")')
        else:
            cursor.execute("UPDATE dayremind Set targetOption="+str(targetOption)+",notedata1="+str(notedata1)+",notedata2="+str(notedata2)+",notedata3="+str(notedata3)+",dayNote="+str(dayNote)+" WHERE dayString = "+str(dayString)+" ")
    else:
        returnmsg_rg["status"]=0
        returnmsg_rg["desc"]="记录成功"
        if(judge_day == 0):
            cursor.execute('INSERT INTO dayremind (dayRemind_id,dayString,targetOption,notedata1,notedata2,notedata3,dayNote,user_id) VALUES ("'+str(dayRemind_id)+'","'+str(dayString)+'","'+str(targetOption)+'","'+str(notedata1)+'","'+str(notedata2)+'","'+str(notedata3)+'","'+str(dayNote)+'","'+str(user_id)+'")')
        else:
            cursor.execute("UPDATE dayremind Set targetOption='"+str(targetOption)+"',notedata1='"+str(notedata1)+"',notedata2='"+str(notedata2)+"',notedata3='"+str(notedata3)+"',dayNote='"+str(dayNote)+"' WHERE dayString = '"+str(dayString)+" '")


    if(judge_day == 0):
        cursor.execute('SELECT * FROM dayremind WHERE dayRemind_id ="' + str(dayRemind_id) + '"')
        result=cursor.fetchall()
        returnmsg_rg["new"] = result
    else:
        cursor.execute('SELECT * FROM dayremind WHERE dayString ="' + str(dayString) + '"' )
        result=cursor.fetchall()
        returnmsg_rg["old"] = result
    day = str(datetime.now()).split(' ')[0]
    time0 = str(datetime.now()).split(' ')[1][0:5]

    if(notedata1 != ''):
        cursor.execute('INSERT INTO happything (day,time,user_id,content) VALUES ("'+str(day)+'","'+str(time0)+'","'+user_id+'","'+str(notedata1)+'")')
    if(notedata2 != ''):
        cursor.execute('INSERT INTO happything (day,time,user_id,content) VALUES ("'+str(day)+'","'+str(time0)+'","'+user_id+'","'+str(notedata2)+'")')
    if(notedata3 != ''):
        cursor.execute('INSERT INTO happything (day,time,user_id,content) VALUES ("'+str(day)+'","'+str(time0)+'","'+user_id+'","'+str(notedata3)+'")')



    return returnmsg_rg





# 记录页 情绪爆炸
@app.route("/record_moodBoom")
def record_moodBoom():

    returnmsg_rg={"status":0,"desc":"记录成功","moodBoomList":[]}

    user_id=request.args.get("user_id")   
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM moodboom WHERE user_id = "36" '  +' ORDER BY timeString desc')
    result=cursor.fetchall()
    returnmsg_rg["moodBoomList"]=result
    return returnmsg_rg


    
# 记录页 每日小结   
@app.route("/record_dayRemind")
def record_dayRemind():

    returnmsg_rg={"status":0,"desc":"记录成功","recordRemindList":[]}

    user_id=request.args.get("user_id")   
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM dayremind WHERE user_id = "36" ' +' ORDER BY dayString desc')
    result=cursor.fetchall()
    returnmsg_rg["recordRemindList"]=result
    return returnmsg_rg


# # ==================================================================================================================
# 揭照片变量
# app = Flask(__name__)
UPLOAD_FOLDER = 'static/photo'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG'])


# 上传文件
@app.route('/up_photo' , methods=['post'])
def api_upload():
    user_id = request.form.get("user_id")
    user_id = str(user_id)
    # print(user_id + "----") 
    if user_id not in app.config['UPLOAD_FOLDER']:
        app.config['UPLOAD_FOLDER'] += ("/"+user_id)
    # print(app.config['UPLOAD_FOLDER'])
# 存图片的路径（不包括图片）
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['file']
    # print(f)
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        print (fname)
        ext = fname.rsplit('.', 1)[1]
        new_filename = create_uuid() + '.' + ext
        f.save(os.path.join(file_dir, new_filename))
# 图片绝对路径
        file_path = os.path.join(file_dir, new_filename) # 把目标图片 input image 放到代码所处的文件夹里
        # file_path = "1.png"  
        image = Image.open(file_path)
        image = fill_image(image)

        image_list = cut_image(image)

        save_images(image_list,file_dir)
# 创建日期
        create_date = str(datetime.now()).split(' ')[0]
# 上次点亮日期
        last_light_date = ""
        cursor=connectDB.cursor(pymysql.cursors.DictCursor)
        cursor.execute('INSERT INTO photo (photo_id,user_id,create_date,last_light_date) VALUES ("'+str(new_filename)+'","'+str(user_id)+'","'+str(create_date)+'","'+str(last_light_date)+'")')
        # cursor.execute('INSERT INTO photo (piece1,piece2,piece3,piece4,piece5,piece6,piece7,piece8,piece9,finish) VALUES ("'+str(0)+'","'+str(0)+'","'+str(0)+'","'+str(0)+'","'+str(0)+'","'+str(0)+'","'+str(0)+'","'+str(0)+'","'+str(0)+'","'+str(0)+'")')
        cursor.execute('Select * From photo Where photo_id = "'+ new_filename +'"')
        result=cursor.fetchall()

        return jsonify({"success": 0, "msg": "上传成功", "photo_message":result[0]})
    else:
        return jsonify({"err": 1001, "msg": "上传失败"})

@app.route("/lightPiece")
def lightPiece():
    lightPiece = request.args.get("piece")
    photo_id = request.args.get("photo_id")

    last_light_date = str(datetime.now()).split(' ')[0]

    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    # cursor.execute('Update photo Set piece'+lightPiece+'=1 Where photo_id = "'+photo_id+'"')
    cursor.execute('Update photo Set piece'+lightPiece+'=1, last_light_date="'+last_light_date+'" Where photo_id = "'+photo_id+'"')

    cursor.execute('Select * From photo Where photo_id = "'+ photo_id +'"')
    
    result=cursor.fetchall()
   
    tmp2 =  result[0]
    returnmsg = {"success": 0, "msg": "点亮成功", "last_light_date":tmp2["last_light_date"]}
    isfinish = 1
    
    print("-------------------------------------------------------")
    # print(tmp2["piece1"]+tmp2["piece1"])
    for i in range(1,10):
        name = "piece" + str(i)
        if(tmp2[name] != 1):
            isfinish = 0
            break;
    if(isfinish == 1):
        cursor.execute('Update photo Set finish = 1 Where photo_id = "'+photo_id+'"')

    print("-------------------------------------------------------")


    return returnmsg

@app.route("/photoInitial")
def photoInitial():
    user_id = request.args.get("user_id")
    user_id = str(user_id)
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from photo where user_id = '"+user_id+"' and finish = 0") 
    returnmsg = {"success": 0, "msg": "图片初始化失败", "result":""}
    result=cursor.fetchall()
    if(len(result) != 0):
        returnmsg["result"] = result
        returnmsg["success"] = 1
        returnmsg["msg"] = "图片初始化成功"
    return returnmsg

@app.route("/photoCard")
def photoCard():
    user_id = request.args.get("user_id")
    user_id = str(user_id)
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from photo where user_id = '"+user_id+"' and finish = 1") 
    returnmsg = {"success": 0, "msg": "图片初始化失败", "result":""}
    result=cursor.fetchall()
    if(len(result) != 0):
        returnmsg["result"] = result
        returnmsg["success"] = 1
        returnmsg["msg"] = "图片初始化成功"
    return returnmsg

@app.route("/moodBottle")
def moodBottle():
    user_id = request.args.get("user_id")
    user_id = str(user_id)
    category = request.args.get("category")
    moodBottleText = request.args.get("moodBottleText")
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute("INSERT INTO moodBottle (category,moodBottleText,user_id) VALUES (\""+str(category)+"\",\""+str(moodBottleText)+"\",\""+str(user_id)+"\")")    

    returnmsg = {"success": 1, "msg": "上传成功"}

    return returnmsg

@app.route("/moodBottlePositive")
def moodBottlePositive():
    category = request.args.get("category")
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from moodBottle where category = 0")    
    result=cursor.fetchall()
    total = len(result)
    print(total)
    randomNum = random.randint(0, total-1);
    print(randomNum)
    returnmsg = {"success": 1, "msg": "上传成功","result":result[randomNum]}
    # ,"result":result[randomNum]
    return returnmsg
@app.route("/moodBottleRandom")
def moodBottleRandom():
    category = request.args.get("category")
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from moodBottle where category = 1||category = 0||category = 2 ")    
    result=cursor.fetchall()
    total = len(result)
    print(total)
    randomNum = random.randint(0, total-1);
    print(randomNum)
    returnmsg = {"success": 1, "msg": "上传成功","result":result[randomNum]}
    # ,"result":result[randomNum]
    return returnmsg
@app.route("/moodBottleNagetive")
def moodBottleNagetive():
    category = request.args.get("category")
    cursor=connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from moodBottle where category = 2")    
    result=cursor.fetchall()
    total = len(result)
    print(total)
    randomNum = random.randint(0, total-1);
    print(randomNum)
    returnmsg = {"success": 1, "msg": "上传成功","result":result[randomNum]}
    # ,"result":result[randomNum]
    return returnmsg

# 上传头像
@app.route('/up_avatar' , methods=['post'])
def up_avatar():
    # 获取除了图片之外的其他信息
    user_id = request.form.get("user_id")
    user_id = str(user_id)

    # print(user_id + "----") 
    if user_id not in app.config['UPLOAD_FOLDER']:
        app.config['UPLOAD_FOLDER'] += ("/"+user_id)
    # print(app.config['UPLOAD_FOLDER'])
# 存图片的路径（不包括图片）
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    returnmsg = {"success": 0, "msg": "上传失败"}
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['file']
    # print(f)
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        print (fname)
        ext = fname.rsplit('.', 1)[1]
        new_filename = 'avatar' + '.' + ext
        f.save(os.path.join(file_dir, new_filename))
        file_path = os.path.join(file_dir, new_filename) # 把目标图片 input image 放到代码所处的文件夹里
        cursor=connectDB.cursor(pymysql.cursors.DictCursor)
        cursor.execute('Update user Set avatar="'+str(new_filename)+'" Where user_id ="'+user_id+'"')
        cursor.execute('Select avatar From user Where user_id = "'+ user_id +'"')
        result=cursor.fetchall()
        returnmsg = {"success": 1, "msg": "上传成功","result":result[0]}

    return returnmsg

@app.route('/myPage')
def myPage():
    user_id = request.args.get("user_id")
    user_id = str(user_id)
    cursor = connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute('Select * From user Where user_id = "' +user_id+'"')
    result = cursor.fetchall()
    returnmsg = {"success": 1, "msg": "获取成功","result":result[0]}
    return returnmsg
    
@app.route('/changeUsername')
def changeUsername():
    user_id = request.args.get("user_id")
    user_id = str(user_id)
    username = request.args.get("username")
    cursor = connectDB.cursor(pymysql.cursors.DictCursor)
    cursor.execute('Update user Set username="'+str(username)+'" Where user_id ="'+user_id+'"')
    cursor.execute('Select username From user Where user_id = "'+ user_id +'"')
    result = cursor.fetchall()
    returnmsg = {"success": 1, "msg": "获取成功","result":result[0]}
    return returnmsg


@app.route("/highLikeBoard")
def highLikeBoard():
    user_id = request.args.get("user_id")
    user_id = str(user_id)
    whiteBgcControl = request.args.get("whiteBgcControl")
    day = str(datetime.now()).split(' ')[0]
    cursor = connectDB.cursor(pymysql.cursors.DictCursor)
    # cursor.execute('Update happything Set light_user_id = "'+user_id+'" Where happything natural join (Select * From like Where light_user_id_1 = "'+ user_id +'")')
    if(str(whiteBgcControl) == "1"):
        cursor.execute('Select * From happything natural join user Where day = "'+ day +'"')
    if(str(whiteBgcControl) == "2"):
        cursor.execute('Select * From happything natural join user Where day = "'+ day +'"')
    if(str(whiteBgcControl) == "3"):
        cursor.execute('Select * From happything natural join user  ')
    result = cursor.fetchall()
    returnmsg = {"success": 1, "msg": "获取成功","result":result}
    return returnmsg



# 揭照片函数
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
def create_uuid(): #生成唯一的图片的名称字符串，防止图片显示时的重名问题
        nowTime = datetime.now().strftime("%Y%m%d%H%M%S");  # 生成当前时间
        randomNum = random.randint(0, 100);  # 生成的随机整数n，其中0<=n<=100
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum);
        uniqueNum = str(nowTime) + str(randomNum);
        return uniqueNum;
def fill_image(image):

    width, height = image.size

    # 选取长和宽中较大值作为新图片的边长
    new_image_length = width if width > height else height

    # 生成新图片[白底]，底色可配置其他颜色
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')

    # 将之前的图片input image 粘贴在新图上，居中
    if width > height: # 原图宽大于高，则填充图片的竖直维度  #(x,y)二元组表示粘贴上图相对下图的起始位置,是个坐标点
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))

    return new_image
def cut_image(image):

    width, height = image.size

    item_width =int(width /3) # 因为朋友圈一行放3张图

    box_list = []

    for i in range(0, 3):

        for j in range(0, 3):

            box = (j*item_width, i*item_width, (j+1)*item_width, (i+1)*item_width) # (left, top, right, bottom)

            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]

    return image_list
def save_images(image_list , file_dir):
    print(file_dir+"[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]")
    index = 1


    if(os.path.exists(file_dir+"/" + "1.png")):
        print('yes')
        for i in range(1,10):
            os.remove(file_dir +"/"+str(i)+".png")
            print(file_dir+"/"+str(i)+".png")
    else:
        print('no')
    for image in  image_list:
        
        image.save(file_dir  +"/"+ str(index) + '.png', 'PNG')

        index += 1



app.run(host="172.30.11.32",port=4444,debug=True)