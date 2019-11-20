<template>
    <v-app style="background-color:rgb(52, 152, 219)">
    <v-container grid-list-xs id="home-background">
        <v-row class="ma-1 ml-8 pt-8">
            <v-col cols class="display-2 font-weight-bold white-text">
                <v-row class="my-3">About</v-row>
                <v-row class="my-3">Your</v-row>
                <v-row class="my-3">Face</v-row>
            </v-col>
            <v-col cols class="mt-3">
                <v-icon size="100" class="pt-12 pl-6" color="white">mdi-account-circle-outline</v-icon>
            </v-col>
        </v-row>
        <v-row class="request-icons p-30p">
        <v-col>
            <v-row justify="center">
                <button @click="movePage('faceAnalysis')"><v-icon size="75" :color="iconColor">mdi-file-find-outline</v-icon></button>
            </v-row>
            <v-row justify="center">
                관상보기
            </v-row>
        </v-col>
        <v-col>
            <v-row justify="center">
                <button @click="movePage('dictionary')"><v-icon size="75" :color="iconColor">mdi-book-open-page-variant</v-icon></button>
            </v-row>
            <v-row justify="center">
                관상사전
            </v-row>
        </v-col>
        </v-row>
        <v-divider></v-divider>
        
        <v-row class="white-text" justify="center">
            <v-col cols="11" id="login-help">
                여러분의 관상을 봐드립니다.
            </v-col>
        </v-row>
    </v-container>
    </v-app>
</template>
<script>
export default {
    methods : {
        movePage(path){
            this.$router.push({name : path});
        }
    }
}
</script>
<style>
    .white-text{
        color: white;
    }
    .p-10p{
        padding-top: 10%
    }
    #login-help{
        padding-top: 0;
    }
</style>