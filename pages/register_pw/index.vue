<!-- 双重密码注册页面 -->
<template>
	<view class="zai-box">
		<view style="height: 100upx;width: 1upx;"></view>
		<image src="../../static/zaizai-login/register.png" mode='aspectFit' class="zai-logo"></image>
		
		<view class="zai-form">
			<input v-model="phone_number" class="zai-input" placeholder-class placeholder="请输入手机号码" />
			<input v-model="password1" class="zai-input" placeholder-class password placeholder="请输入密码"/>
			<input v-model="password2" class="zai-input" placeholder-class password placeholder="请再输入一次密码"/>
			<button @tap="register" class="zai-btn">立即注册</button>
			<navigator url="../zaizai-login/index" open-type='navigateBack' hover-class="none" class="zai-label">已有账号，点此去登录.</navigator>
		</view>
	</view>
</template>

<script>
	var phone_number="";
	var password1="";
	var password2="";
	export default {
		data() {
			return {
				phone_number,
				password1,
				password2
			}
		},
		methods: {
			// changestatus(){
			// 	this.status = 
			// }
			register(){
				if(this.phone_number.length != 11){
					uni.showToast({
					    title: '请输入正确的手机号',
					    duration: 1000,
						icon:"none"
					});
				}
				else if(this.password1!=this.password2){
					uni.showToast({
					    title: '两次密码不一致，请重新输入',
					    duration: 1000,
						icon:"none"
					});
				}
				else if(this.password1.length < 6){
					uni.showToast({
					    title: '密码长度不能小于6位数',
					    duration: 1000,
						icon:"none"
					});
				}
				else{
					uni.request({
						url:this.$url+'/user/register_pw',
						data:{
							phone_number:this.phone_number,
							password:this.password1
						},
						method:"GET",
						success:(res) => {
							console.log(res.data.user_id);
							uni.showToast({
									icon:"none",
									title:res.data.desc
							})
							if(res.data.status == "0"){
								uni.switchTab({
									url: "../tabBar/record/record"
								});
							}
							
						}
					})
				}
		
				
			}
		},
	}
</script>

<style>
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
	.zai-label{
		padding: 60upx 0;
		text-align: center;
		font-size: 30upx;
		color: #a7b6d0;
	}
	.zai-btn{
		background: #ff65a3;
		color: #fff;
		border: 0;
		border-radius: 100upx;
		font-size: 36upx;
		margin-top: 60upx;
	}
	.zai-btn:after{
		border: 0;
	}
	/*按钮点击效果*/
	.zai-btn.button-hover{
		transform: translate(1upx, 1upx);
	}
</style>
