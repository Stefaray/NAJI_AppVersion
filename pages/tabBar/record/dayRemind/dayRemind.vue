<!-- 
	数据接口
	dayString
	targetOption1
	targetOption2
	targetOption3
	targetOption4
	targetOption5
	notedata1
	notedata2
	notedata3
	this.$note1
 -->

<template>
	<view>
		
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="dayR_nav">
				<view class="dayR_back"><img @tap="isBack" src="/static/back.svg" class="svg_back"  /></view>
				<view class="dayR_title"><text class="dayR_titleText">每日小结</text></view>
			</view>
		</view>
		<view class="content_view">
			<view class="dayR_date "><text class="dayR_date">{{dayString}}</text></view>
			<view class="moodValueView">
				<view class="moodValueTitle">
					<text class="dayR_moodValueTitleText">记录一下今天的情绪状态吧~</text>
				</view>
				
			<!-- 	<view class="moodValue">
					<view class="values">
						<view class="firstValue"><text class="dayR_values">压力值</text></view>
						<view class="secondValue"><text class="dayR_values">混乱值</text></view>
					</view>
					<view class="values">
						<view class="firstValue"><text class="dayR_values">活力值</text></view>
						<view class="secondValue"><text class="dayR_values">平静值</text></view>
					</view>
				</view> -->
				
				<view class="questionnaire">
					<view class="score">
						<text class="scoreText">非常不符合</text>
						<text class="scoreText">较不符合</text>
						<text class="scoreText">一般</text>
						<text class="scoreText">较符合</text>
						<text class="scoreText">非常符合</text>
					</view>
					<view class="question">
						<view style="padding-left: 30upx;">
							<text class="title">{{questions[0]}}</text>
						</view>
						<view class="options" >
							<view class="perOption" :class="(targetOption1=='1')?'targetOption':''" @tap="chooseOption1" data-index="1"></view>
							<view class="perOption" :class="(targetOption1=='2')?'targetOption':''" @tap="chooseOption1" data-index="2"></view>
							<view class="perOption" :class="(targetOption1=='3')?'targetOption':''" @tap="chooseOption1" data-index="3"></view>
							<view class="perOption" :class="(targetOption1=='4')?'targetOption':''" @tap="chooseOption1" data-index="4"></view>
							<view class="perOption" :class="(targetOption1=='5')?'targetOption':''" @tap="chooseOption1" data-index="5"></view>
						 </view>
					</view>
					<view class="question">
						<view style="padding-left: 30upx;">
							<text class="title">{{questions[1]}}</text>
						</view>
						<view class="options" >
							<view class="perOption" :class="(targetOption2=='1')?'targetOption':''" @tap="chooseOption2" data-index="1"></view>
							<view class="perOption" :class="(targetOption2=='2')?'targetOption':''" @tap="chooseOption2" data-index="2"></view>
							<view class="perOption" :class="(targetOption2=='3')?'targetOption':''" @tap="chooseOption2" data-index="3"></view>
							<view class="perOption" :class="(targetOption2=='4')?'targetOption':''" @tap="chooseOption2" data-index="4"></view>
							<view class="perOption" :class="(targetOption2=='5')?'targetOption':''" @tap="chooseOption2" data-index="5"></view>
						 </view>
					</view>
					<view class="question">
						<view style="padding-left: 30upx;">
							<text class="title">{{questions[2]}}</text>
						</view>
						<view class="options" >
							<view class="perOption" :class="(targetOption3=='1')?'targetOption':''" @tap="chooseOption3" data-index="1"></view>
							<view class="perOption" :class="(targetOption3=='2')?'targetOption':''" @tap="chooseOption3" data-index="2"></view>
							<view class="perOption" :class="(targetOption3=='3')?'targetOption':''" @tap="chooseOption3" data-index="3"></view>
							<view class="perOption" :class="(targetOption3=='4')?'targetOption':''" @tap="chooseOption3" data-index="4"></view>
							<view class="perOption" :class="(targetOption3=='5')?'targetOption':''" @tap="chooseOption3" data-index="5"></view>
						 </view>
					</view>
					<view class="question">
						<view style="padding-left: 30upx;">
							<text class="title">{{questions[3]}}</text>
						</view>
						<view class="options" >
							<view class="perOption" :class="(targetOption4=='1')?'targetOption':''" @tap="chooseOption4" data-index="1"></view>
							<view class="perOption" :class="(targetOption4=='2')?'targetOption':''" @tap="chooseOption4" data-index="2"></view>
							<view class="perOption" :class="(targetOption4=='3')?'targetOption':''" @tap="chooseOption4" data-index="3"></view>
							<view class="perOption" :class="(targetOption4=='4')?'targetOption':''" @tap="chooseOption4" data-index="4"></view>
							<view class="perOption" :class="(targetOption4=='5')?'targetOption':''" @tap="chooseOption4" data-index="5"></view>
						 </view>
					</view>
					<view class="question">
						<view style="padding-left: 30upx;">
							<text class="title">{{questions[4]}}</text>
						</view>
						<view class="options" >
							<view class="perOption" :class="(targetOption5=='1')?'targetOption':''" @tap="chooseOption5" data-index="1"></view>
							<view class="perOption" :class="(targetOption5=='2')?'targetOption':''" @tap="chooseOption5" data-index="2"></view>
							<view class="perOption" :class="(targetOption5=='3')?'targetOption':''" @tap="chooseOption5" data-index="3"></view>
							<view class="perOption" :class="(targetOption5=='4')?'targetOption':''" @tap="chooseOption5" data-index="4"></view>
							<view class="perOption" :class="(targetOption5=='5')?'targetOption':''" @tap="chooseOption5" data-index="5"></view>
						 </view>
					</view>
					<!-- <view class="question">
						<view style="padding-left: 30upx;">
							<text class="title">{{questions[5]}}</text>
						</view>
						<view class="options" >
							<view class="perOption" :class="(targetOption5=='1')?'targetOption':''" @tap="chooseOption5" data-index="1"></view>
							<view class="perOption" :class="(targetOption5=='2')?'targetOption':''" @tap="chooseOption5" data-index="2"></view>
							<view class="perOption" :class="(targetOption5=='3')?'targetOption':''" @tap="chooseOption5" data-index="3"></view>
							<view class="perOption" :class="(targetOption5=='4')?'targetOption':''" @tap="chooseOption5" data-index="4"></view>
							<view class="perOption" :class="(targetOption5=='5')?'targetOption':''" @tap="chooseOption5" data-index="5"></view>
						 </view>
					</view> -->
				</view>
				
			</view>
		<!-- 图文开始 -->
			<view class="happyThing">
				<view class="happyThingTitle">
					<text class="happyThingText">定格今天的快乐事</text>
					<image src="../../../../static/record/happyThing.png" class="iconAfterword__happyThing"></image>
				</view>
				<view class="picText">
					<view class="avatar">
						<view class="cu-avatar round lg" style="background-image:url(http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2FappIcon.svg);"></view>
					</view>
					<view class="avatarText"  @tap="showModal" data-target="1">
						<view class="avatarTextView">
							<text class="placeholderText placeholderTexthide">{{V_notedata1}}</text>
						</view>
					</view>
				</view>
				
				<view class="picText">
					<view class="avatar">
						<view class="cu-avatar round lg" style="background-image:url(http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2FappIcon.svg);"></view>
					</view>
					<view class="avatarText" @tap="showModal" data-target="2">
						<view class="avatarTextView">
							<text class="placeholderText placeholderTexthide">{{V_notedata2}}</text>
						</view>
					</view>
				</view>
				
				<view class="picText">
					<view class="avatar">
						<view class="cu-avatar round lg" style="background-image:url(http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2FappIcon.svg);"></view>
					</view>
					<view class="avatarText" @tap="showModal" data-target="3">
						<view class="avatarTextView">
							<text class="placeholderText">{{V_notedata3==''?'也可以写自己期待的事情哦':V_notedata3}}</text>
						</view>
					</view>
				</view>
			</view>
			<!-- <textarea background-color="#dddddd" value="666666"></textarea> -->
			
			<!-- 弹出框内容开始 -->
			<view class="cu-modal" :class="modalName==1?'show':''">
				<view class="cu-dialog">
					
					<view class="cu-bar bg-white justify-end">
						<view class="actionLeft" @tap="noModal" >
							<text class="cuIcon-close text-theme"></text>
						</view>	
						<view class="content"><text class="text-theme" style="font:normal bold 32upx '宋体',arial,sans-serif;">记下你的快乐事吧~</text></view>
						<view class="action" @tap="yesModal">
							<text class="cuIcon-check text-theme"></text>
						</view>
					</view>
					<view class="padding-xl">
						<textarea :value="notedata1" style="font:normal bold 34upx '宋体' ;" @blur="bindTextAreaBlur1"></textarea>
						<!-- <input type="idcard" style="font:normal bold 34upx '宋体' ;" /> -->
					</view>
				</view>
			</view>
			<!-- 弹出框内容结束 -->
			<!-- 弹出框内容开始 -->
			<view class="cu-modal" :class="modalName==2?'show':''">
				<view class="cu-dialog">
					
					<view class="cu-bar bg-white justify-end">
						<view class="actionLeft" @tap="noModal" >
							<text class="cuIcon-close text-theme"></text>
						</view>	
						<view class="content"><text class="text-theme" style="font:normal bold 32upx '宋体',arial,sans-serif;">记下你的快乐事吧~</text></view>
						<view class="action" @tap="yesModal">
							<text class="cuIcon-check text-theme"></text>
						</view>
					</view>
					<view class="padding-xl">
						<textarea :value="notedata2"  style="font:normal bold 34upx '宋体' ;" @blur="bindTextAreaBlur2"></textarea>
						<!-- <input type="idcard" style="font:normal bold 34upx '宋体' ;" /> -->
					</view>
				</view>
			</view>
			<!-- 弹出框内容结束 -->
			<!-- 弹出框内容开始 -->
			<view class="cu-modal" :class="modalName==3?'show':''">
				<view class="cu-dialog">
					
					<view class="cu-bar bg-white justify-end">
						<view class="actionLeft" @tap="noModal" >
							<text class="cuIcon-close text-theme"></text>
						</view>	
						<view class="content"><text class="text-theme" style="font:normal bold 32upx '宋体',arial,sans-serif;">记下你的快乐事吧~</text></view>
						<view class="action" @tap="yesModal">
							<text class="cuIcon-check text-theme"></text>
						</view>
					</view>
					<view class="padding-xl">
						<textarea :value="notedata3"  style="font:normal bold 34upx '宋体' ;" @blur="bindTextAreaBlur3"></textarea>
						<!-- <input type="idcard" style="font:normal bold 34upx '宋体' ;" /> -->
					</view>
				</view>
			</view>
			<!-- 弹出框内容结束 -->
	<!-- 图文结束 -->
	
	
			<view class="notetitle">
				<text class="noteText">随手小记</text>
			</view>
			<navigator url="../../../editor/editor" class="note">
				<text class="placeholderText">
					简单写写今天对你影响最大的事吧
				</text>
			</navigator>
		</view>
		
	</view>
</template>

<script>
	
	var today = new Date();//获得当前日期
	var year = today.getFullYear();//获得年份
	var month = today.getMonth() + 1;//此方法获得的月份是从0---11，所以要加1才是当前月份
	var day = today.getDate();//获得当前日期
	var dayString = year+ "/" + month + "/" + day;
	
	
	
	export default {
		data() {
			return {
				dayString,
				notedata : '',
				notedata1: '',
				notedata2: '',
				notedata3: '',
				modalName: 0,
				happyThingId:0,
				// targetOption:0,
				targetOption1:0,
				targetOption2:0,
				targetOption3:0,
				targetOption4:0,
				targetOption5:0,
				V_notedata1:'',
				V_notedata2:'',
				V_notedata3:'',
				

				
				answer:[],
				
				questions :
				[
					'我感觉今天对什么都不感兴趣',
					'我觉得今天过度亢奋',
					'我今天很少觉得紧张和着急',
					'我感觉今天很有活力',
					'我昨晚较快入睡且一天睡的很好',
					'我感觉压力有点大'
				]
			}
		},
		onLoad:function(option){
			const item = JSON.parse(decodeURIComponent(option.item));
			
			var tmp_str = item.targetOption.split(' ')
			var total = [];
			console.log(tmp_str.length)
			for(var j=0; j<tmp_str.length; j++){
				total[j] = parseInt(tmp_str[j])
			}
			this.targetOption1 = total[0]
			this.targetOption2 = total[1]
			this.targetOption3 = total[2]
			this.targetOption4 = total[3]
			this.targetOption5 = total[4]
			
			this.notedata1 = item.notedata1
			this.notedata2 = item.notedata2
			this.notedata3 = item.notedata3
			
			this.dayString = item.dayString
			
			this.$store.commit("ChangeNote1",item.dayNote)
			
			console.log(item)
		},
		methods: {
			bindTextAreaBlur1: function (e) {
				
				this.notedata1 = e.detail.value;
				console.log(this.notedata1)
				if(this.notedata1.length > 9){
					this.V_notedata1 = this.notedata1.slice(0,9) + '...'
				}
				else{
					this.V_notedata1 = this.notedata1
				}
			},
			bindTextAreaBlur2: function (e) {
				this.notedata2 = e.detail.value;
				console.log(this.notedata2)
				if(this.notedata2.length > 9){
					this.V_notedata2 = this.notedata2.slice(0,9) + '...'
				}
				else{
					this.V_notedata2 = this.notedata2
				}
			},
			bindTextAreaBlur3: function (e) {
				this.notedata3 = e.detail.value;
				console.log(this.notedata3)
				if(this.notedata3.length > 9){
					this.V_notedata3 = this.notedata3.slice(0,9) + '...'
				}
				else{
					this.V_notedata3 = this.notedata3
				}
			},
			chooseOption1(e){
				this.targetOption1 = e.target.dataset.index
			},	
			chooseOption2(e){
				this.targetOption2 = e.target.dataset.index
			},	
			
			chooseOption3(e){
				this.targetOption3 = e.target.dataset.index
			},	
			chooseOption4(e){
				this.targetOption4 = e.target.dataset.index
			},	
			chooseOption5(e){
				this.targetOption5 = e.target.dataset.index
			},	
			
			
			
			isBack(){
				var tmp = this.$store.state.note1
				console.log(tmp)
				
				uni.request({
					url:this.$url+'/dayRemind',
					data: {
						user_id: this.$store.state.token_user_id,
						dayString: 	this.dayString	,
						targetOption:this.targetOption1+" "+this.targetOption2+" "+this.targetOption3+" "+this.targetOption4+" "+this.targetOption5,
						notedata1:	this.notedata1,
						notedata2:	this.notedata2,
						notedata3:	this.notedata3,
						dayNote: 	tmp
					},
					method:"GET",
					success:(res) => {
						console.log(res.data.status)
						
						if(res.data.new !=  ""){
							if(res.data.status == -1 || res.data.status == 0)
								this.$store.commit("UNSHIFTdayRemind",res.data.new[0])
							// uni.navigateBack({
							//     delta: 1
							// });
						}
						if(res.data.old != ""){
							// console.log(res.data.old[0])
							if(res.data.status == -1 || res.data.status == 0)
								this.$store.commit("UPDATEdayRemind",res.data.old[0])
								
							// uni.navigateBack({
							//     delta: 1
							// });
							
							// uni.switchTab({
							// 	url:"/pages/tabBar/record/record"
							// });
							// uni.redirectTo({
							// 	url:"/pages/tabBar/record/record"
							// })
						}
						uni.navigateBack({
						    delta: 1
						});
						this.$store.commit("ChangeNote1","")
						
						
					},
					
				})
				
			},
			showModal(e) {				
				this.modalName = e.currentTarget.dataset.target;
			},
			yesModal(e) {
				this.modalName = 0
			},
			noModal(e) {
				this.modalName = 0
				this.notedata = ''
			},
		}
	}
</script>

<style>
	@import "/colorui/main.css";
	@import "/colorui/icon.css";
	.justify-end {
		justify-content: space-between;
		margin-left: 30upx;
	}
	
	.picText{
		width: 685upx;
		height: 120upx;
		/* background-color: #007AFF; */
		margin: 40upx auto 0	;
		display: flex;
	}
	.picText .avatar{
		flex: 1;
		display: flex;
	    justify-content: center;
	    align-items: center;
	}
	.picText .avatarText{
		flex: 3;
		display: flex;
	}
	.picText .avatarText .avatarTextView{
		width: 100%;
		height: 100%;
		border: 5upx solid #ECF7FC;
		border-radius: 15upx;
		/* box-shadow: 5px 5px 5px #ECF7FC; */
		text-align:center;	
		line-height:120upx;
		

	}
	
	.note{
		width: 615upx;
		height: 150upx;
		border: 5upx solid #ECF7FC;
		border-radius: 15upx;
		/* box-shadow: 5px 5px 5px #ECF7FC; */
		margin: 0 auto 40upx;
		/* 灰色字体居中 */
		text-align:center;
		line-height:150upx;
	}
/* 	.distinct{
		text-align:center;
		line-height:150upx;
	} */
	
	/* 返回按钮 */
	.svg_back{
		width: 60upx;
		height: 60upx;
	}
	.dayR_nav{
		display: flex;
		flex-direction: row;
		
	}
	.dayR_back{
		flex: 1;
		text-align:center;
	}
	.dayR_title{
		margin-left: 100upx;
		flex: 3;
	}
	
	
	/* 日期 */
	.dayR_date{
		margin: 20upx 0 20upx 18upx;
	}
	/* 记录一下今天的情绪状态吧 */
	.moodValueTitle{
		margin: 20upx 0 20upx 34upx;
	}
	/* 压力值 混乱值 活力值 平静值  开始 */
	.moodValue{
		flex: 3;
		flex-direction: column;
		display: flex;
	}
	.values{
		flex: 1;
		flex-direction: row;
		display: flex;
		padding-left: 30upx;
		margin: 15upx 0;
	}
	.firstValue{
		flex: 1;
	}
	.secondValue{
		flex: 1;
	}
	/* 压力值 混乱值 活力值 平静值  结束 */
	/* 文字块----定格今天的快乐事 */
	.happyThingTitle{
		margin: 20upx 0 20upx 34upx;
	}
	/* 文字块----随手小记 */
	.notetitle{
		margin: 20upx 0 20upx 34upx;
	}
	/* ----------------------------问卷区域---------------------------- */
	.questionnaire{
		width: 750upx;
		
	}
	.score{
		margin: 0 auto;
		width: 750upx;
		height: 60upx;
		background-color: rgb(243,245,247);
		display: flex;
		justify-content: space-between;
		
	}
	.scoreText{
		width: 150upx;
		font:normal normal 26upx "宋体",arial,sans-serif;
		color: #448088;
		line-height: 60upx;
	}
	.title{
		font:normal normal 34upx "宋体",arial,sans-serif;
		color: #448088;
	}
	.options{
		width: 700upx;
		display: flex;
		justify-content: space-around;
		padding-top: 20upx;
	}
	.perOption{
		width: 40upx;
		height: 40upx;
		/* background-color: #448088; */
		border-radius: 50%;
		border: #448088 solid 3upx;
	}
	.targetOption{
		background-color: #448088;
	}
		
</style>
