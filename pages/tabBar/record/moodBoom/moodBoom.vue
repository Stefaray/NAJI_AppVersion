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
			<view class="moodB_date bord space1 ">{{timeString}}</view>
			<view class="feelTitle space2">
				<text class="feelText">此刻心情</text>	
			</view>
			<view class="moodExpression">
				<!-- <image src="../../../../static/u78.png"></image> -->
				<!-- <view style="width: 665upx;height: 150upx;background-color: #448088;"></view> -->
				<view class="perExpression">
					<image class="iconExpression" src="../../../../static/record/expression/1.png"></image>
					<view><text class="expressionText">开心</text></view>
				</view>
				<view class="perExpression">
					<image class="iconExpression" src="../../../../static/record/expression/2.png"></image>
					<view><text class="expressionText">愤怒</text></view>
				</view>
				<view class="perExpression">
					<image class="iconExpression" src="../../../../static/record/expression/3.png"></image>
					<view><text class="expressionText">悲伤</text></view>
				</view>
				<view class="perExpression">
					<image class="iconExpression" src="../../../../static/record/expression/4.png"></image>
					<view><text class="expressionText">恐惧</text></view>
				</view>
				<view class="perExpression">
					<image class="iconExpression" src="../../../../static/record/expression/5.png"></image>
					<view ><text class="expressionText">焦虑</text></view>
				</view>
				<view class="perExpression">
					<image class="iconExpression" src="../../../../static/record/expression/6.png"></image>
					<view><text class="expressionText">感动</text></view>
				</view>
			</view>
			<view class="actTag">
				<view class="tagTitle"><text class="tagText">主题标签</text><img src="/static/plus.svg" class="svg_plus"  /></view>
					<view class="grid col-4 padding-sm">
						<block v-for="item in tabs" :key="item.id">
							<view class="margin-tb-sm text-center"><button class="cu-btn round shadow">{{item.value}}</button></view>
						
						</block>
					</view>
					
					<!-- <button class="cu-btn round shadow tagChange">其他</button> -->
			</view>
			
			<view class="moodRecord">
				<view class="moodRecordTitle"><text class="moodRecordText">记录一下</text></view>
				<view class="noteArea"></view>
			</view>
		</view>	
		
	</view>
</template>

<script>
	
	var today = new Date();//获得当前日期
	var year = today.getFullYear();//获得年份
	var month = today.getMonth() + 1;//此方法获得的月份是从0---11，所以要加1才是当前月份
	var day = today.getDate();//获得当前日期
	var hour = today.getHours();
	var minute = today.getMinutes();
	var timeString = year+ " / " + month + " / " + day + " " + hour + ": " + minute;
	var tabs = [];
	
	// 标签栏开始
	tabs = [
	      {
	        id: 0,
	        value: "亲情",
	        isActive: true
	      },
	      {
	        id: 1,
	        value: "爱情",
	        isActive: false
	      },
	      {
	        id: 2,
	        value: "友情",
	        isActive: false
	      },
		  {
		    id: 3,
		    value: "日常",
		    isActive: false
		  },
		  {
		    id: 4,
		    value: "时事",
		    isActive: false
		  },
		  {
		    id: 5,
		    value: "爱好",
		    isActive: false
		  },
		  {
		    id: 6,
		    value: "成就",
		    isActive: false
		  },
		  {
		    id: 7,
		    value: "财务",
		    isActive: false
		  },
		  {
		    id: 8,
		    value: "美食",
		    isActive: false
		  },
		  {
		    id: 9,
		    value: "旅行",
		    isActive: false
		  },
		  {
		    id: 10,
		    value: "创伤",
		    isActive: false
		  },
		  {
		    id: 11,
		    value: "陌生人",
		    isActive: false
		  }
	    ];
	//标签栏结束
	
	export default {
		data() {
			return {
				timeString,
				tabs
			}
		},
		methods: {
			isBack(){
				uni.navigateBack({
				    delta: 1
				});
			}
		}
	}
</script>

<style>
	@import "/colorui/main.css";
	@import "/colorui/icon.css";
	.svg_plus{
		margin: 30upx 0 0 25upx;
		width: 50upx;
		height: 45upx;
		/* display: inline-block; */
	}
	.tagChange{
		background-color: #99D3C9 !important;
		color: #ffffff;
	}
	.noteArea{
		background-color: #F6F9FA;
		width: 665upx;
		height: 290upx;
		border: 5upx solid #ECF7FC;
		border-radius: 15upx;
		/* box-shadow: 5px 5px 5px #ECF7FC; */
		margin: 0 auto 40upx;
	}
	.space1{
		margin: 20upx 0 20upx 30upx;
	}
	.space2{
		margin: 30upx 0 30upx 30upx;
	}
	.space3{
		margin: 30upx 0 30upx 20upx;
	}
	/* 包含六个表情的总块 */
	.moodExpression{
		margin: 20upx 0 20upx 34upx;
		display: flex;
		flex-direction: row;
	}
	/* 六个表情的单块 */
	.perExpression{
		flex:1;
		/* height: 100%; */
		/* width: 100upx; */
	}
	/*  */
	.iconExpression{
		width: 89upx;
		height: 80upx;
		/* transform: scale(10%); */
	}
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
	/* 此刻心情 */
	.feelTitle{
		margin: 40upx 0 20upx 34upx;
	}
	/* 主题标签 */
	.tagTitle{
		margin: 20upx 0 0upx 34upx;
	}
	/* 记录一下 */
	.moodRecordTitle{
		margin: 20upx 0 20upx 34upx;
	}
	
</style>
