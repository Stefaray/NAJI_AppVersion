<template>
	<view>
		<view class="top_view">
			<view class="getSpace2"></view>
		<!-- 	<view class="dayR_nav">
				
				<view class="dayR_title1" style="align-items: center;text-align: center;"><text class="shareExp">我的消息</text></view>
			</view> -->
			<view class="dayR_nav">
				<view class="dayR_back"><img @tap="isBack" src="/static/back.svg" class="svg_back"  /></view>
				<view class="dayR_title"><text class="dayR_titleText">我的消息</text></view>
			</view>
		</view>
		 <view class="Communitytotal">
			 <navigator url="happyPopcorn/happyPopcorn" class="Popcorn"><text class="communityText" style="color: rgb(251,189,105);">专属的每周杂志</text></navigator >
			 <navigator url="moodBottle/moodBottle" class="MoodBottle"><text class="communityText" style="color: rgb(115,153,209);">情绪/自杀预警</text></navigator >
			 <navigator url="NAJIHouse/NAJIHouse" class="NAJIHouse"><text class="communityText" style="color: rgb(243, 181, 162);">月度/年度报告</text></navigator >
			 <navigator url="happyPopcorn/happyPopcorn" class="Popcorn1"><text class="communityText" style="color: rgb(189, 153, 223);">情绪调节小技巧</text></navigator >
		 </view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			isBack(){
				
				uni.navigateBack({
					delta: 1
				});
			} , 
		}
	}
</script>

<style>
	.shareExp{
		font:normal bold 50upx "微软雅黑",arial,sans-serif;
		color: #448088;
	}
	.communityText{
		font:normal bold 40upx "微软雅黑",arial,sans-serif;
		
	}
	.dayR_title1{
		/* margin-left: 100upx; */
		flex: 3;
	}
	.Communitytotal{
		/* background-color: #0066CC; */
		width: 750upx;
		height: 865upx;
		display: flex;
		flex-direction: column;
		justify-content:space-around;
	}
	.Popcorn{
		
		width: 480upx;
		height: 160upx;
		margin: 0 auto;
		background-color: rgb(254,241,216);
		text-align: center;
		line-height: 160upx;
	}
	.Popcorn1{
		
		width: 480upx;
		height: 160upx;
		margin: 0 auto;
		background-color: rgb(237, 231, 243);
		text-align: center;
		line-height: 160upx;
	}
	.MoodBottle{
		
		width: 480upx;
		height: 160upx;
		margin: 0 auto;
		background-color: rgb(237,246,255);
		text-align: center;
		line-height: 160upx;
	}
	.NAJIHouse{
		
		width: 480upx;
		height: 160upx;
		margin: 0 auto;
		background-color: rgb(253, 234, 230);
		text-align: center;
		line-height: 160upx;
	}
</style>
