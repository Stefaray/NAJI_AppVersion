<!-- 
	数据接口
		timeString
		whichExpression
		tagidText
		$note2
 -->
<template>
	<view>
		
		<view class="top_view">
			<view class="getSpace2"></view>
			<view class="dayR_nav">
				<view class="dayR_back"><img @tap="isBack" src="/static/back.svg" class="svg_back"  /></view>
				<view class="dayR_title"><text class="dayR_titleText">每日小结</text></view>
			</view>
		</view>
		<view class="content_view">
			<view class="moodB_date bord space1 ">{{timeString}}</view>
			<view class="feelTitle space2">
				<text class="feelText">此刻心情</text>	
			</view>
			<view class="moodExpression">
				<!-- <image src="../../../../static/u78.png"></image> -->
				<!-- <view style="width: 665upx;height: 150upx;background-color: #448088;"></view> -->
				<view @tap="chooseExp" data-index='1' class="perExpression" :class="[(whichExpression != 1 && whichExpression != 0) ? 'hideView' : 'visualView']">
					<image class="iconExpression" src="../../../../static/record/expression/1.png"></image>
					<view style="padding-left: 15upx;"><text class="expressionText">开心</text></view>
				</view>
				<view @tap="chooseExp" data-index='2' class="perExpression" :class="[(whichExpression != 2 && whichExpression != 0) ? 'hideView' : 'visualView']">
					<image class="iconExpression" src="../../../../static/record/expression/2.png"></image>
					<view style="padding-left: 15upx;"><text class="expressionText">愤怒</text></view>
				</view>
				<view @tap="chooseExp" data-index='3'  class="perExpression" :class="[(whichExpression != 3 && whichExpression != 0) ? 'hideView' : 'visualView']">
					<image class="iconExpression" src="../../../../static/record/expression/3.png"></image>
					<view style="padding-left: 15upx;"><text class="expressionText">悲伤</text></view>
				</view>
				<view @tap="chooseExp" data-index='4'  class="perExpression" :class="[(whichExpression != 4 && whichExpression != 0) ? 'hideView' : 'visualView']">
					<image class="iconExpression" src="../../../../static/record/expression/4.png"></image>
					<view style="padding-left: 15upx;"><text class="expressionText">恐惧</text></view>
				</view>
				<view @tap="chooseExp" data-index='5'  class="perExpression" :class="[(whichExpression != 5 && whichExpression != 0) ? 'hideView' : 'visualView']">
					<image class="iconExpression" src="../../../../static/record/expression/5.png"></image>
					<view style="padding-left: 15upx;"><text class="expressionText">焦虑</text></view>
				</view>
				<view @tap="chooseExp" data-index='6'  class="perExpression" :class="[(whichExpression != 6 && whichExpression != 0) ? 'hideView' : 'visualView']">
					<image class="iconExpression" src="../../../../static/record/expression/6.png"></image>
					<view style="padding-left: 15upx;"><text class="expressionText">感动</text></view>
				</view>
			</view>
			<view class="actTag">
				<view class="tagTitle">
					<text class="tagText">主题标签</text>
					<img src="/static/plus.svg" class="svg_plus" @tap="showModal" data-target="1"/>
					<button v-if="showActTag" class="cu-btn round shadow tagChange" >{{tagidText}}</button>
				</view>
					<view class="grid col-4 padding-sm" @change="radioChange">
						<block v-for="item in tabs" :key="item.id" >
							<view :value="item.id" class="margin-tb-sm text-center">
								<button @tap="menuClick" :data-id="item.id" class="cu-btn round shadow">{{item.value}}</button>
							</view>	
						
						</block>
					</view>
					
					<!-- <button class="cu-btn round shadow tagChange">其他</button> -->
			</view>
			
			<navigator url="../../../editor/editor2" class="moodRecord">
				<view class="moodRecordTitle"><text class="moodRecordText">记录一下</text></view>
				<view class="noteArea"></view>
			</navigator>
		</view>	
		
		
		<!-- 弹出框内容开始 -->
		<view class="cu-modal" :class="modalName==1?'show':''">
			<view class="cu-dialog">
				
				<view class="cu-bar bg-white justify-end">
					<view class="actionLeft" @tap="noModal" >
						<text class="cuIcon-close text-theme"></text>
					</view>	
					<view class="content"><text class="text-theme" style="font:normal bold 32upx '宋体',arial,sans-serif;">自定义标签</text></view>
					<view class="action" @tap="yesModal">
						<text class="cuIcon-check text-theme"></text>
					</view>
				</view>
				<view class="padding-xl">
					<!-- <textarea value="666666" id="textarea1" style="font:normal bold 34upx '宋体' ;"></textarea> -->
					<input v-model="tagidText" type="text" maxlength="10" style="font:normal bold 34upx '宋体' ;" />
				</view>
			</view>
		</view>
		<!-- 弹出框内容结束 -->
	</view>
</template>

<script>
	
	var today = new Date();//获得当前日期
	var year = today.getFullYear();//获得年份
	var month = today.getMonth() + 1;//此方法获得的月份是从0---11，所以要加1才是当前月份
	var day = today.getDate();//获得当前日期
	var hour = today.getHours();
	var minute = today.getMinutes();
	var timeString = year+ "/" + month + "/" + day + " " + hour + ":" + minute;
	var tabs = [];
	var tagidText;
	var showActTag=false;
	// 标签栏开始
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
	//标签栏结束
	
	export default {
		data() {
			return {
				timeString,
				tabs,
				tagidText,
				showActTag,
				modalName:0,
				whichExpression:0,
				toggle:0,
			}
		},
		methods: {
			chooseExp:function(e){
				this.toggle ++;
				if(this.toggle % 2 == 0){
					this.whichExpression = 0;
				}
				else{
					this.whichExpression = e.currentTarget.dataset.index;
				}
			},
			menuClick:function(e){
				var tagid = e.currentTarget.dataset.id;
				this.tagidText = this.tabs[tagid].value;
				this.showActTag = true;
			},
		
			isBack(){
				// console.log(this.$note2)
				var tmp = this.$store.state.note2	
				console.log(tmp)
				uni.request({
					url:this.$url+'/moodBoom',
					data:{
						user_id: this.$store.state.token_user_id,
						timeString: 	this.timeString,
						whichExpression:this.whichExpression,
						tagidText:		this.tagidText,
						moodNote: 		tmp
					},
					method:"GET",
					success:(res) => {
						
						
						if(res.data.status == -1){
							uni.showToast({
									icon:"none",
									title:res.data.desc
							}),
							uni.navigateBack({
							    delta: 1
							});
						}
						else{
							uni.showToast({
									icon:"success",
									title:res.data.desc
							}),
							uni.navigateBack({
								delta: 1
							})
							console.log('yeeeeeeeeessss')
							this.$store.commit("UNSHIFTmoodBoom",res.data.new[0])
						}
						this.$store.commit("ChangeNote","")
					},
					fail: (res) => {
						console.log('---------1')
						uni.showToast({
								icon:"none",
								title:res.data.desc
						})
						uni.navigateBack({
						    delta: 1
						});
					}
					
				})
				
			},
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target;
			},
			yesModal(e) {
				if(this.tagidText==''){
					this.showActTag = false
				}
				else{
					this.showActTag = true
				}
				
				this.modalName = 0
			},
			noModal(e) {
				this.modalName = 0
				this.notedata = ''
			},
			
		}
	}
</script>

<style>
	@import "/colorui/main.css";
	@import "/colorui/icon.css";
	/* 隐藏一个块-----六个表情 */
	.hideView{
		visibility: hidden;
	}
	.visualView{
		visibility:visible;
	}
	/* 弹出层的关闭按钮位置 */
	.justify-end {
		justify-content: space-between;
		margin-left: 30upx;
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
	.noteArea{
		background-color: #F6F9FA;
		width: 665upx;
		height: 290upx;
		border: 5upx solid #ECF7FC;
		border-radius: 15upx;
		/* box-shadow: 5px 5px 5px #ECF7FC; */
		margin: 0 auto 40upx;
	}
	.space1{
		margin: 20upx 0 20upx 30upx;
	}
	.space2{
		margin: 30upx 0 30upx 30upx;
	}
	.space3{
		margin: 30upx 0 30upx 20upx;
	}
	/* 包含六个表情的总块 */
	.moodExpression{
		margin: 20upx 0 0upx 34upx;
		display: flex;
		flex-direction: row;
	}
	/* 六个表情的单块 */
	.perExpression{
		flex:1;
		/* height: 100%; */
		/* width: 100upx; */
	}
	/*  */
	.iconExpression{
		width: 89upx;
		height: 80upx;
		/* transform: scale(10%); */
	}
	/* 返回按钮 */
	.svg_back{
		width: 60upx;
		height: 60upx;
	}
	.dayR_nav{
		display: flex;
		flex-direction: row;
		
	}
	.dayR_back{
		flex: 1;
		text-align:center;
	}
	.dayR_title{
		margin-left: 100upx;
		flex: 3;
	}
	/* 此刻心情 */
	.feelTitle{
		margin: 40upx 0 20upx 34upx;
	}
	/* 主题标签 */
	.tagTitle{
		margin: 20upx 0 0upx 34upx;
	}
	/* 记录一下 */
	.moodRecordTitle{
		margin: 20upx 0 20upx 34upx;
	}
	
</style>
