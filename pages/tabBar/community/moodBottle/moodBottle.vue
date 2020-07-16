<template>
	<view>
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="commNav">
				<view class="commNav1"><img @tap="isBack" src="/static/back.svg" class="svg_back"  /></view>
				<view class="commNav2"><text class="shareExp">情绪漂流瓶</text></view>
				<view class="commNav3"><img @tap="edit" src="/static/community/moodBottle/edit.svg" class="svg_back"  /></view>
			</view>
		</view>
		
		<view v-if="isEdit==1">
			<view class="paper">
				
				<textarea :value="initText" class="editArea" maxlength="-1" placeholder="想说点什么呢" @blur="bindTextAreaBlur"></textarea>
				
				<view class="commNav1"><img @tap="submit" src="/static/community/moodBottle/submit.svg" class="submitButton"  /></view>
				<picker @change="bindPickerChange" :value="index" :range="array" class="chooseTitle">
					<view class="uni-input">{{array[index]}}</view>
				</picker>
			</view>
		</view>
		<view v-else-if="isEdit==0">
			
			<textarea class="othersStory" maxlength="-1" :value="moodBottleText2"></textarea>
			<image src="../../../../static/community/moodBottle/1.png" class="paper"></image>
			
		</view>
		
		<view class="commBottom">
			<view style="width: 100%;height: 60upx;text-align: center;line-height:60upx ;"><text class="listen">听听别人的故事～</text></view>
			<view class="bottom">
				<view class="bottom1" @tap="positive"><image src="../../../../static/community/moodBottle/2.png" style="width: 100upx;height: 240upx;"></image></view>
				<view class="bottom2" @tap="random"><image src="../../../../static/community/moodBottle/3.png" style="width: 100upx;height: 240upx;"></image></view>
				<view class="bottom3" @tap="nagetive"><image src="../../../../static/community/moodBottle/4.png" style="width: 100upx;height: 240upx;"></image></view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				isEdit:1,
				title: 'picker',
				array: ['积极', '随机', '消极'],
				index: 0,
				moodBottleText:"",
				moodBottleText2:"",
				time: '12:01',
				initText:""
			}
		},
		methods: {
			edit(){
				this.isEdit = 1
			},
			positive(){
				this.isEdit = 0,
				uni.request({
					url:this.$url+'/moodBottlePositive',
					data:{
						category: 0,
					},
					method:"GET",
					success:(res)=>{
						console.log(res.data),
						this.moodBottleText2 = res.data.result.moodBottleText
					}
				})
			},
			random(){
				this.isEdit = 0,
				uni.request({
					url:this.$url+'/moodBottleRandom',
					data:{
						category: 1,
					},
					method:"GET",
					success:(res)=>{
						console.log(res.data),
						this.moodBottleText2 = res.data.result.moodBottleText
					}
				})
			},
			nagetive(){
				this.isEdit = 0,
				uni.request({
					url:this.$url+'/moodBottleNagetive',
					data:{
						category: 2,
					},
					method:"GET",
					success:(res)=>{
						console.log(res.data),
						this.moodBottleText2 = res.data.result.moodBottleText
					}
				})
			},
			
			bindTextAreaBlur: function (e){
			
				this.moodBottleText = e.detail.value
				
			},
			
			isBack(){
				uni.navigateBack({
					delta: 1
				});
			} , 
			submit(){
				if(this.moodBottleText == "" || this.moodBottleText == " "){
					uni.showToast({
						title: '输入不能为空',
						icon: "none", 
						duration: 1000
					})
				}
				else{
					uni.request({
						url:this.$url+'/moodBottle',
						data:{
							category: this.index,
							moodBottleText: this.moodBottleText,
							user_id: this.$store.state.token_user_id
						},
						method:"GET",
						success:(res)=>{
							console.log(res.data),
							this.initText = " ",
							this.index = 0
						}
					}),
					uni.showToast({
						title: '提交成功',
						icon: 'success',
						duration: 1000
					})
				}
				
			},
			bindPickerChange: function(e) {
				// console.log('picker发送选择改变，携带值为', e.target.value)
				this.index = e.target.value	
			},
		}
	}
</script>

<style>
	.othersStory{
		/* background-color: #007AFF; */
		width: 370upx;
		height: 400upx;
		position: absolute;
		left: 200upx;
		bottom: 550upx;
		z-index:1;
		font: normal 34upx "宋体",arial,sans-serif;
		color: #448088;
	}
	.commNav{
		width: 680upx;
		display: flex;
		flex-direction: row;
		padding: 0 30upx;
		justify-content: space-between;
	}
	.paper{
		width: 600upx;
		height: 720upx;
		padding: 80upx 40upx 0upx 100upx;
		margin: 0 auto 30upx;
		position: relative;
		
	}

	/* 编辑板块 */
	.editArea{
		background-color: rgb(241,250,254);
		width: 500upx;
		height: 500upx;
		padding: 50upx 50upx 100upx 50upx;
		
		
	}
	.submitButton{
		position: absolute;
		bottom: 100upx;
		right: 120upx;
		width: 60upx;
		height: 60upx;
	}
	.chooseTitle{
		position: absolute;
		bottom: 100upx;
		right: 460upx;

		/* background-color: #FFFFFF; */
		/* border-radius: 20upx; */
	}
	.shareExp{
		font:normal bold 50upx "微软雅黑",arial,sans-serif;
		color: #448088;
	}
	.listen{
		font:normal bold 38upx "宋体",arial,sans-serif;
		color: #448088;
	}
	.commBottom{
		width: 750upx;
		height: 157px;
		background-color: rgb(245,249,250)
	}
	.bottom{
		display: flex;
		flex-direction: row;
		justify-content: space-around;
	}
	.bottom1{
		
	}
</style>
