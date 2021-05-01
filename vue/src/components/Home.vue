<template>
  <div class="home">
    <div class = "menu-wrapper" ref = "menu">
        <div class = "menu-accordion">
            <b-button class ="menu-button" v-b-toggle.collapse-1 variant="primary">MENU</b-button>
            <b-collapse id="collapse-1" class="mt-2">
                <b-card class = "menu-collapse">
                    <a href = "#about" >01. ABOUT</a>
                    <a href = "#use-it">02. USE IT</a>
                    <a href = "#features">03. FEATURES</a>
                    <a href = "#why">04. WHY</a>
                    <a href ="#effects">05. EFFECTS</a>
                    <a href ="#updates">06. UPDATES</a>
                </b-card>
            </b-collapse>
        </div>
    </div>
    <div class = "nav-bar container-fluid" ref = "navigation">
        <div class = "row text-center">
            <div class = "col-2"><a href = "#about">ABOUT</a></div>
            <div class = "col-2"><a href = "#use-it">USE IT</a></div>
            <div class = "col-2"><a href = "#features">FEATURES</a></div>
            <div class = "col-2"><a href = "#why">WHY</a></div>
            <div class = "col-2"><a href = "#effects">EFFECTS</a></div>
            <div class = "col-2"><a href = "#updates">UPDATES</a></div>
        </div>
    </div>
    <div class = "container-fluid">
        <div class = "product home row" id = "about">
            <div class = "col-12">
                <p><span class = "plant-vision">PLANT VISION</span> IS A WEB APP THAT USES AI TO DETECT PLANT DISEASES FROM IMAGES.</p>
            </div>
             <div class = "col-12 identify">
                <p><span class = "plant-vision">IDENTIFY</span><br>PLANT DISEASES<br>WITH JUST ONE CLICK NOW!</p>
                <button class = "btn btn-primary upload-image-btn-home" v-on:click="direct">GO TO IDENTIFICATION</button>
                    <div style="height:0px;overflow:hidden">
                        <input type="file" id="fileInput" name="fileInput" @change="onFileChanged" ref='file' />
                    </div>
            </div>
            <div class = "col-12 visit-library">
                <a href = "/library">VISIT LIBRARY -></a>
            </div>
        </div>
        <div class = "product use-it row" id ="use-it">
            <div class = "use-it col-12 col-md-6">
                <span class = "use-it-title-1">SIMPLE. FAST.<br>UPLOAD<br>AN IMAGE NOW!</span>
                <button class = "btn btn-primary upload-image-btn-use-it" v-on:click="direct">GO TO IDENTIFICATION</button>
                <div style="height:0px;overflow:hidden">
                    <input type="file" id="fileInput" name="fileInput">
                </div>
                <div class = "col-12 visit-library">
                    <a href = "/library">VISIT LIBRARY -></a>
                </div>
            </div>
             <div class = "use-it col-12 col-md-6">
                <span class = "use-it-title-2">TAKE A CLOSEUP OF<br>THE DISEASED LEAF<br>LIKE THIS!</span>
                <img src = "@/assets/tomato.png">
                <span class = "img-title">Tomato__Septoria__Leaf__Spot</span>
             </div>
        </div>
        <div class = "product features row" id ="features">
            <div class = "row col-12 features-title">FEATURES</div>
            <div class = "row col-12 features-details"><span>01. FAST DETECION OF PLANTS FROM IMAGES.</span></div>
            <div class = "row col-12 features-details"><span>02. PROVIDE EARLY DETECTION, SYMPTOMS, CURING METHODS, AND RELATED CONTENT FOR EACH DISEASE.</span></div>
            <div class = "row col-12 features-details"><span>03. INCLUDE MORE THAN 10 TYPES OF DISEASES SPANNING 3 PLANT SPECIES: Tomato, Pepper Bell, Potato</span></div>
            <div class = "row col-12 features-details"><span>04. SCALABLE AND LIGHTWEIGHT AI git</span></div>
        </div>
         <div class = "product home row">
            <div class = "col-12">
                <p><span class = "plant-vision-why" id = "why">WHY PLANT VISION?</span><br>
                <span class = "plant-vision-explain">CROPS DISEASES POSE MAJOR THREATS TO AGRICULTURE, AFFECTING CROP YIELDS AND SLOWING DOWN FARMERS' EFFICIENCY. HOWEVER, DETECTION METHODS LARGELY STILL REMAIN SLOW AND INEFFECTIVE DUE TO LACK OF INFRASTUCTURE AND ACCESS TO KNOWLEDGE. <span class = "plant-vision">PLANT VISION</span> PUTS THE ABILITY TO DETECT PLANT DISEASES RAPIDLY AT THE HANDS OF FARMERS, RESEARCHERS AND MANY MORE TO DIAGNOSE AND PROTECT PLANTS' WELLBEING PROMPTLY AND EFFICIENTLY.</span></p>
            </div>
             <div class = "col-12 identify">
                <p><span class = "plant-vision">IDENTIFY</span><br>PLANT DISEASES<br>WITH JUST ONE CLICK NOW!</p>
                <button class = "btn btn-primary upload-image-btn-home" v-on:click="direct">GO TO IDENTIFICATION</button>
                    <div style="height:0px;overflow:hidden">
                        <input type="file" id="fileInput" name="fileInput" @change="onFileChanged" ref='file' />
                    </div>
            </div>
              <div class = "col-12 visit-library">
                    <a href = "/library">VISIT LIBRARY -></a>
                </div>
        </div>
        <div class = "product row effects" id ="effects">
            <div class = "row col-12 effects-title">EFFECTS</div>
            <div class = "row col-12 effects-details"><span>01. HELP FARMERS DETECT PLANT DISEASES FOR BETTER PROTECTION OF OTHER PLANTS AND MORE EFFICIENT FARM-MONITORING</span></div>
            <div class = "row col-12 effects-details"><span>02. A RESEARCH TOOL FOR SCIENTISTS TO EXAMINE PLANT DISEASES.</span></div>
            <div class = "row col-12 effects-details"><span>03. A LEARNING TOOL FOR STUDENTS TO STUDY ABOUT PLANT DISEASES</span></div>
            <div class = "row col-12 effects-details"><span>04. PROVIDE DETAILS AND SOLUTIONS TO IMPROVE PLANTS' WELLBEING</span></div>
        </div>
        <div class = "product row updates" id = "updates">
            <div class = "col-12 col-md-4 updates-title">FUTURE UPDATES</div>
            <div class = "col-12 col-md-8">
                <div class = "visit-github">VISIT MY <a href = "">GITHUB</a> FOR MORE INFO ABOUT PLANT VISION</div>
                <div class = "upcoming">UPCOMING UPDATES:
                    <div>01. EXPAND CAPABILITY OF AI MODEL TO MORE SPECIES AND DISEASES</div>
                    <div>02. INCORPORATE USERS' LOGIN FEATURES</div>
                    <div>03. INCLUDE DETECTION HISTORY FOR EACH USER</div>
                    <div>04. INTEGRATE CHATBOT FOR PERSONALIZED HELP</div>
                    <div>05. ORDER PESTICIDES TO DEAL WITH EACH PLANT DISEASE</div>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Home',
    data() {
        return {
             image: null,
             file: null
        }
    },
    methods: {
        chooseFile: function() {
            document.getElementById("fileInput").click();
        },
        direct: function() {
            window.location.href = "/prediction"
        },
        myEventHandler() {
            if(window.innerWidth <= 900) {
                this.$refs.navigation.style.display = "none"
                this.$refs.menu.style.display = ""
            }
            else {
                this.$refs.navigation.style.display = ""
                this.$refs.menu.style.display = "none"
            }
        },
        onFileChanged() {
            // const reader = new FileReader()
            // this.file = event.target.files[0]
            // reader.readAsDataURL(this.file)
            // reader.onload = e => {
            //     this.image = e.target.result
            //     axios.post("http://127.0.0.1:5000/predict", this.image)
            // }
            const formData = new FormData()
            this.file = this.$refs.file.files[0];
            formData.append("file", this.file)
            axios.post("http://127.0.0.1:5000/predict", formData,{
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(function(){
                console.log('SUCCESS!!');
            })
            .catch(function(){
                console.log('FAILURE!!');
            })
        },
    },
    mounted() {
        window.addEventListener("load", this.myEventHandler);
        window.addEventListener("resize", this.myEventHandler);
    },
    destroyed() {
        window.removeEventListener("load", this.myEventHandler);
        window.removeEventListener("resize", this.myEventHandler);
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@font-face {
  font-family: Neue;
  src: url(~@/assets/NeueMachina-Regular.otf);
}

@font-face {
  font-family: Matahari;
  src: url(~@/assets/Matahari-400Regular.otf);
}

.container-fluid {
    width: 100%;
    margin: 0;
    padding: 0 !important;
}

.nav-bar {
    font-family: Matahari;
    vertical-align: middle;
    text-align: center;
    color:black;
    font-size: 1.5rem;
    height: 8vh;
    background-color: white;
    border-bottom: 1px solid black;
    position: fixed;
    top:0;
    z-index: 2;
    margin: 0;
    padding: 0;
}

a {
    color: black;
    position: relative;
    top: 30%;
    transition: all 0.5s ease;
}

a:hover {
    color:#D92121;

}

.menu-accordion {
    border-bottom: 1px solid white;
    background-color: black;
    text-align: left;
}

.menu-button {
    background-color: transparent;
    border: none;
    font-family: Matahari;
    letter-spacing: 5px;
    font-size: 2rem;
    margin-left: 1.3%;
}

.menu-button:focus {
    border:none;
    background-color: transparent;
    box-shadow: none;
}

.menu-button:active {
    background-color: transparent !important;
    box-shadow: none;
}

.btn-primary:not(:disabled):not(.disabled):active:focus, .btn-primary:not(:disabled):not(.disabled).active:focus, .show > .btn-primary.dropdown-toggle:focus {
    box-shadow: none;
}

.menu-button:hover {
    background-color: black;
}

.menu-collapse {
    background-color: black;
    border-top: 1px solid white;
    border-right: none;
    border-bottom: none;
    border-radius: 0%;
}

.menu-collapse a {
    color: white !important;
    font-size: 1.5rem;
    display: block;

}

.product {
    padding: 0 !important;
    margin:0;
    overflow: hidden;
}

.home {
    background-color: white;
    border-bottom: 1px solid black;
    font-family: Neue;
    font-size: 4.5rem;
}

.plant-vision {
    color: #20604F;
    text-decoration-color:#20604F;
    text-decoration: underline;
}

.home p {
    margin-top: 15%;
}

.identify {
    margin-top: 0%;
    padding-bottom: 10%;
}

.upload-image-btn-home {
    background-color: transparent;
    font-size: 2.5rem;
    border-color: transparent;
    border: 1.5px solid #20604F;
    color: #20604F;
}

.upload-image-btn-home:hover {
    background-color:#20604F;
    color: white;
}

.features {
    background-color: white;
    display: flex;
    padding-bottom: 5% !important;
    border-bottom: 1.5px solid black;
}

.features-title {
    border-bottom: 1px solid white;
    font-family: Neue;
    justify-content: center;
    font-size: 7rem;
    letter-spacing: 2px;
    color: #D92121;
    margin: 0;
    margin-top: 8%;
    padding-bottom: 5% !important;
}

.features-details {
    width: 100%;
    border-bottom: 1px solid white;
    font-family: Matahari;
    font-size: 2.2rem;
    transition: all 0.5s ease;
    padding-bottom: 4%;
    margin: 0;
    text-align: left;
}


.features-details span {
    padding-left: 3%;
    padding-top: 4%;
}


.plant-vision-why {
    color: #B59BC9;
    text-decoration-color:#20604F;
    text-decoration: underline;
}

.plant-vision-explain {
    font-size: 2rem;
    line-height: 0;
}

.how {
    background-color: #B59BC9;
    color: #3449E1;
    border-bottom: 1px solid white;
    margin: 0;
}

.product-how-title {
    border-right: 1px solid white;
    padding-bottom: 8%;
}


.how-title {
    margin-top: 20%;
    font-size: 7rem;
    text-align: left;
    font-family: Neue;
    margin-left: 3%;
}

.how-description {
    font-size: 3.5rem;
    font-family: Matahari;
    margin-left: 3%;
    text-align: left;
    color: white;
}

.upload-image-btn-how {
    margin-top:5%;
    background-color: white;
    font-size: 2.2rem;
    font-family: Neue;
    float: left;
    margin-left: 3%;
    color: #3449E1;
    border: 5px;
}

.use-it {
    background-color: white;
    font-family: Neue;
    border-bottom: 1px solid black;
}

.use-it-title-1 {
    display: block;
    color: black;
    font-size: 4rem;
    text-align: center;
    margin-top: 28%;
}

.use-it-title-2 {
    margin-top: 5%;
    display: block;
    color: black;
    font-size: 4rem;
    text-align: center;
    padding-bottom: 6%;
}

.use-it img {
    max-width: 100%;
    border-radius: 50%;
    border: 2px solid black;
}

.img-title {
    margin-top: 5%;
    color:#3449E1;
    font-size: 2rem;
    font-family: Neue;
    display: block;
    padding-bottom: 10%;
}

.upload-image-btn-use-it {
    margin-top: 5%;
    font-size: 2.2rem;
    font-family: Neue;
    color: #3449E1;
    background-color: transparent;
    margin-bottom: 10%;
}


.effects {
    background-color: white;
    color: #E8C31D;
    border-bottom: 1.5px solid black;;
}

.effects-title {
    color: #E8C31D;
    border-bottom: 1px solid white;
    font-family: Neue;
    justify-content: center;
    font-size: 7rem;
    letter-spacing: 2px;
    margin: 0;
}

.effects-details {
    width: 100%;
    border-bottom: 1px solid white;
    font-family: Matahari;
    font-size: 2.2rem;
    transition: all 0.5s ease;
    padding-bottom: 4%;
    margin: 0;
    text-align: left;
    color: black;
}

.effects-details:hover {
    background-color:#E8C31D;
    color:black;
}

.effects-details span {
    padding-top: 5%;
    padding-left: 3%;
}

.updates {
    font-family: Neue;
    border-bottom: 1px solid black;
}

.updates-title {
    text-align: left;
    font-size: 5rem;
    padding-top: 25%;
    padding-right: 3%;
    border-right: 1px solid black;
}

.visit-github {
    text-align: right;
    margin-top: 6%;
    font-size: 3.5rem;
}

.visit-github a {
    color:#3449E1;
}

.visit-library {
    font-size: 2.5rem;
    font-family: Neue;
    color: black;
    text-align: center;
    margin-top: 6%;
    padding-bottom: 6%;
}

.visit-library a {
    top: 0%;
}

.upcoming {
    margin-top: 6%;
    text-align: right;
    font-size: 4rem;
    color:brown;
    padding-bottom: 3%;
}

.upcoming div {
    border-top: 1px solid black;
    text-align: right;
    font-size: 2rem;
    color: black;
    padding-top: 3%;
    padding-bottom: 3%;
    margin:0;
    transition: all 0.5s ease;
}

.upcoming div:hover {
    background-color: black;
    color: brown;
}

@media only screen and (max-width:1100px) {
    .updates-title {
        font-size: 4.5rem;
        padding-top: 15%;
    }
}

@media only screen and (max-width: 1000px) {
    
}

@media only screen and (max-width: 777px) {
    .product-statement {
        padding-bottom: 0% !important;
    }

    .use-it-title-1 {
        margin-top: 10%;
    }
}

@media only screen and (max-width: 700px) {
    .home {
        font-size: 4rem;
    }

    .plant-vision-explain {
        font-size: 2rem;
    }
}

@media only screen and (max-width: 600px) {
    .home {
        font-size: 3rem;
    }

    .use-it-title-2 {
        font-size: 3rem;
    }

    .img-title {
        font-size: 1.5rem;
    }

    .features-title {
        font-size: 4rem;
    }

    .features-details {
        font-size: 1.5rem;
    }

    .plant-vision-explain {
        font-size: 1.5rem;
    }

    .effects-title {
        font-size: 4rem;
    }

    .effects-details {
        font-size: 1.5rem;
    }

    .updates-title {
        font-size: 4rem;
    }

    .visit-github {
        font-size: 2rem;
    }

    .upcoming div {
        font-size: 1.5rem;
    }

    .btn-primary {
        font-size: 1.5rem !important;
    }
}

@media only screen and (max-width: 400px) {
    .home {
        font-size: 2rem;
    }

    .use-it-title-2 {
        font-size: 2rem;
    }

    .img-title {
        font-size: 1rem;
    }

    .features-title {
        font-size: 3.5rem;
    }

    .features-details {
        font-size: 1rem;
    }

    .plant-vision-explain {
        font-size: 1rem;
    }

    .effects-title {
        font-size: 3.5rem;
    }

    .effects-details {
        font-size: 1rem;
    }

    .updates-title {
        font-size: 3.5rem;
    }

    .visit-github {
        font-size: 1.5rem;
    }

    .upcoming div {
        font-size: 1rem;
    }

    .btn-primary {
        font-size: 1rem !important;
    }
}


</style>
