<template>
	<view>
		<view class="top_view">
			<view class="getSpace3"></view>
			<view class="popcNav">
				<view class="popcNav1"><img @tap="isBack" src="/static/back.svg" class="svg_back"  /></view>
				<view class="popcNav2">
					<button @tap="switchButton1" class="switchButton" :class="whiteBgcControl==1?'whiteBgc':''"><text style="color: #448088;">个人装</text></button>
					<button @tap="switchButton2" class="switchButton" :class="whiteBgcControl==2?'whiteBgc':''"><text style="color: #448088;">分享装</text></button>
					 
				</view>
				<view class="popcNav3"><img @tap="isBack" src="/static/plus.svg" class="svg_back"  /></view>
			</view>
		</view>
		<view class="randomTalk">
			<image src="../../../../static/record/edit.svg" class="talkEdit"></image>
			<image src="../../../../static/community/happyPopcorn/star.svg" class="talkStar"></image>
			<view class="talkSentenceView"><text class="talkSentence" @tap="restrictLength">{{randomTalkPiece}}</text></view>
		</view>
		
		
		<view class="popcMachine" >
			<image @tap="popMachine" src="../../../../static/community/happyPopcorn/popcorn.png" style="width: 450upx;height: 520upx;">
				
			</image>
		</view>
		
		<navigator url="highLikeBoard" class="popcBottomBar">
			<text>点击查看高赞榜(๑•̀ㅂ•́)و✧</text>
		</navigator>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				whiteBgcControl:2,

				randomTalkPiece:''
			}
		},
		onLoad() {
			uni.request({
				url:this.$url+'/highLikeBoard',
				method:"GET",
				data:{
					whiteBgcControl:3,
					user_id: this.$store.state.token_user_id
				},
				success: (res) => {
					console.log(res.data)
					// this.happything_str = res.data.result;
					var num = Math.floor(Math.random()*res.data.result.length);
					this.randomTalkPiece = res.data.result[num].content;
				}
			})
		},
		methods: {
			popMachine(){
				uni.request({
					url:this.$url+'/highLikeBoard',
					method:"GET",
					data:{
						whiteBgcControl:3,
						user_id: this.$store.state.token_user_id
					},
					success: (res) => {
						console.log(res.data)
						// this.happything_str = res.data.result;
						var num = Math.floor(Math.random()*res.data.result.length);
						this.randomTalkPiece = res.data.result[num].content;
					}
				})
			},
			switchButton1(){
				this.whiteBgcControl = 1;
			},
			switchButton2(){
				this.whiteBgcControl = 2;
			},
			isBack(){
				
				uni.navigateBack({
					delta: 1
				});
			} , 
		}
	}
</script>

<style>
	.popcNav{
		width: 680upx;
		display: flex;
		flex-direction: row;
		padding: 0 30upx;
		justify-content: space-between;
	}
	.popcNav2{
		padding-bottom: 30upx;
	}
	.switchButton{
		border-radius: 15upx;
		/* border: dashed rgb(238,241,234) ; */
		/* margin-bottom: 100upx; */
		display:inline-block;
		width: 200upx;
		height: 80upx;
		background-color: rgb(235,241,242);
	}
	.getSpace3{
		height: 100upx;
		text-align:center;
	}
	.whiteBgc{
		background-color: #ffffff;
	}
	.popcBottomBar{
		width: 750upx;
		height: 100upx;
		background-color: rgb(245,249,250);
		position: fixed;
		bottom: 0;
		text-align: center;
		line-height: 100upx;
		color: #448088;
	}
	.popcMachine{
		/* display: flex; */
		/* padding-left: 60upx; */
		position: fixed;
		bottom: 100upx;
		width: 750upx;
		text-align: center;
		/* justify-content: space-between; */
	}
	/* .popcMachineImage{
		flex: 1;
	} */
	.randomTalk{
		margin: 50upx auto;
		width: 600upx;
		height: 350upx;
		background-color: rgb(253,255,232);
		box-shadow:-15px -15px 10px rgb(254,255,242) ;
		position:relative;  
		   
		/* 让文字自动换行 */
		word-wrap:break-word;
		word-break:break-all; 
		
	}
	.talkStar{
		
		width: 60upx;
		height: 60upx;
		position:absolute;     
		right: 10upx;
		bottom: 10upx;
	}
	.talkEdit{
		width: 60upx;
		height: 60upx;
		position:absolute;   
		right: 10upx;
		top: 10upx;
	}
	.talkSentenceView{
		text-align: center;
		padding-top: 80upx;
		margin: 0upx 60upx;

		
/* 		max-width: 480px;
		word-wrap: break-word; */
		
	/* 	width:fit-content;
		width:-webkit-fit-content;
		width:-moz-fit-content; */
		
		
		/* display:inline-block !important; */
	}
	.talkSentence{
		font:normal bold 40upx "宋体",arial,sans-serif;
		color: #448088;
	}
</style>
