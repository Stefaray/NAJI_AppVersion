<template>
	<view>
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="commNav">
				<view class="commNav1"><img @tap="isBack" src="/static/back.svg" class="svg_back"  /></view>
				<view class="commNav2"><text class="shareExp">纳己小木屋</text></view>
				<view class="commNav3"><img @tap="isBack" src="/static/plus.svg" class="svg_back"  /></view>
			</view>
		</view>
		<view class="commList">
			<view class="commPer">
				<view class="commElement">
					<view class="commAvatar">
						<image src="../../../../static/community/NAJIHouse/1.png" mode="widthFix" class="imag"></image>
					</view>
					<view class="commTitle">
						<view><text class="commTitleText">抑郁症干预群</text></view>
						<view><text class="commTitleText">No.1106</text></view>
					</view>
					<view class="commTime">
						<text class="commTimeText">8:05PM</text>
					</view>
				</view>
				<view style="width: 750upx;height: 3upx;background-color: #dddddd;"></view>
			</view>
			<view class="commPer">
				<view class="commElement">
					<view class="commAvatar">
						<image src="../../../../static/community/NAJIHouse/2.png" mode="widthFix" class="imag"></image>
					</view>
					<view class="commTitle">
						<view><text class="commTitleText">焦虑症干预群</text></view>
						<view><text class="commTitleText">No.525</text></view>
					</view>
					<view class="commTime">
						<text class="commTimeText">10:05PM</text>
					</view>
				</view>
				<view  style="width: 750upx;height: 3upx;background-color: #dddddd;"></view>
			</view>
			<view class="commPer">
				<view class="commElement">
					<view class="commAvatar">
						<image src="../../../../static/community/NAJIHouse/3.png" mode="widthFix" class="imag"></image>
					</view>
					<view class="commTitle">
						<view><text class="commTitleText">积极心理训练营	</text></view>
						<view><text class="commTitleText">No.88</text></view>
					</view>
					<view class="commTime">
						<text class="commTimeText">6:11PM</text>
					</view>
				</view>
				<view  style="width: 750upx;height: 3upx;background-color: #dddddd;"></view>
			</view>
			<view class="comBottomBar"></view>
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
	.commNav{
		width: 680upx;
		display: flex;
		flex-direction: row;
		padding: 0 30upx;
		justify-content: space-between;
	}
	
/* ==================榜单元素css开始====================== */
	.commElement{
		padding: 10upx;
		height: 200upx;
		width: 750upx;
		/* background-color: #0066CC; */
		display: flex;
	}
	.commAvatar{
		
		height: 100%;
		flex: 3;
		/* background-color: #39B54A; */
		border: solid thin #dddddd;
		box-shadow: #dddddd;
	}
	.commTitle{
		padding-top: 20upx;
		padding-left: 20upx;
		flex: 5;
	}
	.commTime{
		flex: 2;
	}
	.imag{
		margin: 0upx auto;
		width: 90%;
	}
	.commTitleText{
		margin: 20upx 0 30upx 0;
		font:normal bold 40upx "微软雅黑",arial,sans-serif;
		color: #000000;
	}
	.commTimeText{
		font:normal normal 30upx "宋体",arial,sans-serif;
		color: #448088;
	}
/* ==================榜单元素css结束====================== */



	.comBottomBar{
		width: 750upx;
		height: 100upx;
		background-color: rgb(245,249,250);
		/* 固定在底部 */
		position: fixed;
		bottom: 0;
	}
</style>
