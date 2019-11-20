import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    photo : {
      // "name":"6.581923052952608",
      // "eye":[
      // {
      //   "number":1,
      //   "title":"용안(龍眼)",
      //   "positive":"용의 눈과 같은 용안은 고귀한 존재가 되는 상이자 고위 관직에 오르는 상이다. 검은자위와 흰자위가 분명하면 정신적으로 강하고, 눈초리가 길게 째지므로 눈안에 기(氣)와 신(神)이 머문다. 이런 눈을 가진 사람은 부귀하고, 많은 급여를 받는 지위에 올라 왕을 곁에 모시는 신하가 되기도 한다.",
      //   "negative":"-"
      // }],
      // "eye_brow":[
      // {
      //   "number":1,
      //   "title":"유용미(遊龍眉)",
      //   "positive":"용이 노니는 듯한 맑고 수려한 눈썹이다. 유용미에 눈동자가 크고 눈빛이 강하여 마치 용이 엎드린 듯한 복룡안(伏龍眼)의 눈을 갖추면, 총명하고 용감하여 결단력이 있다.",
      //   "negative":"-"
      // }],
      // "nose":[
      // {
      //   "number":1,
      //   "title":"호비(虎鼻)",
      //   "positive":"호비란 코끝이 둥글고 크고, 콧구멍은 보이지 않고, 난대와 정위(양 콧망울)가 없는 형태를 말한다. 콧날이 구부러지거나 비뚤어지지 않고 곧게 뻗어 있으며, 산근(두 눈 사이)이 넓은 코로 매우 보기 드물다.",
      //   "negative":"-"
      // }],
      // "mouse":[
      // {
      //   "number":1,
      //   "title":"사자구(四字口)",
      //   "positive":"사(四)자 모양을 한 입의 형태다. 가장 좋은 상으로, 부귀지격(富贵之格)이다. 입의 윤곽이 분명하고, 상하 입술이 잘 갖추어져 있으며, 구각이 위로 향해 있는것이 좋은 상이다. 이러한 입을 가진 사람은 총명하고 다방면에서 재능이 뛰어나 학문에서 두각을 나타내 부귀를 누리며, 반드시 공명을 얻는다.",
      //   "negative":"-"
      // }]
      },
    dictionarys : [
    ],
    isLoading : false,
  },
  mutations: {
    init(state,data){
      //test
      // state.photo.name = data.name;



      state.photo=data

    },
    startLoading(state){
      state.isLoading = true;
    },
    endLoading(state){
      state.isLoading = false;
    },
    init_dictionarys(state, data){
      state.dictionarys=[]
      state.dictionarys=data
    },
    loadFace(){
      alert("loadFace")
    },
    loadEye(){
      alert("loadEye")
    },
    loadEyeBrow(){
      alert("loadEyeBrow")
    },
    loadNose(){
      alert("loadNose")
    },
    loadMouse(){
      alert("loadMouse")
    },
  },
  actions: {
  },
  modules: {
  }
})
