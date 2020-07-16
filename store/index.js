import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex);
const store = new Vuex.Store({
 state : {
	note1 : "",
	note2 : "",
	token_user_id:'36',
	hasLogin: false,
	moodBoomList:[],
	dayRemindList:[]
 },
 mutations : {
	  ChangeNote(state,data){
		  state.note2 = data;
	  },
	  ChangeNote1(state,data){
	  		  state.note1 = data;
	  },
	  ChangeToken(state,data){
	  		  state.token_user_id = data;
	  },
	  ChangemoodBoom(state,data){
	  		  state.moodBoomList  = data;
	  },
	  ADDmoodBoom(state){
		for(var i=0; i<state.moodBoomList.length; i++){
			if(state.moodBoomList[i].whichExpression == 0){
				state.moodBoomList[i].whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F1.png'
				state.moodBoomList[i].whichExpressionText = '无感'
			}
			else if(state.moodBoomList[i].whichExpression == 1){
				state.moodBoomList[i].whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F1.png'
				state.moodBoomList[i].whichExpressionText = '开心'
			}
			else if(state.moodBoomList[i].whichExpression == 2){
				state.moodBoomList[i].whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F2.png'
				state.moodBoomList[i].whichExpressionText = '愤怒'
			}
			else if(state.moodBoomList[i].whichExpression == 3){
				state.moodBoomList[i].whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F3.png'
				state.moodBoomList[i].whichExpressionText = '悲伤'
			}
			else if(state.moodBoomList[i].whichExpression == 4){
				state.moodBoomList[i].whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F4.png'
				state.moodBoomList[i].whichExpressionText = '恐惧'
			}
			else if(state.moodBoomList[i].whichExpression == 5){
				state.moodBoomList[i].whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F5.png'
				state.moodBoomList[i].whichExpressionText = '焦虑'
			}
			else if(state.moodBoomList[i].whichExpression == 6){
				state.moodBoomList[i].whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F6.png'
				state.moodBoomList[i].whichExpressionText = '感动'
			}
		}
	  },
	  ADDdayRemind(state){
		for(var i=0; i<state.dayRemindList.length; i++){
			var tmp_str
			tmp_str = state.dayRemindList[i].targetOption.split(' ')
			var total = 0;
			for(var j=0; j<tmp_str.length; j++){
				total += parseInt(tmp_str[j])
			}
			if(total>=0 && total<=5){
				state.dayRemindList[i].dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fbad.svg'
				state.dayRemindList[i].dayRate_text =  '抱抱'
			}
			else if(total>=6 && total<=11){
				state.dayRemindList[i].dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fsoso.svg'
				state.dayRemindList[i].dayRate_text =  '还行'
			}
			else if(total>=12 && total<=18){
				state.dayRemindList[i].dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fgood.svg'
				state.dayRemindList[i].dayRate_text =  '不错'
			}
			else if(total>=19 && total<=25){
				state.dayRemindList[i].dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fverygood.svg'
				state.dayRemindList[i].dayRate_text =  '非常好'
			}
		}
	  },
	  ChangedayRemind(state,data){
		  state.dayRemindList = data;
	  },
	  UPDATEdayRemind(state,data){
		  var tmp_str
		  tmp_str = data.targetOption.split(' ')
		  var total = 0;
		  for(var j=0; j<tmp_str.length; j++){
		  	total += parseInt(tmp_str[j])
		  }
		  if(total>=0 && total<=5){
		  	data.dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fbad.svg'
		  	data.dayRate_text =  '抱抱'
		  }
		  else if(total>=6 && total<=11){
		  	data.dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fsoso.svg'
		  	data.dayRate_text =  '还行'
		  }
		  else if(total>=12 && total<=18){
		  	data.dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fgood.svg'
		  	data.dayRate_text =  '不错'
		  }
		  else if(total>=19 && total<=25){
		  	data.dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fverygood.svg'
		  	data.dayRate_text =  '非常好'
		  }
		  for(var k=0; k<state.dayRemindList.length; k++){
			  if(state.dayRemindList[k].dayString == data.dayString){
				  // state.dayRemindList[k] = data;
				  Vue.set(state.dayRemindList, k, data)
				  break;
			  }
			  console.log(state.dayRemindList[k])
		  }
	  },
	  UNSHIFTdayRemind(state,data){
		  var tmp_str
		  tmp_str = data.targetOption.split(' ')
		  var total = 0;
		  for(var j=0; j<tmp_str.length; j++){
		  	total += parseInt(tmp_str[j])
		  }
		  if(total>=0 && total<=5){
		  	data.dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fbad.svg'
		  	data.dayRate_text =  '抱抱'
		  }
		  else if(total>=6 && total<=11){
		  	data.dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fsoso.svg'
		  	data.dayRate_text =  '还行'
		  }
		  else if(total>=12 && total<=18){
		  	data.dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fgood.svg'
		  	data.dayRate_text =  '不错'
		  }
		  else if(total>=19 && total<=25){
		  	data.dayRate_icon = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fday_score%2Fverygood.svg'
		  	data.dayRate_text =  '非常好'
		  }
		  state.dayRemindList.unshift(data)
		  
	  },
	  UNSHIFTmoodBoom(state,data){
		  if(data.whichExpression == 0){
		  	data.whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F1.png'
		  	data.whichExpressionText = '无感'
		  }
		  else if(data.whichExpression == 1){
		  	data.whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F1.png'
		  	data.whichExpressionText = '开心'
		  }
		  else if(data.whichExpression == 2){
		  	data.whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F2.png'
		  	data.whichExpressionText = '愤怒'
		  }
		  else if(data.whichExpression == 3){
		  	data.whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F3.png'
		  	data.whichExpressionText = '悲伤'
		  }
		  else if(data.whichExpression == 4){
		  	data.whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F4.png'
		  	data.whichExpressionText = '恐惧'
		  }
		  else if(data.whichExpression == 5){
		  	data.whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F5.png'
		  	data.whichExpressionText = '焦虑'
		  }
		  else if(data.whichExpression == 6){
		  	data.whichExpression = 'http://ray34.cn-sh2.ufileos.com/%E4%B8%89%E5%88%9B%E8%B5%9B%2Fexpression%2F6.png'
		  	data.whichExpressionText = '感动'
		  }
		  
		  state.moodBoomList.unshift(data)
		  
	  }
 },
 actions:{
	 
 }
});
export default store