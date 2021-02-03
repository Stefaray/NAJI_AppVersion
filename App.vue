<script>
	

	
export default {
	
	onLaunch: function() {
		uni.getStorageSync()({//获得保存在本地的用户信息
			key: 'token_user_id',
			success:(res) => {
				this.login(res.data);
				if(res.data == ''){
					uni.switchTab({
						url: "pages/login/index"
					});
				}
				else{
					uni.switchTab({
						url: "../tabBar/record/record"
					});
				}
			}
		});
		
	},
	onShow: function() {
		console.log('App Show');
	},
	onHide: function() {
		console.log('App Hide');
	},
	methods:{
		isBack(){
			
			uni.navigateBack({
				delta: 1
			});
		} , 
	}
};
</script>

<style>
	
	  /* 你的项目css */

/* 解决头条小程序组件内引入字体不生效的问题 */

/* #ifdef MP-TOUTIAO */
@font-face {
	font-family: uniicons;
	src: url('/static/uni.ttf');
}
/* #endif */

/* 顶部栏 */
.top_view{
	height: 180upx;
	
	background-color: #F4F8F9;
/* 	padding: 60upx;
	padding-left: 100upx; */
}

.getSpace1{
	height: 50upx;
}
.getSpace2{
	height: 100upx;
	text-align:center;
}
.title_font{
	font:normal bold 50upx "微软雅黑",arial,sans-serif;
	color: #448088;
}
.content_text{
	font:normal normal 40upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 上面自定义tab栏 */
/* 返回按钮 */
	.svg_back , .svg_search{
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
/*上面自定义tab栏  */
/* 首页----今天还没有记录哦 */
.plus_text{
	font:normal normal 45upx "楷体",arial,sans-serif;
	/* color: #448088; */
}
/* 首页----卡片日期 */
.record_date{
	font:normal bold 36upx "微软雅黑",arial,sans-serif;
	color: #448088;
}
/* 首页----压力值 混乱值 活力值 平静值 */
.record_values{
	font:normal bold 30upx "微软雅黑",arial,sans-serif;
	color: #448088;
}
/* 每日小结----标题 */
.dayR_titleText{
	font:normal bold 60upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 每日小结----记录一下今天的情绪状态吧 */
.dayR_moodValueTitleText{
	font:normal bold 44upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 每日小结----日期 */
.dayR_date{
	font:normal bold 40upx "微软雅黑",arial,sans-serif;
	color: #448088;
}
/* 每日小结----压力值 混乱值 活力值 平静值 */
.dayR_values{
	font:normal bold 40upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 每日小结----定格今天的快乐事 */
.happyThingText{
	font:normal bold 44upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 每日小结----随手小记 */
.noteText{
	font:normal bold 44upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 灰色字体 */
.placeholderText{
	font:normal normal 36upx "宋体",arial,sans-serif;
	color: #dddddd;
}
/* 灰色字体 */
.placeholderText1{
	font:normal normal 33upx "宋体",arial,sans-serif;
	color: #dddddd;
}
.placeholderTextGreen{
	font:normal normal 30upx "宋体",arial,sans-serif;
	color: #448088;
}

/* 情绪爆炸----时间 */
.moodB_date{
	font:normal bold 40upx "微软雅黑",arial,sans-serif;
	color: #448088;
}
/*  */
.moodB_content{
	font:normal normal 34upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 情绪爆炸----此刻心情 */
.feelText{
	font:normal bold 40upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 情绪爆炸----主题标签 */
.tagText{
	font:normal bold 40upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 情绪爆炸----记录一下 */
.moodRecordText{
	font:normal bold 40upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 情绪爆炸----六个表情的文本 */
.expressionText{
	font:normal normal 28upx "宋体",arial,sans-serif;
	color: #448088;
}

/* 文字后面的图标 */
.iconAfterword__happyThing{
	width: 60upx;
	height: 60upx;
	/* padding-top: 10upx; */
	margin: 0upx 0 0 20upx;
}
/* 	每日小结----不错！活力满满 */
.card_bottomText{
	font:normal bold 40upx "微软雅黑",arial,sans-serif;
	color: #448088;
}
/* 情绪爆炸----弹出层表情 */
.expressionTextPopupView{
	margin: 20upx auto 40upx;
}
/*  */
.expressionTextPopup{
	font:normal normal 50upx "宋体",arial,sans-serif;
	color: #448088;
}
/* 情绪爆炸---卡片---开心 */
.expressionText{
	
	font:normal normal 34upx "宋体",arial,sans-serif;
	color: #448088;
}
.bord{
	font:bold !important
}
/* 顶部栏固定样式 */
.dayR_title1{
		/* margin-left: 100upx; */
		flex: 3;
	}	
.shareExp{
	font:normal bold 50upx "微软雅黑",arial,sans-serif;
	color: #448088;
}
</style>
