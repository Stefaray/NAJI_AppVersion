<template>
	<view class="whole">
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="dayR_nav">
				<view  class="dayR_title1" style="align-items: center;text-align: center;"><text class="shareExp">揭晓快乐</text></view>
			</view>
		</view>
		
		<!-- <page-head :title="title"></page-head> -->
		<view class="uni-padding-wrap uni-common-mt" v-show="!hasPhoto">
			<view class="demo">
				<block v-if="imageSrc">
					<image :src="imageSrc" class="image" mode="widthFix"></image>
				</block>
				<block v-else>
					<view class="uni-hello-addfile" @click="chooseImage"><text class="Text">+ 选择图片</text></view>
				</block>
			</view>
		</view>
		
		<view class="uni-padding-wrap uni-common-mt total" v-show="hasPhoto">
			<image class="piece" :src='piecestr[0]' :class="[piece1==0?'opacity':'nonOpacity'] "></image>
			<image class="piece" :src='piecestr[1]' :class="[piece2==0?'opacity':'nonOpacity'] "></image>
			<image class="piece" :src='piecestr[2]' :class="[piece3==0?'opacity':'nonOpacity'] "></image>
			<image class="piece" :src='piecestr[3]' :class="[piece4==0?'opacity':'nonOpacity'] "></image>
			<image class="piece" :src='piecestr[4]' :class="[piece5==0?'opacity':'nonOpacity'] "></image>
			<image class="piece" :src='piecestr[5]' :class="[piece6==0?'opacity':'nonOpacity'] "></image>
			<image class="piece" :src='piecestr[6]' :class="[piece7==0?'opacity':'nonOpacity'] "></image>
			<image class="piece" :src='piecestr[7]' :class="[piece8==0?'opacity':'nonOpacity'] "></image>
			<image class="piece" :src='piecestr[8]' :class="[piece9==0?'opacity':'nonOpacity'] "></image>
		</view>
		
		
		
		<image @tap="myCollection" class="photoBox" src="../../../static/photo/box.svg"></image>
		<image @tap="light" class="photoBar" src="../../../static/photo/bar.svg"></image>
		<view :class="reUpload==0?'':'reUploadButton'" @click="chooseImage"><text class="content_text">重新上传</text></view>
	</view>
</template>

<script>
	export default {
		
		data() {
			return {
				title: 'uploadFile',
				imageSrc: '',
				hasPhoto:0,
				piecestr:[],
				isOpacity:[],
				tmpstr:[],
				last_light_date:'',
				photo_id:'',
				piece1:0,
				piece2:0,
				piece3:0,
				piece4:0,
				piece5:0,
				piece6:0,
				piece7:0,
				piece8:0,
				piece9:0,
				reUpload:0
			}
		},
		onUnload() {
			this.imageSrc = '';
		},
		onLoad(){
			uni.request({
				url:this.$url+'/photoInitial',
				data:{
					 user_id: this.$store.state.token_user_id
				},
				method:"GET",
				success:(res)=>{
					var getTimestamp = new  Date().getTime();
					if(res.data.success == 1){
						this.hasPhoto = 1;
						for(var i=1; i<=9; i++){
							this.piecestr.push(this.$photoUrl + this.$store.state.token_user_id + "/" + i + ".png" + "?timestamp=" + getTimestamp)
						}
						
						this.isOpacity[0] = res.data.result[0].piece1 == null ? 0 : 1	
						this.isOpacity[1] = res.data.result[0].piece2 == null ? 0 : 1
						this.isOpacity[2] = res.data.result[0].piece3 == null ? 0 : 1
						this.isOpacity[3] = res.data.result[0].piece4 == null ? 0 : 1
						this.isOpacity[4] = res.data.result[0].piece5 == null ? 0 : 1
						this.isOpacity[5] = res.data.result[0].piece6 == null ? 0 : 1
						this.isOpacity[6] = res.data.result[0].piece7 == null ? 0 : 1
						this.isOpacity[7] = res.data.result[0].piece8 == null ? 0 : 1
						this.isOpacity[8] = res.data.result[0].piece9 == null ? 0 : 1
						this.photo_id = res.data.result[0].photo_id
						this.last_light_date = res.data.result[0].last_light_date
						if(this.isOpacity[0] == 1)
							this.piece1 = 1
						if(this.isOpacity[1] == 1)
							this.piece2 = 1
						if(this.isOpacity[2] == 1)
							this.piece3 = 1
						if(this.isOpacity[3] == 1)
							this.piece4 = 1
						if(this.isOpacity[4] == 1)
							this.piece5 = 1
						if(this.isOpacity[5] == 1)
							this.piece6 = 1
						if(this.isOpacity[6] == 1)
							this.piece7 = 1
						if(this.isOpacity[7] == 1)
							this.piece8 = 1
						if(this.isOpacity[8] == 1)
							this.piece9 = 1
						// console.log(this.isOpacity)
						
					}
					else{
						this.hasPhoto = 0
					}
					console.log(res.data)
					
				}
			})
			
			
		},
		methods: {
			myCollection(){
				
				uni.navigateTo({
					url:"myCollection"
				})
			},
			light(){
				var today = new Date();//获得当前日期
				var year = today.getFullYear();//获得年份
				var month = today.getMonth() + 1 ;//此方法获得的月份是从0---11，所以要加1才是当前月份
				month = month + ""
				
				if(month.length == 1)
					month = "0" + month
				var day = today.getDate();//获得当前日期
				day = day + ""
				if(day.length == 1)
					day = "0" + day
				var date = year+"-"+month+"-"+day;
				
				if(this.last_light_date == date){
					uni.showToast({
						title: '今日已点亮',
						icon: 'none',
						duration: 1000
					})
				}
				else{
					this.tmpstr=[];
					for(var i=0; i<9; i++){
						if(this.isOpacity[i] == 0)
							this.tmpstr.push(i+1)
					}
					
					if(this.tmpstr.length == 0 && this.hasPhoto == 1){ 
						uni.showToast({
							title: '碎片已集结完毕~',
							icon: 'none',
							duration: 1000
						})
						this.reUpload = 1;
					}
					else if(this.tmpstr.length == 0 && this.hasPhoto == 0){ 
						uni.showToast({
							title: '请上传照片',
							icon: 'none',
							duration: 1000
						})
					}
					else{
						// console.log(1)
						var cc = Math.floor(Math.random() * this.tmpstr.length) 
						if(this.tmpstr[cc] == 1)
							this.piece1 = 1
						else if(this.tmpstr[cc] == 2)
							this.piece2 = 2
						else if(this.tmpstr[cc] == 3)
							this.piece3 = 3
						else if(this.tmpstr[cc] == 4)
							this.piece4 = 4
						else if(this.tmpstr[cc] == 5)
							this.piece5 = 5
						else if(this.tmpstr[cc] == 6)
							this.piece6 = 6
						else if(this.tmpstr[cc] == 7)
							this.piece7 = 7
						else if(this.tmpstr[cc] == 8)
							this.piece8 = 8
						else if(this.tmpstr[cc] == 9)
							this.piece9 = 9
						
						// console.log(this.isOpacity);
						
						uni.request({
							url:this.$url+'/lightPiece',
							data:{
								piece: this.tmpstr[cc],
								photo_id: this.photo_id
							},
							method:"GET",
							success:(res)=>{
								// console.log(res.data)
								this.last_light_date = res.data.last_light_date
								console.log(this.last_light_date)
								console.log(date)
							}
						})
						
							
						
						
					}
					// while( isOpacity[Math.floor(Math.random()*9)] != 0 )
				}
				
			},
			chooseImage: function() {
				this.reUpload = 0;
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
							
							url:this.$url+'/up_photo',
							method:"POST",
							filePath: imageSrc,
							fileType: 'image',
							name: 'file',
							formData:{
								 user_id: this.$store.state.token_user_id
							},
							success: (res) => {
								console.log('uploadImage success, res is:', res.data)
								var data = JSON.parse(res.data);
								console.log(data)
								if(data.success == 0){
									console.log(res.data.addr)
									uni.showToast({
										title: '上传成功',
										icon: 'success',
										duration: 1000
									}),
									this.hasPhoto = 1 
									this.imageSrc = imageSrc
									console.log(data.addr)
									for(var i=1; i<=9; i++){
										this.piecestr.push(this.$photoUrl + this.$store.state.token_user_id + "/" + i + ".png")
									}
									console.log(this.piecestr)
									data.photo_message.piece1 == null ? (this.isOpacity[0] = 0 ) : (this.isOpacity[0] = 1 )
									data.photo_message.piece2 == null ? (this.isOpacity[1] = 0 ) : (this.isOpacity[1] = 1 )
									data.photo_message.piece3 == null ? (this.isOpacity[2] = 0 ) : (this.isOpacity[2] = 1 )
									data.photo_message.piece4 == null ? (this.isOpacity[3] = 0 ) : (this.isOpacity[3] = 1 )
									data.photo_message.piece5 == null ? (this.isOpacity[4] = 0 ) : (this.isOpacity[4] = 1 )
									data.photo_message.piece6 == null ? (this.isOpacity[5] = 0 ) : (this.isOpacity[5] = 1 )
									data.photo_message.piece7 == null ? (this.isOpacity[6] = 0 ) : (this.isOpacity[6] = 1 )
									data.photo_message.piece8 == null ? (this.isOpacity[7] = 0 ) : (this.isOpacity[7] = 1 )
									data.photo_message.piece9 == null ? (this.isOpacity[8] = 0 ) : (this.isOpacity[8] = 1 )
									// console.log(this.isOpacity[0]+"yyyyyyyyyyyyyyyyyyy" + data.photo_message.piece1)
									// console.log(data.photo_message.last_light_date)
									this.photo_id = data.photo_message.photo_id
									this.last_light_date = data.photo_message.last_light_date 
									// console.log(this.last_light_date)
								}
								
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
	.reUploadButton{
		width: 140upx;
		height: 60upx;
		border: 3upx #448088 solid;
		border-radius: 10upx;
		position: absolute;
		bottom: 0upx;
		left: 520upx;
	}
	.nonOpacity{
		opacity:1
	}
	.opacity{			
		opacity:0.1
	}
	.total{
		width: 750upx;
		height: 1000upx;
		/* background-color: #1CBBB4; */
		padding-top: 100upx;
	}
	.piece{
		width: 230upx;
		height: 230upx;
		background-color: #0066CC;
		display: inline-block;
		margin: 10upx 10upx;
	}
	.Text{
		font:normal bold 34upx "宋体",arial,sans-serif;
		color: #448088;
	}
	.whole{
		position: relative;
		width: 750upx;
		height: 1200upx;
		/* text-align: center; */
	}
	.photoBar{
		position: absolute;
		width: 80upx;
		height: 80upx;
		bottom: 0upx;
		left: 420upx;
	}
	.photoBox{
		position: absolute;
		width: 80upx;
		height: 80upx;
		bottom: 0upx;
		left: 50upx;
	}
	.dayR_title1{
		/* margin-left: 100upx; */
		flex: 3;
	}	
	.shareExp{
		font:normal bold 50upx "微软雅黑",arial,sans-serif;
		color: #448088;
	}
	.image {
		width: 100%;
	}
	
	.demo {
		margin: 100upx auto;
		width: 600upx;
		height: auto;
		background: #dddddd;
		padding: 30upx;
		border: dashed #448088 5upx;
		line-height: 400upx;
		text-align: center;
	}
	.content_text{
		font:normal normal 34upx "宋体",arial,sans-serif;
		color: #448088;
	}
	
</style>
