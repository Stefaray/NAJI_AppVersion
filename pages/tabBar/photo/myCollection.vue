<template>
	<view>
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="dayR_nav">
				<view class="dayR_back"><img @tap="isBack" src="/static/back.svg" class="svg_back"  /></view>
				<view class="dayR_title"><text class="shareExp">我的收藏品</text></view>
			</view>
		</view>
		<view>
			
			<view class="card" v-for="item in cards" :key="item">
				<image :src="item" style="width: 100%;height: 100%;"></image>
			</view>
			
		</view>
	</view>
</template>

<script>
	export default {
		onLoad() {
			uni.request({
				url:this.$url+'/photoCard',
				method:"GET",
				data:{
					user_id: this.$store.state.token_user_id
				},
				success:(res)=>{
					console.log(res.data.result)
					
					for(var i=0; i<res.data.result.length; i++){
						var tmp = this.$photoUrl + this.$store.state.token_user_id + "/" + res.data.result[i].photo_id;
						this.cards.push(tmp);
					}
					console.log(this.cards)
				},
				
				
			})
		},
		data() {
			return {
				cards:[]
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
	.card{
		width: 200upx;
		height: 300upx;
		margin: 60upx 40upx 30upx 60upx;
		border: #000000 3upx solid;
		
		background-color: rgb(241,250,254);
		display: inline-block;
	}
</style>
