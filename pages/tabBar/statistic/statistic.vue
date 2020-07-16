<template>
	<view>
		<!-- 顶部栏开始 -->
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="dayR_nav">
				<view  class="dayR_title1" style="align-items: center;text-align: center;"><text class="shareExp">数据统计</text></view>
			</view>
		</view> 
		 <!-- 顶部栏结束 -->
		 <view class="zanshi">
		 <image src="../../../static/statistic/1.png" class="a1"></image>
		 <image src="../../../static/statistic/2.png" class="a2"></image>
		 <image src="../../../static/statistic/3.png" class="a3"></image>
		 <!-- <image src="../../../static/statistic/4.png" class="a4"></image> -->
		 
		 
		 </view>
		 
		 <!-- <button @tap="menuClick" :data-id="item.id" class="cu-btn round shadow">111</button> -->
		<!-- <view class="actTag">
		 	<view class="tagTitle">
		 		<text class="tagText">主题标签</text>
		 		<img src="/static/plus.svg" class="svg_plus" @tap="showModal" data-target="1"/>
		 		<button v-if="showActTag" class="cu-btn round shadow tagChange" >{{tagidText}}</button>
		 	</view>
		 		<view class="grid col-4 padding-sm" @change="radioChange">
		 				<view  class="margin-tb-sm text-center" @tap="menuClick">
		 					<button class="cu-btn round shadow">亲情</button>
		 				</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">爱情</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">友情</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">日常</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">时事</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">爱好</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">成就</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">财务</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">美食</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">旅行</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">创伤</button>
						</view>	
						<view  class="margin-tb-sm text-center">
							<button class="cu-btn round shadow">陌生人</button>
						</view>	
		 		</view>
		 		
		 		
		 </view> -->
		 <!-- <button class="cu-btn round shadow tagChange">其他</button> -->
		 <!-- <button class="cu-btn round shadow">6327</button> -->
		 
		 
		 
		 
	</view>
</template>

<script>
	var tabs = [];
	var showActTag=false;
	tabs = [
	      {
	        id: 0,
	        value: "亲情",
	        isActive: true
	      },
	      {
	        id: 1,
	        value: "爱情",
	        isActive: false
	      },
	      {
	        id: 2,
	        value: "友情",
	        isActive: false
	      },
		  {
		    id: 3,
		    value: "日常",
		    isActive: false
		  },
		  {
		    id: 4,
		    value: "时事",
		    isActive: false
		  },
		  {
		    id: 5,
		    value: "爱好",
		    isActive: false
		  },
		  {
		    id: 6,
		    value: "成就",
		    isActive: false
		  },
		  {
		    id: 7,
		    value: "财务",
		    isActive: false
		  },
		  {
		    id: 8,
		    value: "美食",
		    isActive: false
		  },
		  {
		    id: 9,
		    value: "旅行",
		    isActive: false
		  },
		  {
		    id: 10,
		    value: "创伤",
		    isActive: false
		  },
		  {
		    id: 11,
		    value: "陌生人",
		    isActive: false
		  }
	    ];
		
		
	export default {
		data() {
			return {
				tagidText,
				showActTag,
				tabs,
				showActTag,
			}
		},
		methods: {
			
			menuClick:function(e){
				alert(1)
				var tagid = e.currentTarget.dataset.id;
				this.tagidText = this.tabs[tagid].value;
				this.showActTag = true;
			},
		}
	}
</script>

<style>
	@import "/colorui/main.css";
	@import "/colorui/icon.css";
	.zanshi{
		align-items:center;
		text-align: center;
	}
	.a1{
		margin: 50upx;
		width: 90%;
	}
	.a2{
		margin: 50upx;
		width: 80%;
	}
	.a3{
		margin: 30upx;
		width: 85%;
	}
	.a4{
		width: 80%;
		
	}
	
	
	
	/* 主题标签 */
	.tagTitle{
		margin: 20upx 0 0upx 34upx;
	}
	.svg_plus{
		margin: 30upx 0 0 25upx;
		width: 50upx;
		height: 45upx;
		/* display: inline-block; */
	}
	.tagChange{
		background-color: #99D3C9 !important;
		color: #ffffff;
		margin-left: 125upx;
	}
</style>
