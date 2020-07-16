<template>
	<view>
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="dayR_nav">
				<view class="dayR_title1" style="align-items: center;text-align: center;"><text class="shareExp">分享情绪</text></view>
			</view>
		</view>
		 <view class="Communitytotal">
			 <navigator url="happyPopcorn/happyPopcorn" class="Popcorn"><text class="communityText" style="color: rgb(251,189,105);">快乐爆米花</text></navigator >
			 <navigator url="moodBottle/moodBottle" class="MoodBottle"><text class="communityText" style="color: rgb(115,153,209);">情绪漂流瓶</text></navigator >
			 <navigator url="NAJIHouse/NAJIHouse" class="NAJIHouse"><text class="communityText" style="color: rgb(88,165,176);">纳己小木屋</text></navigator >
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
		background-color: rgb(235,245,246);
		text-align: center;
		line-height: 160upx;
	}
</style>
