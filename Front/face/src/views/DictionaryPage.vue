<template>
<v-app>
  <toolbar toolbarTitle="Dictionary"></toolbar>
  <!-- margin-left/right 18% -->
  <v-tabs
        v-model="tab"
        background-color="#fafafa"
        icons-and-text
        centered
      >
        <v-tabs-slider></v-tabs-slider>
  
        <v-tab @click="find_info('EYE')">
          눈
          <v-icon>mdi-github-face</v-icon>
        </v-tab>
  
        <v-tab @click="find_info('EYEBROW')">
          눈썹
          <v-icon>mdi-github-face</v-icon>
        </v-tab>
  
        <v-tab @click="find_info('NOSE')">
          코
          <v-icon>mdi-github-face</v-icon>
        </v-tab>
        <v-tab @click="find_info('MOUSE')">
          입
          <v-icon>mdi-github-face</v-icon>
        </v-tab>
  </v-tabs>
  <v-flex
    v-for="(item,i) in this.$store.state.dictionarys"
    :key="i"
  >
    <v-card
      class="mx-auto"
      height="80%"
      width="80%"
      >
        <v-card-text>
          <h3 class="text--primary">{{item.title}}</h3>
          <img class="show" :src="'http://192.168.31.91:8000/api/media/dictionarys/'+type+'/'+item.number+'.jpg'"/>
          <v-textarea
            v-if="item.negative=='-'"
            outlined
            readonly
            auto-grow
            :value = item.positive
          ></v-textarea>
          <v-textarea
            v-else
            outlined
            readonly
            auto-grow
            :value = item.positive+but+item.negative
          ></v-textarea>
        </v-card-text>
    </v-card>
    <br/>
  </v-flex>
</v-app>
</template>

<script>
import toolbar from "@/components/toolbar.vue";
export default {
  components :{
    toolbar
  },
  data () {
    return {
      type : '',
      but : " 다만, "
    }
  },
  mounted : function(){
      this.find_info('EYE')
  },
  methods: {
    find_info : function(search){
        var scope=this;
        this.type=search;
        $.ajax({
          type : "GET",
          url : "http://192.168.31.91:8000/api/dictionarys/",
          data : {
            types : search
          },
          success: function(data){
            scope.$store.commit("init_dictionarys",data)
            console.log('들어간거', scope.$store.state.dictionarys)
          }
        })
    },
  }
}
</script> 

<style>
.divider{
    border: 1px solid gray;
}
.gray-background{
    background-color: #F5F5F5;
}
.show{
  width: 50%;
}
#slide{
  margin-left: 18%;
  margin-right: 18%;
}
.tabs{
  width: 50%;
}
.v-text-field__slot textarea{
  height: 35vh;
}
</style>