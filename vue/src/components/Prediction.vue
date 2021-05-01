<template>
    <div class = "prediction">
        <div class = "nav-bar container-fluid" ref = "navigation">
            <div class = "row text-center">
                <div class = "col-12"><a href = "/#about">RETURN TO HOME</a></div>
            </div>
        </div>
        <div class = "container-fluid">
            <div class ="row prediction-statement">
                <div class = "col-12 prediction-statement-text">
                    UPLOAD AN IMAGE HERE<br> TO IDENTIFY
                </div>
                <div class = "col-12">
                    <button class = "btn btn-primary upload-image-prediction" v-on:click="chooseFile">UPLOAD IMAGE</button>
                    <div style="height:0px;overflow:hidden">
                        <input type="file" id="fileInput" name="fileInput" @change="onFileChanged" ref='file' />
                    </div>
                </div>
            </div>
             <div class = "row">
                <div class = "col-12 prediction-img">
                    <img :src="prediction.url">
                </div>
            </div>
            <div class = "container-fluid result-title ">
                <div class = "row text-center result-text">RESULT:</div>
                <div class ="row prediction-result">{{prediction.result}}</div>
            </div>
            <div class = "menu-wrapper row">
                <div class = "menu-accordion">
                    <b-button class ="menu-button" v-b-toggle.collapse-2 variant="primary"><span>SYMPTOMS:</span></b-button>
                    <b-collapse id="collapse-2" class="mt-2">
                        <b-card class = "menu-collapse">
                            <div v-if="!isPredict" class = "not-predict">NO PREDICTION HAS BEEN MADE</div>
                            <div v-if="isPredict" class = "predict">{{prediction.symptoms}}</div>
                            <div v-if="isPredict=='error'" class = "predict-error">Error</div>
                        </b-card>
                    </b-collapse>
                    <b-button class ="menu-button" v-b-toggle.collapse-3 variant="primary"><span>CAUSES:</span></b-button>
                    <b-collapse id="collapse-3" class="mt-2">
                        <b-card class = "menu-collapse">
                            <div v-if="!isPredict" class = "not-predict">NO PREDICTION HAS BEEN MADE</div>
                            <div v-if="isPredict" class = "predict">{{prediction.causes}}</div>
                            <div  v-if="isPredict==null" class = "predict-error">Error</div>
                        </b-card>
                    </b-collapse>
                    <b-button class ="menu-button" v-b-toggle.collapse-4 variant="primary"><span>SOLUTIONS:</span></b-button>
                    <b-collapse id="collapse-4" class="mt-2">
                        <b-card class = "menu-collapse">
                            <div v-if="!isPredict" class = "not-predict">NO PREDICTION HAS BEEN MADE</div>
                            <div v-if="isPredict" class = "predict">{{prediction.solutions}}</div>
                            <div  v-if="isPredict==null" class = "predict-error">Error</div>
                        </b-card>
                    </b-collapse>
                </div>
            </div>
            <div class = "row visit-library">
                <div class = "col-12">
                    <a href = "/library">VISIT LIBRARY -></a>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: 'Prediction',
    data() {
        return {
             image: null,
             file: null,
             prediction: {
                 url: null,
                 result: null,
                 symptoms: null,
                 causes: null,
                 solutions: null
             },
             isPredict: false
        }
    },
    methods: {
        chooseFile: function() {
            document.getElementById("fileInput").click();
        },
        onFileChanged() {
            const formData = new FormData()
            this.file = this.$refs.file.files[0];
            formData.append("file", this.file)
            axios.post("http://127.0.0.1:5000/predict", formData,{
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(res => {
                this.prediction.url = res.data.image
                this.prediction.result = res.data.result.replace("_", " ")
                this.prediction.symptoms = res.data.symptoms
                this.prediction.causes = res.data.causes
                this.prediction.solutions = res.data.solutions
                this.isPredict = true
            })
            .catch(function(){
                this.isPredict = "error"
                console.log('FAILURE!!');
            })
        },
    },
    mounted() {
    }
}
</script>

<style scoped>
@font-face {
  font-family: Neue;
  src: url(~@/assets/NeueMachina-Regular.otf);
}

@font-face {
  font-family: Matahari;
  src: url(~@/assets/Matahari-400Regular.otf);
}

.prediction {
    background-color: white;
}

.container-fluid {
    width: 100%;
    margin: 0;
    padding: 0 !important;
}

.nav-bar {
    font-family: Neue;
    vertical-align: middle;
    text-align: center;
    color:white;
    font-size: 1.5rem;
    height: 8vh;
    background-color: white;
    border-bottom: 2px solid black;
    position: fixed;
    top:0;
    z-index: 2;
    margin: 0;
    padding: 0;
}

a {
    position: relative;
    color: black;
    top: 30%;
}

a:hover {
    color:#3449E1;;
}

.result-title {
    margin-top: 3%;
    text-align: center;
    font-size: 4rem;
    color: #3449E1;
    font-family: Neue;
}

.result-text {
    margin-left: 3%;
}

.prediction-statement {
    font-size: 4rem;
    color:#3449E1;
    text-align: center;
    font-family: Neue;
}

.prediction-statement-text {
    margin-top: 6rem;
}

.upload-image-prediction {
    font-size: 2rem;
    font-family: Neue;
    background-color: transparent;
    color:#3449E1;
    border: 2px solid #3449E1;
}

.prediction-result {
    font-size: 2.5rem;
    color:#3449E1;
    text-align: center;
    font-family: Neue;
    margin-left: 3%;
}

.menu-accordion {
    width: 100%;
}

.menu-button {
    display: block;
    font-size: 4rem;
    background-color: transparent;
    color: #3449E1;
    font-family: Neue;
    width: 100%;
    border-left: none;
    border-right: none;
    border-top: 2px solid black;
    box-shadow: none;
    text-align: left;
    border-color: black !important;
    padding: 0;
}

.menu-button span {
    margin-left: 4%;
}

.menu-collapse {
    font-size: 2rem;
    font-family: Matahari;
    color: black;
    text-align: left;
    border-top: none;
}

.menu-collapse div {
    margin-left: 2%;
}

.visit-library {
    font-size: 2.5rem;
    font-family: Neue;
    color: black;
    text-align: center;
    margin-top: 6%;
    padding-bottom: 6%;
}

.prediction-img {
    padding-top: 5%;
    max-width: 150%;
    border-radius: 50%;
    padding-bottom: 5%;
}

@media only screen and (max-width: 700px) {
    .prediction-statement-text {
        font-size: 3.5rem;
    }

    .result-text {
        font-size: 3.5rem;
    }

    .menu-button {
        font-size: 3.5rem;
    }

    .menu-collapse {
        font-size: 1.5rem;
    }
}

@media only screen and (max-width: 500px) {
    .prediction-statement-text {
        font-size: 3rem;
    }

    .result-text {
        font-size: 3rem;
    }

    .menu-button {
        font-size: 3rem;
    }

    .menu-collapse {
        font-size: 1rem;
    }

    .prediction-statement {
        padding-bottom: 6rem;
    }
}

@media only screen and (max-width: 400px) {
    .prediction-statement-text {
        font-size: 2.5rem;
    }

    .result-text {
        font-size: 2.5rem;
    }

    .menu-button {
        font-size: 2.5rem;
    }

    .menu-collapse {
        font-size: 1rem;
    }

    .prediction-statement {
        padding-bottom: 6rem;
    }
}

</style>
