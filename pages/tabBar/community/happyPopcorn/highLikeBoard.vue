<template>
	<view>
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="highLikeNav">
				<view ><img @tap="isBack" src="/static/back.svg" class="svg_back"  /></view>
				<view ><text class="highLike">高赞榜</text></view>
				<view ><img @tap="" src="/static/search.svg" class="svg_search"  /></view>
			</view>
		</view>
		
		<!-- 实时榜 日榜 月榜 -->
		<view class="popcNav2">
			<button @tap="boardSwitch1" class="switchButton" :class="whiteBgcControl==1?'whiteBgc':''"><text style="color: #448088;">实时榜</text></button>
			<button @tap="boardSwitch2" class="switchButton" :class="whiteBgcControl==2?'whiteBgc':''"><text style="color: #448088;">日榜</text></button>
			<button @tap="boardSwitch3" class="switchButton" :class="whiteBgcControl==3?'whiteBgc':''"><text style="color: #448088;">月榜</text></button>
		</view>
		
		
<!-- ============== 榜单开始 ==================== -->
		<view class="highLikePer" v-for="item in happything_str">
			<view class="highLikeElement">
				<view class="highLikeAvatar">
					<view class="avatar">
						<view class="cu-avatar round lg"  :style="{backgroundImage: 'url('+$photoUrl + item.user_id + '/' + item.avatar+')'}" ></view>
					</view>
				</view>
				<view class="highLikeTitle">
					<view class="highLikeID"><text class="highLikeIDText">{{item.username}}</text></view>
					<view class="highLikeContent"><text class="highLikeContentText">{{item.content}}</text></view>
				</view>
				<view class="highLikeTime_Like">
					<view>
						<text class="highLikeTimeText">{{item.time}}</text>
					</view>
					
					<view class="highLikeTime_Like2">
						<image @tap="light" :data-index="item.happything_id" src="../../../../static/community/happyPopcorn/star.svg" class="talkStar"></image>
						<text class="likeCount">{{item.like}}</text>
					</view>
				</view>
			</view>
			<view style="width: 750upx;height: 3upx;background-color: #dddddd;"></view>
		</view>
<!-- ============== 榜单结束 ==================== -->		
		<view class="highLikePer">
			<view class="highLikeElement">
				<view class="highLikeAvatar">
					<view class="avatar">
						<view class="cu-avatar round lg" style="background-image:url(http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fray34.jpg);"></view>
					</view>
				</view>
				<view class="highLikeTitle">
					<view class="highLikeID"><text class="highLikeIDText">Ray</text></view>
					<view class="highLikeContent"><text class="highLikeContentText">鹏宇哥哥好帅呀！！！</text></view>
				</view>
				<view class="highLikeTime_Like">
					<view>
						<text class="highLikeTimeText">8:05PM</text>
					</view>
					
					<view class="highLikeTime_Like2">
						<image src="../../../../static/community/happyPopcorn/star.svg" class="talkStar"></image>
						<text class="likeCount">8888</text>
					</view>
				</view>
			</view>
			<view style="width: 750upx;height: 3upx;background-color: #dddddd;"></view>
		</view>
		
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				whiteBgcControl:1,
				happything_str:[],
				Mylike_str:[]
			}
		},
		onLoad() {
			
			uni.request({
				url:this.$url+'/highLikeBoard',
				method:"GET",
				data:{
					whiteBgcControl:this.whiteBgcControl,
					user_id: this.$store.state.token_user_id
				},
				success: (res) => {
					console.log(res.data)
					this.happything_str = res.data.result;
				}
			})
			
		},
		methods: {
			light(e){
				console.log(e.currentTarget.dataset.index)
				
			},
			isBack(){
				
				uni.navigateBack({
					delta: 1
				});
			} , 
			
			boardSwitch1(){
				this.whiteBgcControl = 1;
			},
			boardSwitch2(){
				this.whiteBgcControl = 2;
			},
			boardSwitch3(){
				this.whiteBgcControl = 3;
			},
		}
	}
</script>

<style>
/* ===========colorUI引用开始================== */
/* 头像 */
.cu-avatar {
	font-variant: small-caps;
	margin: 0;
	padding: 0;
	display: inline-flex;
	text-align: center;
	justify-content: center;
	align-items: center;
	background-color: #ccc;
	color: #ffffff;
	white-space: nowrap;
	position: relative;
	width: 64upx;
	height: 64upx;
	background-size: cover;
	background-position: center;
	vertical-align: middle;
	font-size: 1.5em;
}
.round {
	border-radius: 5000upx;
}
.cu-avatar.lg {
	width: 96upx;
	height: 96upx;
	font-size: 2em;
}

/* ===========colorUI引用结束================== */


	.highLikeNav{
		width: 680upx;
		display: flex;
		flex-direction: row;
		padding: 0 30upx;
		justify-content: space-between;
	}
	/* 高赞榜 */
	.highLike{
		font:normal bold 50upx "微软雅黑",arial,sans-serif;
		color: #448088;
	}
	
	/* ============================切换按钮相关css开始====================================== */
	/* 切换按钮 */
	.switchButton{
		border-radius: 15upx;
		border: #448088 solid 1upx;
		display:inline-block;
		width: 250upx;
		height: 80upx;
		background-color: #ffffff;
		line-height: 80upx;
	}
	/* 切换按钮切换后的颜色 */
	.whiteBgc{
		background-color: rgb(247,251,251);
	}
	/* ============================切换按钮相关css结束====================================== */
	
	
	
	/* ==================榜单元素css开始====================== */
		.highLikeElement{
			padding: 10upx;
			height: 200upx;
			width: 750upx;
			/* background-color: #0066CC; */
			display: flex;
		}
		.highLikeAvatar{
			
			height: 100%;
			flex: 2;
			/* background-color: #39B54A; */
			padding : 30upx 0 30upx 30upx;
		}
		.highLikeTitle{
			padding-top: 20upx;
			padding-left: 20upx;
			flex: 6;
			display: flex;
			flex-direction: column;
		}
		.highLikeID{
			flex: 1;
		}
		.highLikeIDText{
			font:normal bold 40upx "微软雅黑",arial,sans-serif;
			color: #448088;
		}
		.highLikeContent{
			flex: 3;
		}
		.highLikeContentText{
			font:normal bold 30upx "宋体",arial,sans-serif;
			color: #448088;
		}
		.highLikeTime_Like{
			flex: 2;
			display: flex;
			flex-direction: column;
			justify-content: space-between;
		}
	
		.imag{
			margin: 0upx auto;
			width: 90%;
		}
		.highLikeTitleText{
			margin: 20upx 0 30upx 0;
			font:normal bold 40upx "微软雅黑",arial,sans-serif;
			color: #000000;
		}
		.highLikeTimeText{
			font:normal normal 30upx "宋体",arial,sans-serif;
			color: #448088;
		}
	/* ==================榜单元素css结束====================== */
	.highLikeTime_Like2{
		position: relative;
	}
	/* 星星 */
	.talkStar{
		width: 50upx;
		height: 50upx;
		position:absolute;     
		right: 160upx;
		bottom: 10upx;
	}
	.likeCount{
		position:absolute;     
		right: 70upx;
		bottom: 20upx;
		font:normal bold 30upx "微软雅黑",arial,sans-serif;
		color: #448088;
	}
</style>
