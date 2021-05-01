<template>
    <div class = "library">
         <div class = "nav-bar container-fluid" ref = "navigation">
            <div class = "row text-center">
                <div class = "col-12"><a href = "/#about">RETURN TO HOME</a></div>
            </div>
        </div>
        <div class = "container-fluid library-main">
            <div class = "library-title row">
                <span>LIBRARY</span>
            </div>
            <div class = "row library-members" v-for="(disease,index) in diseases" :key="disease">
                <div class = "library-child col-12">
                    <a  v-bind:href="'/library/'+ disease">{{index + 1}}. {{disease}}</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import  axios from 'axios'
export default {
    name: "Library",
    data() {
        return {
            diseases: [
            ]
        }
    }, 
    methods: {
        getDisease() {
            axios.get("http://127.0.0.1:5000/predict")
            .then(res => {
                for(var i = 0; i < res.data.diseases.length; i++){
                    this.diseases.push(res.data.diseases[i]);
                }
            })
        }
    },
    mounted() {
        this.getDisease()
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
    color:#E8C31D;
}

.library {
    margin-top: 5%;
}

.container-fluid {
    width: 100%;
    margin: 0;
    font-family: Neue;
    color: black;
}

.library-main {
    height: 100vh;
}

.library-title {
    color: #E8C31D;
    font-size: 6rem;
    margin-left: 4%;
    padding-bottom: 3rem;
}

.library-title span {
    margin-top: 4rem;
}

.library-members {
    color: black;
    font-size: 2.5rem;
    text-align: left;
    padding-bottom: 4rem;
    padding-top: 2rem;
    border-top: 2px solid black;
    white-space: nowrap;
}

.library-members a {
    margin-left: 4%;
}

@media only screen and (max-width: 1114px) {
    .library-members {
        font-size: 2rem;
    }
}

@media only screen and (max-width: 890px) {
    .library-members {
        font-size: 1.5rem;
    }

    #app {
        overflow-x: auto !important;
    }

}

@media only screen and (max-width: 500px) {
    .library-title {
        margin-top: 10%;
        font-size: 4rem;
    }

    .library-members {
        font-size: 1.2rem;
    }

}

@media only screen and (max-width: 400px) {
    .library-title {
        margin-top: 10%;
        font-size: 4rem;
    }

    .library-members {
        font-size: 1rem;
    }

}
</style>