<template>
    <v-row class="request-icons p-30p">
        <v-col>
            <v-row justify="center">
                <button @click="takePicture"><v-icon size="75" :color="iconColor">mdi-camera-enhance-outline</v-icon></button>
            </v-row>
            <v-row v-if="!isMainPage()" justify="center">
                사진 촬영
            </v-row>
        </v-col>
        <v-col>
            <v-row justify="center">
                <button @click="openFilePicker"><v-icon size="75" :color="iconColor">mdi-image</v-icon></button>
            </v-row>
            <v-row v-if="!isMainPage()" justify="center">
                불러오기
            </v-row>
        </v-col>
    </v-row>
</template>
<script>
export default {
    props :['who'],
    data(){
        return {
            iconColor : "#616161",
        }
    },
    methods:{
        test(){
            console.log('this.$store.state.isLoading',this.$store.state.isLoading);
            this.$store.commit("startLoading")
            
        },
        isMainPage(){
            if( this.who == 'main') return true;
            return false;
        },
        takePicture : function(){
            var vueObject = this;
            var camera_srcType = Camera.PictureSourceType.CAMERA;
            var camera_options = this.setCameraOptions(camera_srcType);
            
            navigator.camera.getPicture(function cameraSuccess(imgurl) {
                // You may choose to copy the picture, save it somewhere, or upload.
                vueObject.sendImageToServer(imgurl);
                
            }, function cameraError(error) {
                console.debug("Unable to obtain picture: " + error, "app");
            }, camera_options);
        },
        openFilePicker : function(selection){
            var vueObject = this;

            var camera_srcType = Camera.PictureSourceType.SAVEDPHOTOALBUM;
            var camera_options = this.setCameraOptions(camera_srcType);

            if (selection == "thumnail-image") {
                // Camera.EncodingType (e.g., JPEG) must match the selected image type.
                camera_options.targetHeight = 100;
                camera_options.targetWidth = 100;
            }
            navigator.camera.getPicture(function success(imageUri) {

                // Do something
                vueObject.sendImageToServer(imageUri);

            }, function error(error) {
                console.debug("Unable to obtain picture: " + error, "app");
            }, camera_options);
        },
        sendImageToServer(imgurl) {
            this.$store.commit("startLoading")

            var vueObject = this;
            var fileUploadOptions = new FileUploadOptions();
            fileUploadOptions.fileKey="image";
            fileUploadOptions.httpMethod = "POST";
            fileUploadOptions.fileName=imgurl.substr(imgurl.lastIndexOf('/')+1);
            fileUploadOptions.mimeType="image/jpeg";

            // var params = new Object();
            // fileUploadOptions.params = params;
            // options.headers = {
            // Connection: "close"
            // }
            fileUploadOptions.chunkedMode = false;
            
            
            var fileTransfer = new FileTransfer();
            fileTransfer.upload(imgurl, encodeURI("http://192.168.31.91:8000/api/faces/"), vueObject.upload_success, vueObject.upload_fail, fileUploadOptions);
            
            // fileTransfer.upload(imgurl, encodeURI("http://192.168.31.91:8000/api/face_post/"), vueObject.upload_success, vueObject.upload_fail, fileUploadOptions);
        },
        upload_success(r) {
            this.test = "file posted...";
            console.log(r)
            console.log("Code = " + r.responseCode);
            console.log("Response = " + r.response);
            console.log("Sent = " + r.bytesSent);

            var obj=JSON.parse(r.response)
            this.$store.commit("init",obj)
            this.$store.commit("endLoading");
            this.$router.push({name : 'result'});
        },

        upload_fail(error) {
            this.test = "file post fail...";
            this.test = error;
            this.$store.commit("endLoading");
            console.log("upload error source " + error.source);
            console.log("upload error target " + error.target);
        },
        setCameraOptions : function(srcType) {
            var options = {
                // Some common settings are 20, 50, and 100
                quality: 50,
                destinationType: Camera.DestinationType.FILE_URI,
                // In this app, dynamically set the picture source, Camera or photo gallery
                sourceType: srcType,
                encodingType: Camera.EncodingType.JPEG,
                mediaType: Camera.MediaType.PICTURE,
                allowEdit: true,
                correctOrientation: true  //Corrects Android orientation quirks
            }
            return options;
        }
    },
    mounted(){

        if( this.who == 'main'){
            this.iconColor = "white";
        }
    }
}
</script>
<style>
.p-30p{
    padding-top: 30%;
}
.p-50p{
    padding-top: 50%;
}
</style>