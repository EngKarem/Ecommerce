<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to our Watches Store
            </p>
            <p class="subtitle">
                The best place to buy your suitable watch
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

     <ProductBox 
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />    

    </div>
    <footer class="footer-distributed">

			<div class="footer-left">

				<h3>important<span>Links</span></h3>

				<p class="footer-links">
					<a href="http://localhost:8080/summer">Classic</a>
					·
					<a href="http://localhost:8080/winter">Smart</a>
					·
					<a href="http://localhost:8080/log-in">Log In</a>
					·
					<a href="http://localhost:8080/cart">Cart</a>
				</p>

			

				<div class="footer-icons">
         <h3>social<span>Links</span></h3>

					<a href="#"><i class="fa-brands fa-facebook"></i></a>
					<a href="#"><i class="fa-brands fa-twitter"></i></a>
					<a href="#"><i class="fa-brands fa-linkedin"></i></a>
					<a href="#"><i class="fa-brands fa-github"></i></a>

				</div>

			</div>

			<div class="footer-right">

				<p>Contact Us</p>

				<form action="#" method="post">

					<input type="text" name="email" placeholder="Email">
					<textarea name="message" placeholder="Message"></textarea>
					<button>Send</button>

				</form>

			</div>

		</footer>
   
  </div>
  
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'
export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()
    document.title = 'HomePage' + ' : Great Watches'
  },
  methods: {
      getLatestProducts() {
        axios
          .get('/api/v1/latest-product/')
          .then(response => {
            this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
<style scoped>

  * {
  font-family: Roboto;
}

.footer-distributed{
	background: #444;
	box-shadow: 0 1px 1px 0 rgba(231, 11, 11, 0.12);
	box-sizing: border-box;
	width: 100%;
	font: bold 16px sans-serif;
	text-align: left;
	padding: 50px 60px 40px;
	overflow: hidden;
}





.footer-distributed .footer-left{
	float: left;
}



.footer-distributed h3{
	color:  #ffffff;
	font: normal 36px 'Roboto', cursive;
	margin: 0 0 10px;
}

.footer-distributed h3 span{
	color:  #5383d3;
}



.footer-distributed .footer-links{
	color:  #ffffff;
	margin: 0 0 10px;
	padding: 0;
}

.footer-distributed .footer-links a{
	display:inline-block;
	line-height: 1.8;
	text-decoration: none;
	color:  inherit;
}



.footer-distributed .footer-icons{
	margin-top: 40px;
  
}





.footer-distributed .footer-icons a{
	display: inline-block;
	width: 35px;
	height: 35px;
	cursor: pointer;
	background-color:  #33383b;
	border-radius: 2px;

	font-size: 20px;
	color: #ffffff;
	text-align: center;
	line-height: 35px;

	margin-right: 3px;
	margin-bottom: 5px;
}

.footer-distributed .footer-right{
	float: right;
}

.footer-distributed .footer-right p{
	display: inline-block;
	vertical-align: top;
	margin: 15px 42px 0 0;
	color: #ffffff;
}



.footer-distributed form{
	display: inline-block;
}

.footer-distributed form input,
.footer-distributed form textarea{
	display: block;
	border-radius: 3px;
	box-sizing: border-box;
	background-color:  #1f2022;
	box-shadow: 0 1px 0 0 rgba(255, 255, 255, 0.1);
	border: none;
	resize: none;

	font: inherit;
	font-size: 14px;
	font-weight: normal;
	color:  #d1d2d2;

	width: 400px;
	padding: 18px;
}

.footer-distributed ::-webkit-input-placeholder {
	color:  #5c666b;
}

.footer-distributed ::-moz-placeholder {
	color:  #5c666b;
	opacity: 1;
}

.footer-distributed :-ms-input-placeholder{
	color:  #5c666b;
}


.footer-distributed form input{
	height: 55px;
	margin-bottom: 15px;
}

.footer-distributed form textarea{
	height: 100px;
	margin-bottom: 20px;
}

.footer-distributed form button{
	border-radius: 3px;
	background-color:  #33383b;
	color: #ffffff;
	border: 0;
	padding: 15px 50px;
	font-weight: bold;
	float: right;
}


@media (max-width: 1000px) {

	.footer-distributed {
		font: bold 14px sans-serif;
	}


	.footer-distributed form input,
	.footer-distributed form textarea{
		width: 250px;
	}

	.footer-distributed form button{
		padding: 10px 35px;
	}

}

@media (max-width: 800px) {

	.footer-distributed{
		padding: 30px;
	}

	.footer-distributed .footer-left,
	.footer-distributed .footer-right{
		float: none;
		max-width: 300px;
		margin: 0 auto;
	}

	.footer-distributed .footer-left{
		margin-bottom: 40px;
	}

	.footer-distributed form{
		margin-top: 30px;
	}

	.footer-distributed form{
		display: block;
	}

	
}

</style>