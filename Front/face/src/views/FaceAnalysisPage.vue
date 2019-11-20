<template>
    <v-app>
        <toolbar toolbarTitle="Face Analysis"></toolbar>
        <v-container grid-list-xs>
            <v-row  justify="center">
                <v-col cols="1"></v-col>
                <v-col cols="10" class="mt-1">
                    <h1>재미로 보는 관상</h1>
                    <p class="help-text">보다 정확한 결과를 얻고 싶다면,<br/>평정심을 유지한 채 사진을 찍어주세요.</p>
                </v-col>
                <v-col cols="1"></v-col>
                <v-col class="icon-profile">
                    <v-icon size="75">mdi-face-recognition</v-icon>
                </v-col>
            </v-row>
            <requestAnalysis/>

            <v-overlay
            :absolute="absolute"
            :value="$store.state.isLoading"
            >
            
            <v-row><img src="@/assets/Magnify-1.5s-200px.gif"/></v-row>
            <v-row justify="center">분석 중입니다...</v-row>
            
            </v-overlay>

        </v-container>
    </v-app>
</template>
<script>
// eslint-disable-next-line no-unused-vars
import toolbar from "@/components/toolbar.vue";
import requestAnalysis from "@/components/requestAnalysis.vue";

export default {
    components:{
        toolbar,
        requestAnalysis,
    },
    data(){
        return {
            absolute: true,
            overlay: false,
        }
    },
    computed: {
        isLoading() {
            return this.$store.state.isLoading
        }
    },


}
</script>
<style>
.help-text{
    color: #757575;
    margin-top: 5%;
}
.icon-btn{
    /* border: 3 solid black;
    color: black; */
}
.icon-profile{
    padding-top: 10%;
}
</style>