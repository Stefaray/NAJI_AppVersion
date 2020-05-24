<template>
    <view>
		<view class="whole">
			
			<!-- 顶部栏开始 -->
			<view class="top_view">
				<view class="getSpace1"></view>
				<uni-segmented-control :current="current" :values="items" @clickItem="onClickItem" style-type="button" active-color="#448088" class="uni_seg"></uni-segmented-control>
			</view> 
			 <!-- 顶部栏结束 -->
			
			
			<view v-show="current === 0">
			    
				<view class="content">
					<navigator class="enterRecord" url="dayRemind/dayRemind">
						<!-- <img src="/static/plus2.svg" class="svg_plus"  />
						<view>今天还没有记录哦</view>
						<text >今天还没有记录哦</text> -->
						<view class="plus_left">
							<img src="/static/plus2.svg" class="svg_plus2"  />
						</view>
						<view class="plus_right">
							<text class="plus_text">今天还没有记录哦</text>
						</view>
						
					</navigator>
					<view class="getSpace1"></view>
					<view class="dayCard">
						<view class="date">
							<text class="record_date">{{dayString}}</text>
						</view>
						<view class="moodValue">
						
							<view class="values">
								<view class="firstValue"><text class="record_values">压力值</text></view>
								<view class="secondValue"><text class="record_values">混乱值</text></view>
							</view>
							<view class="values">
								<view class="firstValue"><text class="record_values">活力值</text></view>
								<view class="secondValue"><text class="record_values">平静值</text></view>
							</view>
							
						</view>
					</view>
					<view class="dayCard"></view>
					<view class="dayCard"></view>
				  
				   
				</view>
				
			 </view>
			 <view v-show="current === 1">
			     
				 <view class="content">
				 	<navigator class="enterRecord" url="moodBoom/moodBoom">
				 		<!-- <uni-icon type="checkbox" size="30"></uni-icon> -->
						<view class="plus_left">
							<img src="/static/plus.svg" class="svg_plus"  />
						</view>
						<view class="plus_right">
							<text class="plus_text">想说点什么呢</text>
						</view>
				 		
				 	</navigator>
				 	<view class="getSpace1"></view>
				 	<view class="dayCard">
				 		<view class="date">
				 			<text class="record_date">{{dayString}}</text>
				 		</view>
				 		<view class="moodValue">
				 		
							<view class="values">
								<view class="firstValue"><text class="record_values">压力值</text></view>
								<view class="secondValue"><text class="record_values">混乱值</text></view>
							</view>
							<view class="values">
								<view class="firstValue"><text class="record_values">活力值</text></view>
								<view class="secondValue"><text class="record_values">平静值</text></view>
							</view>
				 			
				 		</view>
				 	</view>
				 	<view class="dayCard"></view>
				 	<view class="dayCard"></view>
				   
				    
				 </view>
				 
			 </view>
			
			
		</view>
       
    </view>
</template>
<script>
	import uniSegmentedControl from "@/components/uni-segmented-control/uni-segmented-control.vue";
	// import uniIcon from "@/components/uni-icons/icons.js";
	
	var today = new Date();//获得当前日期
	var year = today.getFullYear();//获得年份
	var month = today.getMonth() + 1;//此方法获得的月份是从0---11，所以要加1才是当前月份
	var day = today.getDate();//获得当前日期
	var dayString = year+ "/" + month + "/" + day;
	
	export default {
	
		// components: {uniIcon},
	    components: {uniSegmentedControl},
	    data() {
			
	        return {
	            items: ['每日小结','情绪爆炸'],
	            current: 0,
				dayString
	        }
	    },
	    methods: {
	        onClickItem(e) {
	            if (this.current !== e.currentIndex) {
	                this.current = e.currentIndex;
	            }
	        }
	    },
		
	};
	
	
	// var day = today.getDate();//获得当前日期
	// console.log(day)
</script>

<style>
	@import "/colorui/main.css";
	@import "/colorui/icon.css";
	
.whole{
	background-color: #FBFCFB;
}	


.uni_seg{
	background-color: #E9F0F0;
	color:#448088;
	width: 500upx;
	margin: 0upx auto;
	
}


.enterRecord{
	/* width: 100upx; */
	height: 141upx;
	width: 615upx;
	margin: 50upx auto 0;
	background-color: #F1F5F5;
	box-shadow: 5px 5px 5px gainsboro;
	/* padding: 20upx 30upx; */
	display: flex;
	flex-direction: row;
	/* 让flex中的元素垂直居中 */
	align-items:center;
	
	

	/* justify-content:center;  用来处理块状水平居中*/
}
.plus_left{
	flex: 1;
	text-align:center;
}
.plus_right{
	flex: 3;
}
/* 首页----每天的记录卡片 */
.dayCard{
	width: 615upx;
	height: 220upx;
	border: 5upx solid #ECF7FC;
	border-radius: 15upx;
	/* box-shadow: 5px 5px 5px #ECF7FC; */
	margin: 0 auto 40upx;
	display: flex;
	flex-direction: column;
}
/* 首页----卡片中的时间块和阈值块 */
.date{
	flex: 1;
	margin-top: 10upx;
	margin-left: 10upx;
}

/* 压力值 混乱值 活力值 平静值  开始 */
.moodValue{
	flex: 3;
	flex-direction: column;
	display: flex;
}
.values{
	flex: 1;
	flex-direction: row;
	display: flex;
	padding-left: 30upx;
}
.firstValue{
	flex: 1;
}
.secondValue{
	flex: 1;
}
/* 压力值 混乱值 活力值 平静值  结束 */

/* 灰色加号 */
.svg_plus2{
	width: 100upx;
	height: 100upx;
}
/* 绿色加号 */
.svg_plus{
	width: 60upx;
	height: 60upx;
}
</style>
