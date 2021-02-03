<template>
    <view>
		<view class="whole">
			
			<!-- 顶部栏开始 -->
			<view class="top_view">
				<view class="getSpace1"></view>
				<button style="margin-left: 180upx;" @tap="switchButton1" class="switchButton" :class="whiteBgcControl==1?'whiteBgc':''"><text style="color: #448088;">每日小结</text></button>
				<button @tap="switchButton2" class="switchButton" :class="whiteBgcControl==2?'whiteBgc':''"><text style="color: #448088;">情绪爆炸</text></button>
				<!-- <uni-segmented-control :current="current" :values="items" @clickItem="onClickItem" style-type="button" active-color="#448088" class="uni_seg"></uni-segmented-control> -->
			</view> 
			 <!-- 顶部栏结束 -->
			
			
			<view v-show="whiteBgcControl === 1">
			    
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
					
					
					<view v-for="item in $store.state.dayRemindList" class="dayCard" type="primary" @tap="togglePopup1(item)">
						<view class="date">
							<text class="record_date">{{item.dayString}}</text>
						</view>
						<view class="moodValue">
							<image class="card_bottomImage" :src="item.dayRate_icon" ></image>
							<view class="card_bottomTextView">
								<text class="card_bottomText">{{item.dayRate_text}}</text>
							</view>

						</view>
						
					</view>
					<!-- <view class="dayCard"></view>
					<view class="dayCard"></view> -->
				  
				   
				</view>
				
			 </view>
			 <view v-show="whiteBgcControl === 2">
			     
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
		<!-- 正式卡片————————情绪爆炸 -->
				 	<view v-for="item in $store.state.moodBoomList" class="dayCard"  type="primary" @tap="togglePopup2(item)" >

				 		<view class="moodValue">
							<view class="card_bottomImage0">
								<image class="card_bottomImage1" :src='item.whichExpression' style="width: 99upx;height: 50upx; margin: 10upx 0 0 20upx;"></image>
								<view class="card_bottomImage2"><text class="expressionText">{{item.whichExpressionText}}</text></view>
							</view>
							<!-- <view class="card_bottomImage"><text class="expressionText">开心</text></view> -->
				 			<view class="card_bottomTextView">
				 				<view class="card_bottomText1"><text class="moodB_date">{{item.timeString}}</text></view>
								<view class="card_bottomText2" style="margin-top: 10upx;">
									<!-- <text class="moodB_content" v-html="item.moodNote"></text> -->
									<view v-html="formatStatus(item.moodNote)"></view>
									<!-- <rich-text class="moodB_content">{{item.moodNote}}</rich-text> -->
									<!-- <rich-text class="moodB_content" :nodes="item.moodNote"  ></rich-text> -->
								</view>
				 			</view>
							
				 			
				 		</view>
				 	</view>
				<!-- 	<view class="dayCard"></view>
				 	<view class="dayCard"></view>
				   -->
				    
				 </view>
				 
			 </view>
			
			
		</view>
       
	   <!-- 弹出层开始 -->
	 <uni-popup ref="showpopup" :type="type">
		 <view class="popup-content">
			 <view class="popupTop">
				 <view class="popupTime">
					 <text class="record_date">{{dayPopupContent.dayString}}</text>
				 </view>
				 <view class="popupIcon">
					 <img src="/static/record/collect.svg" class="svgPopup"  />
					 <img src="/static/record/edit.svg" class="svgPopup" @tap="Nav_historyCard" />
				 </view>
			 </view>
			 <view class="popupMiddle">
				 <view class="moodValue">
				 	<image class="card_bottomImage" :src="dayPopupContent.dayRate_icon" ></image>
				 	<view class="card_bottomTextView">
				 		<text class="card_bottomText">{{dayPopupContent.dayRate_text}}</text>
				 	</view>
				 </view>
			 </view>
			 <view class="popupBottom">
				 <view class="noteContent">
					 <!-- <text v-html="dayPopupContent.dayNote" class="placeholderText placeholderTexthide"></text> -->
					 <view v-html="formatStatus(dayPopupContent.dayNote)" class="placeholderText placeholderTexthide"></view>
					 
				 </view>
			 </view>
		 </view>
	 </uni-popup>
		<!-- 弹出层结束 -->
		
		<!--情绪爆炸弹出层开始 -->
		<!-- 弹出层开始 -->
		<uni-popup ref="showpopup2" :type="type">
				 <view class="popup-content">
					<image :src='moodPopupContent.whichExpression' style="width: 178upx;height: 160upx;"></image>
					<view class="expressionTextPopupView"><text class="expressionTextPopup">{{moodPopupContent.whichExpressionText}}</text></view>
					<view class="cardTag">
						<!-- <text >随手小记的内.......</text> -->
						 <text class="placeholderTextGreen placeholderTexthide">{{moodPopupContent.tagidText}}</text>
					</view>
					<view class="cardNote">
						<view v-html="formatStatus(moodPopupContent.moodNote)"  style="text-align: center; font:normal bold 30upx '宋体',arial,sans-serif; color: #448088;"></view>
						<!-- <text v-html="moodPopupContent.moodNote" style="text-align: center; font:normal bold 30upx '宋体',arial,sans-serif; color: #448088;"></text>	 -->
					</view>
					<view class="cardTime">
						<text class="placeholderText1 placeholderTexthide">{{tmp}}</text>
					</view>
				 </view>
				
		</uni-popup>
		<!-- 情绪爆炸弹出层结束 -->
		
		
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
	var hour = today.getHours();
	var min = today.getMinutes();
	var timeString = dayString + ' ' + hour + ':' + min ;
	
	// var moodNote = ''
	export default {
		
		onLoad(){
			uni.request({
				url:this.$url+'/getUID',
				data:{
					user_id : this.$store.state.token_user_id,
				},
				method:"GET",
				success:(res)=>{
					console.log(res)
				}
			}),
			uni.request({
				url:this.$url+'/record_dayRemind',
				data:{
					user_id: 36
				},
				method:"GET",
				success:(res) => {
					
					this.$store.commit("ChangedayRemind",res.data.recordRemindList)
					this.$store.commit("ADDdayRemind",res.data.recordRemindList)
					console.log(this.$store.state.dayRemindList)
					
					uni.request({
						url:this.$url+'/record_moodBoom',
						data:{
							user_id: 36
						},
						method:"GET",
						success:(res) => {

							this.$store.commit("ChangemoodBoom",res.data.moodBoomList)
							this.$store.commit("ADDmoodBoom",res.data.moodBoomList)
							console.log(this.$store.state.moodBoomList)
							for(var i=0; i<this.$store.state.moodBoomList.length; i++){
								this.moodBoomList[i] = this.$store.state.moodBoomList[i]
							}
							for(var i=0; i<this.$store.state.dayRemindList.length; i++){
								this.dayRemindList[i] = this.$store.state.dayRemindList[i]
							}
							
						}
					})
					
				}
			})
			
		},
		// onShow: function() {
		// 	for(var i=0; i<this.$store.state.dayRemindList.length; i++){
		// 		this.dayRemindList[i] = this.$store.state.dayRemindList[i]
		// 	}
		// 	for(var i=0; i<this.$store.state.moodBoomList.length; i++){
		// 		this.moodBoomList[i] = this.$store.state.moodBoomList[i]
		// 	}
		// 	console.log('testtest')
		// },
		
		
		// components: {uniIcon},
	    components: {uniSegmentedControl},
	    data() {
			
	        return {
				moodBoomList:[],
				dayRemindList:[],
				whiteBgcControl:1,
	            items: ['每日小结','情绪爆炸'],
	            current: 0,
				dayString,
				timeString,
				modalName:0,
				moodNote:'此刻无记录....',
				moodPopupContent:[],
				dayPopupContent	:[],	
				tmp:"",
				type:"",
				// moodNote:'<text>45</text>.....<text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><tex<text>45</text>.....<text>45</text><text>45</text><text>45</text><text>45</text><text>45</te<text>45</text>.....<text>45</text><text>45</text><text>45。。。。。。。。。。。。。。。。。。。。。</text><text>45</text><text>45</tet>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text><text>45</text>'
	        }
	    },
	// 弹出层入口开始-----------------------------------------------
	    methods: {
		formatStatus(index){
			return index;
		},
			
		Nav_historyCard(){
			// var targetOption = dayPopupContent.targetOption
			this.$nextTick(() => {
				this.$refs['showpopup'].close()
			})
			uni.navigateTo({
					url:"dayRemind/dayRemind?item="+ encodeURIComponent(JSON.stringify(this.dayPopupContent))
			})
		},
		
		switchButton1(){
			this.whiteBgcControl = 1;
		},
		switchButton2(){
			this.whiteBgcControl = 2;
		},
		togglePopup1(item){
			this.dayPopupContent = item

			// console.log(this.moodPopupContent)
			this.type = 'center'
			this.$nextTick(() => {
				this.$refs['showpopup'].open()
			})
		},
		togglePopup2(item) {
			// moodPopupContent:[],
			// console.log(whichExpression+" "+whichExpressionText+" "+tagidText+" "+moodNote+" "+timeString)
			this.moodPopupContent = item
			this.tmp = item.timeString.split(' ')[0];
			
			// console.log(this.moodPopupContent)
			this.type = 'center'
			this.$nextTick(() => {
				this.$refs['showpopup2'].open()
			})
		},
	// 弹出层入口结束------------------------------------------------
		onClickItem(e) {
	            if (this.current !== e.currentIndex) {
	                this.current = e.currentIndex;
	            }
	        },
			showModalCard(e) {
				// console.log(11)
				this.modalName = e.currentTarget.dataset.target;
				// console.log(this.modalName)
				// console.log(11)
			},
			yesModal(e) {
				
				this.modalName = 0
			},
			noModal(e) {
				this.modalName = 0
				this.notedata = ''
			}
	    }
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
	margin:30upx 0 10upx 20upx;
	flex: 3;
	flex-direction: row;
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
/* 卡片上的底部 */
.card_bottomImage{
	flex:1;
	width: 60upx;
	height: 100upx;
/* 	display: flex;
	flex-direction: column; */
}
.card_bottomImage0{
	flex:1;
	/* width: 60upx;
	height: 100upx; */
	display: flex;
	flex-direction: column;
}
.card_bottomImage1{
	flex: 2;
}
.card_bottomImage2{
	flex: 1;
	padding-left: 35upx;
}
.card_bottomTextView{
	padding-top: 10upx;
	padding-left: 30upx;
	flex: 3;
	display: flex;
	flex-direction: column;
	/* justify-content: ; */
}
.card_bottomTextView1{
	flex: 1;
}
.card_bottomTextView2{
	flex: 1;
}
/*  */
.cardPopup{
	width: 550upx;
	height: 700upx;
	background-color: #1CBBB4;
}
/* 弹出层样式 */
.popup-content {
		/* #ifndef APP-NVUE */
		display: block;
		/* #endif */
		background-color: #fff;
		padding: 50upx 45upx 30upx;
		font-size: 14px;
		width: 545upx;
		height: auto;
		border-radius: 20upx;
		border: 5upx solid #ECF7FC;
		text-align: center;
		align-items:center;
		position:relative;
		padding-bottom: 100upx;
		
		/* 让文字自动换行 */
		word-wrap:break-word;
		word-break:break-all; 

		
}

/* 弹出层顶部 */
.popupTop{
	width: 100%;
	height: 5%;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	margin-bottom: 30upx;
	/* background-color: #0066CC; */
}
.popupTime{
	flex: 2;
	/* justify-content: flex-start; */
}
.popupIcon{
	flex: 1;
}
/* 弹出层图标 */
.svgPopup{
	margin: 0 5upx;
	width: 50upx;
	height: 50upx;
}

/* 随手小记的内容 */
.noteContent{
	margin: 30upx auto;
	width: 400upx;
	height: auto;
	/* background-color: #0066CC; */
	border: 5upx solid rgb(238,240,240);
	border-radius: 15upx;
	/* box-shadow: 5px 5px 5px #ECF7FC; */
	text-align:center;	
	/* line-height:350upx; */
}
/* 情绪爆炸-----弹出层卡片标签 */
.cardTag{
	margin: 20upx auto;
	width: 300upx;
	height: 90upx;
	border-radius: 15upx;
	border: 5upx solid rgb(238,240,240);
	text-align: center;
	line-height: 90upx;
}
/* 情绪爆炸----弹出层时间 */
.cardTime{
	margin: 0 auto;
	padding:  30upx 160upx;
	bottom: 5upx;
	position: absolute;
}
/* 切换按钮 */
.switchButton{
		border-radius: 15upx;
		/* border: dashed rgb(238,241,234) ; */
		/* margin-bottom: 100upx; */
		display:inline-block;
		width: 200upx;
		height: 80upx;
		background-color: rgb(235,241,242);
}
/* 白色背景 */
.whiteBgc{
	background-color: #ffffff;
}
.card_bottomText2{
	display: -webkit-box;
	  overflow: hidden;
	  -webkit-box-orient: vertical;
	  -webkit-line-clamp: 1;
}
</style>



				<!-- <view class="values">
					<view class="firstValue"><text class="record_values">压力值</text></view>
					<view class="secondValue"><text class="record_values">混乱值</text></view>
				</view>
				<view class="values">
					<view class="firstValue"><text class="record_values">活力值</text></view>
					<view class="secondValue"><text class="record_values">平静值</text></view>
				</view> -->
							