<template>
	<view class="zai-box">
		<view style="height: 100upx;width: 1upx;"></view>
		<image src="../../static/zaizai-login/login.png" mode='aspectFit' class="zai-logo"></image>
		
		<view class="zai-form">
			<input v-model="account" class="zai-input" placeholder-class placeholder="手机号码"  />
			<input v-model="password" class="zai-input" placeholder-class password placeholder="请输入密码"/>
			<view class="total-lebal">
				<view class="zai-label1">忘记密码</view>
				<navigator url="../register_sms/index" hover-class="none" class="zai-label2">点击注册</navigator>
			</view>
			<button class="zai-btn" @tap="login">立即登录</button>	
			<view class="divideLine flex flex-direction align-center justify-center">
				<view class="line"></view>
				<text style="color:gray;font-size: small;">其他登录方式</text>
				<view class="line"></view>
			</view>
			
			
			<view class="other_login">
				<view style="width: 1upx;"></view>
				<navigator url="../login_sms/index">
					<image class="phone_icon" src="../../static/zaizai-login/login.png"></image>
					<view style="margin-top: 10upx;font-size: small;color: gray;">验证码登录</view>
				</navigator>
				<view style="width: 1upx;"></view>
			</view>
			
			
		</view>
	</view>
</template>

<script>
	var account;
	var password;
	export default {
		data() {
			return {
				account,
				password
			}
		},
		methods: {
			// changestatus(){
			// 	this.status = 
			// }
			login(e){
				// console.log(e.data)
				// ---------------------------------
				uni.request({
					url:this.$url+'/user/login',
					data:{
						account:this.account,
						password:this.password
					},
					method:"GET",
					success:(res) => {
						// console.log(res.data.user_id);
						uni.showToast({
							icon:"none",
							title:res.data.desc
						})
						// console.log(res.data)
						if(res.data.status==0){
							uni.setStorageSync("token_user_id",res.data.user_id);
							// this.$store.commit("ChangeToken",res.data.uid);
							uni.switchTab({
								url: "../tabBar/record/record"
							});
						}
						else{
							
						}
					}
				})
				// -------------------------------------
			}
		},
	}
</script>

<style>
	.other_login{
		margin: 10upx;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		
	}
	.phone_icon{
		
		width: 100upx;
		height: 100upx;
	}
	.divideLine{
		display: flex;
		justify-content: space-between;
		align-content: center;	
		margin-top: 50upx;
		margin-bottom: 50upx;
	}
	.line{
		
		height: 0upx;
		background-color: #DDDDDD;
		flex-grow: 1;
	}
	.total-lebal{
		display: flex;
		justify-content: space-between;
	}
	.zai-box{
		padding: 0 100upx;
		position: relative;
	}
	.zai-logo{
		width: 100%;
		width: 100%;
		height: 310upx;
	}
	.zai-title{
		position: absolute;
		top: 0;
		line-height: 360upx;
		font-size: 68upx;
		color: #fff;
		text-align: center;
		width: 100%;
		margin-left: -100upx;
	}
	.zai-form{
		margin-top: 100upx;
	}
	.zai-input{
		background: #e2f5fc;
		margin-top: 30upx;
		border-radius: 100upx;
		padding: 20upx 40upx;
		font-size: 36upx;
	}
	.input-placeholder, .zai-input{
		color: #94afce;
	}
	.zai-label1{
		padding: 60upx 0;
		text-align: center;
		color: #a7b6d0;
		font-size: 30upx;
	}
	.zai-label2{
		padding: 60upx 0;
		text-align: right;
		color: #a7b6d0;
		font-size: 30upx;
	}
	.zai-btn{
		background: #ff65a3;
		color: #fff;
		border: 0;
		border-radius: 100upx;
		font-size: 36upx;
	}
	.zai-btn:after{
		border: 0;
	}
	/*按钮点击效果*/
	.zai-btn.button-hover{
		transform: translate(1upx, 1upx);
	}
</style>
