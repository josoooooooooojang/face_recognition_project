<template>
    <v-app>
        <toolbar></toolbar>
        <v-container>
            <v-row justify="center">
                <v-col cols="8">
                <v-card class="mx-auto"
                        max-width="85%">
                    <img
                        class="white--text align-end"
                        height="100%"
                        width="100%"
                        id="myImg"
                        :src="resultImgSrc"
                    ><img>
                </v-card>
                </v-col>
            </v-row>

            <v-row>
                <v-tabs
                v-model="tab"
                background-color="#fafafa"
                icons-and-text
                centered
                >
                <v-tabs-slider></v-tabs-slider>
        
                <v-tab @click="info('eye')">
                눈
                <v-icon>mdi-github-face</v-icon>
                </v-tab>
        
                <v-tab @click="info('eyebrow')">
                눈썹
                <v-icon>mdi-github-face</v-icon>
                </v-tab>
        
                <v-tab @click="info('nose')">
                코
                <v-icon>mdi-github-face</v-icon>
                </v-tab>
                <v-tab @click="info('mouse')">
                입
                <v-icon>mdi-github-face</v-icon>
                </v-tab>
            </v-tabs>
            </v-row>
            <v-row>
                <v-col>
                    <p>{{resultTitle}}</p>
                </v-col> 
            </v-row>
            <v-textarea
                v-if="resultNegative=='-'"
                outlined
                readonly
                auto-grow
                :value = resultPositive
            ></v-textarea>
            <v-textarea
                v-else
                outlined
                readonly
                auto-grow
                :value = resultPositive+but+resultNegative
          ></v-textarea>
        </v-container>
    </v-app>
</template>
<script src="http://code.jquery.com/jquery-latest.min.js"></script>
<script>
import toolbar from "@/components/toolbar.vue";
export default {
    components : {
        toolbar
    },
    data(){
        return {
            resultTitle : "temp Title",
            resultPositive : "temp Contents......",
            resultNegative : 'test',
            response: {},
            resultImgSrc : "",
            but : " 다만, "
        }
    },
    mounted(){
       this.info('eye')
    },
    methods : {
        info(data){

            var find=''
            if(data=='eyebrow'){
                find='eye_brow'
            }else{
                find=data
            }

            console.log('this.$store.state.photo[data]', this.$store.state.photo[find]);
            
            this.resultTitle=this.$store.state.photo[find][0].title
            this.resultPositive=this.$store.state.photo[find][0].positive
            this.resultNegative=this.$store.state.photo[find][0].negative
            this.resultImgSrc = "http://192.168.31.91:8000/api/media/"+this.$store.state.photo.name+"/"+this.$store.state.photo.name+"_"+data+".jpg";
        }
    }

}
</script>
<style>
.v-text-field__slot textarea{
  height: 35vh;
}
</style>
