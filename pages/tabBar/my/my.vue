<template>
	<view>
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="my_nav">
				<view class="my_title" style="align-items: center;text-align: center;"><text class="myText">个人中心</text></view>
			</view>
		</view>
		
		<view class="myProfile">
			<view class="myProfileAvatar">
				<view class="avatar" @tap="chooseAvatar">
					<view class="cu-avatar round lg" :style="{backgroundImage: 'url('+imageURL+')'}"></view>
				</view>
			</view>
			<view class="myProfileWord">
				<view class="Username">
					<text class="myWord">{{Username}}</text>
					<img src="/static/record/edit.svg" class="svgEdit" @tap="showModal" data-target="1" />
				</view>
				<view class="Level"><text class="myWord">Lv 5</text></view>
			</view>
			<view class="rightRow"><text class="rightRowWord"> > </text></view>
		</view>
		<view class="cutLine"></view>
		
		<view class="mySpace">
			<view ><text class="myWord">我的空间</text></view>
			<view class="rightRow2"><text class="rightRowWord"> > </text></view>
		</view>
		<view class="cutLine"></view>
		
		<view class="myMessage">
			<view ><text class="myWord">我的消息</text></view>
			<view class="rightRow2"><text class="rightRowWord"> > </text></view>
		</view>
		<view class="cutLine"></view>
		
		<view class="myPrivacy">
			<view ><text class="myWord">隐私</text></view>
			<view class="rightRow2"><text class="rightRowWord"> > </text></view>
		</view>
		<view class="cutLine"></view>
		
		<view class="myCustomize">
			<view ><text class="myWord">自定义</text></view>
			<view class="rightRow2"><text class="rightRowWord"> > </text></view>
		</view>
		<view class="cutLine"></view>
		
		<view class="myStore">
			<view ><text class="myWord">纳己小卖部</text></view>
			<view class="rightRow2"><text class="rightRowWord"> > </text></view>
		</view>
		<view class="cutLine"></view>
		
		<view class="myBackup">
			<view class="Username"><text class="myWord">备份</text></view>
			<view class="rightRow2"><text class="rightRowWord"> > </text></view>
		</view>
		<view class="cutLine"></view>
		
		<view class="myHelp">
			<view class="Username"><text class="myWord">帮助与反馈</text></view>
			<view class="rightRow2"><text class="rightRowWord"> > </text></view>
		</view>
		<view class="cutLine"></view>
		
		<!-- 弹出框内容开始 -->
		<view class="cu-modal" :class="modalName==1?'show':''">
			<view class="cu-dialog">
				
				<view class="cu-bar bg-white justify-end">
					<view class="actionLeft" @tap="noModal" >
						<text class="cuIcon-close text-theme"></text>
					</view>	
					<view class="content"><text class="text-theme" style="font:normal bold 32upx '宋体',arial,sans-serif;">编辑您的用户名～</text></view>
					<view class="action" @tap="yesModal">
						<text class="cuIcon-check text-theme"></text>
					</view>
				</view>
				<view class="padding-xl">
					<textarea auto-height maxlength="11" :value="notedata1" style="font:normal bold 34upx '宋体' ;" @blur="bindTextAreaBlur"></textarea>
					<!-- <input type="idcard" style="font:normal bold 34upx '宋体' ;" /> -->
				</view>
			</view>
		</view>
		<!-- 弹出框内容结束 -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				imageURL: '',
				Username:'',
				modalName: 0,
				notedata1:''
			}
		},
		onLoad() {
			uni.request({
				url:this.$url+'/myPage',
				method:"GET",
				data:{
					user_id: this.$store.state.token_user_id
				},
				success: (res) => {
					
					var getTimestamp = new  Date().getTime();
					console.log(getTimestamp)
					console.log(res.data)
					this.imageURL = this.$photoUrl + this.$store.state.token_user_id + "/" + res.data.result.avatar + "?timestamp=" + getTimestamp
					this.Username = res.data.result.username
					
				}
			})
		},
		methods: {
			bindTextAreaBlur: function (e) {
				if(e.detail.value != '')
					this.Username = e.detail.value;
				
				console.log(this.Username)
				
			},
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target;
				console.log(this.modalName)
			},
			yesModal(e) {
				this.modalName = 0,
				uni.request({
					url:this.$url+'/changeUsername',
					method:"GET",
					data:{
						username: this.Username,
						user_id: this.$store.state.token_user_id
					},
					success: (res) => {
						console.log(res.data)
						this.Username = res.data.result.username
					}
				})
			},
			noModal(e) {
				this.modalName = 0
				this.notedata1 = ''
			},
			chooseAvatar: function() {
				var getTimestamp = new  Date().getTime();
				uni.chooseImage({
					count: 1,
					sizeType: ['compressed'],
					sourceType: ['album'],
					name:'photo',
					method:"POST",
					success: (res) => {
						console.log(res)
						console.log('chooseImage success, temp path is', res.tempFilePaths[0])
						var imageSrc = res.tempFilePaths[0]
						uni.uploadFile({
							url:this.$url+'/up_avatar',
							method:"POST",
							filePath: imageSrc,
							fileType: 'image',
							name: 'file',
							formData:{
								user_id: this.$store.state.token_user_id

							},
							success: (res) => {
								var getTimestamp = new  Date().getTime();
								// console.log('uploadImage success, res is:', res.data)
								var data = JSON.parse(res.data);
								console.log(data)
								this.imageURL = this.$photoUrl + this.$store.state.token_user_id + "/" + data.result.avatar + "?timestamp=" + getTimestamp
								console.log(this.imageURL)
							},
							fail: (err) => {
								console.log('uploadImage fail', err);
								uni.showModal({
									content: err.errMsg,
									showCancel: false
								});
							}
						});
					},
					fail: (err) => {
						console.log('chooseImage fail', err)
						// #ifdef MP
						uni.getSetting({
							success: (res) => {
								let authStatus = res.authSetting['scope.album'];
								if (!authStatus) {
									uni.showModal({
										title: '授权失败',
										content: 'Hello uni-app需要从您的相册获取图片，请在设置界面打开相关权限',
										success: (res) => {
											if (res.confirm) {
												uni.openSetting()
											}
										}
									})
								}
							}
						})
						// #endif
					}
				})
			}
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
	.svgEdit{
		width: 50upx;
		height: 50upx;
		margin: 0 0 0 20upx;
	}
	.myWord{
		font:normal bold 40upx "微软雅黑",arial,sans-serif;
		color: #448088;
	}
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
		width: 136upx;
		height: 136upx;
		font-size: 2em;
		border: #448088 solid 5upx;
		margin: 0 0 0 60upx;
	}
	
	/* ===========colorUI引用结束================== */
	.myText{
		font:normal bold 50upx "微软雅黑",arial,sans-serif;
		color: #448088;
	}
	.my_nav{
		display: flex;
		flex: row;
	}
	.my_title{
		flex: 1;
	}
	
	
	/* 我的个人简介 */
	.myProfile{
		margin-top: 50upx;
		width: 750upx;
		height: 172upx;
		display: flex;
		flex-direction: row;
		position: relative;
		/* justify-content: space-evenly;	 */
		/* background-color: #000000; */
	}
	.myProfileAvatar{
		flex: 1;
		
	}
	.myProfileWord{
		padding: 25upx 0 0 25upx;
		flex: 2;
	}
	.mySpace,.myMessage,.myBackup,.myCustomize,.myPrivacy,.myHelp,.myStore{
		width: 690upx;
		height: 113upx;
		/* background-color: #000000;	 */
		padding-left: 60upx;
		/* margin-left: 60upx; */
		line-height: 113upx;
		position: relative;
		/* background-color: #0066CC; */
	}
	.cutLine{
		width: 750upx;
		height: 6upx;
		background-color: rgb(241,250,254);
	}
	.rightRow{
		position: absolute;
		bottom: 60upx;
		right: 120upx;
	}
	.rightRow2{
		position: absolute;
		bottom: -10upx;
		right: 60upx;
	}
	.rightRowWord{
		font:normal bold 60upx "微软雅黑",arial,sans-serif;
		color: #448088;
	}
</style>
