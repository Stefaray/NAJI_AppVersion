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
				<view class="moodValue">
					<view class="values">
						<view class="firstValue"><text class="dayR_values">压力值</text></view>
						<view class="secondValue"><text class="dayR_values">混乱值</text></view>
					</view>
					<view class="values">
						<view class="firstValue"><text class="dayR_values">活力值</text></view>
						<view class="secondValue"><text class="dayR_values">平静值</text></view>
					</view>
					
				</view>
			</view>
		<!-- 图文开始 -->
			<view class="happyThing">
				<view class="happyThingTitle">
					<text class="happyThingText">定格今天的快乐事</text>
					<image src="../../../../static/record/happyThing.png" class="iconAfterword__happyThing"></image>
				</view>
				<view class="picText" @tap="showModal" data-target="Modal">
					<view class="avatar">
						<view class="cu-avatar round lg" style="background-image:url(http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fray34.jpg);"></view>
					</view>
					<view class="avatarText">
						<view class="avatarTextView"></view>
					</view>
				</view>
				
				<view class="picText" @tap="showModal" data-target="Modal">
					<view class="avatar">
						<view class="cu-avatar round lg" style="background-image:url(http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fray34.jpg);"></view>
					</view>
					<view class="avatarText">
						<view class="avatarTextView"></view>
					</view>
				</view>
				
				<view class="picText" @tap="showModal" data-target="Modal">
					<view class="avatar">
						<view class="cu-avatar round lg" style="background-image:url(http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fray34.jpg);"></view>
					</view>
					<view class="avatarText distinct">
						<view class="avatarTextView">
							<text class="placeholderText">也可以写自己期待的事情哦</text>
						</view>
					</view>
				</view>
			</view>
			
			<!-- 弹出框内容开始 -->
			<view class="cu-modal" :class="modalName=='Modal'?'show':''">
				<view class="cu-dialog">
					
					<view class="cu-bar bg-white justify-end">
						<view class="actionLeft" @tap="hideModal" >
							<text class="cuIcon-close text-theme"></text>
						</view>	
						<view class="content"><text class="text-theme" style="font:normal bold 32upx '宋体',arial,sans-serif;">记下你的快乐事吧~</text></view>
						<view class="action" @tap="hideModal">
							<text class="cuIcon-check text-theme"></text>
						</view>
					</view>
					<view class="padding-xl">
						<textarea style="font:normal bold 34upx '宋体' ;"></textarea>
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
	var dayString = year+ " / " + month + " / " + day;
	
	
	export default {
		data() {
			return {
				dayString,
				modalName: null,
			}
		},
		methods: {
			isBack(){
				uni.navigateBack({
				    delta: 1
				});
			},
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
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
	    float:left;
	    width:20%;
		flex: 1;
		display: flex;
	    justify-content: center;
	    align-items: center;
	}
	.picText .avatarText{
	    float:right;
	    width:80%;
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
</style>
