<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
export default {
  data () {
      return {
        activeBtn: 1,
      }
    },
  methods :{
    onBackKeyDown(){
      console.log('onBackKeyDown', navigator.notification);
      
      navigator.notification.confirm("Are you sure you want to exit the application?",this.fnLogout,"Warning","Ok,Cancel");


    },
    onDeviceReady(){
      // document.addEventListener("backbutton", this.onBackKeyDown, false);
    },
    fnLogout(button) {
      if(button == 1) {
          $.ajax({
          type : "GET",
          url : "http://192.168.31.91:8000/api/DB_delete",	
          success : function(data){
            navigator.app.exitApp();
          }
        })
    } else {
        return; //No action if presses "cancel"
    }                     
 }
  },
  mounted(){
    document.addEventListener("deviceready", this.onDeviceReady, false);
    window.addEventListener('beforeunload', function(event) {
      $.ajax({
          type : "GET",
          url : "http://192.168.31.91:8000/api/DB_delete",	
          success : function(data){
            navigator.app.exitApp();
          }
        })
    });
  }
}
</script>
<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

body.main{
  background-color: rgb(52, 152, 219);
}

</style>
