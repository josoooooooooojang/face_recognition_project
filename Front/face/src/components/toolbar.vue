<template>
    <v-card flat>
          <div>
            <v-toolbar >
              <v-btn @click="goBack" icon>
                <v-icon>mdi-chevron-left</v-icon>
              </v-btn>
                
              <v-spacer></v-spacer>
              <v-toolbar-title style="margin-right : 9%">{{title}}</v-toolbar-title>
              <v-spacer></v-spacer>
              
            </v-toolbar>
          </div>
    </v-card>
</template>
<script>
export default {
    props:['toolbarTitle'],
    data(){
      return{
        title : 'About Your Face',
        hidden : true
      }
    },
    mounted(){
      if( this.toolbarTitle != null)
        this.title = this.toolbarTitle;
    },
    methods:{
      goBack(){
        this.$router.go(-1)
      },
    },
}
</script>
<style>

</style>