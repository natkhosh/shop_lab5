<script>

    import { onMount, onDestroy } from 'svelte';
    import Cookies from 'js-cookie/src/js.cookie.js'

   let food = [];

    const CSRF_TOKEN = Cookies.get('csrftoken');
    const WISHLIST_URL = getRef("wishlist-ref");

    function getRef(id) {return document.getElementById(id).href;};

    onMount(async () => {
       const response = await fetch(WISHLIST_URL, {
                                     headers: {
                                        'Accept': 'application/json, text-plain, */*',
                                        'X-Requested-With': 'XMLHttpRequest',
                                     }, });

       let food_json = await response.json();
        food = food_json['food']
        food = food
       console.log(food)
   });

</script>

<main>
    
<table class="table">
    <thead class="thead-primary">
      <tr class="text-center">
        <th>&nbsp;</th>
        <th>Product List</th>
        <th>&nbsp;</th>
        <th>Price</th>
        <th>Quantity</th>
        <th>Total</th>
      </tr>
    </thead>
    <tbody >
    
        {#each food as item }
          <tr class="text-center">
            <td class="product-remove"><a href="."><span class="ion-ios-close"></span></a></td>						        
            <td class="image-prod"><div class="img" style="background-image:url({item.img});"></div></td>						        
            <td class="product-name">
                <h3>{item.title}</h3>
                <p>{item.description}</p>
            </td>						        
            <td class="price">{item.currency}{item.price}</td>						        
            <td class="quantity">
                <div class="input-group mb-3">
                <input type="number" name="quantity" class="quantity form-control input-number" bind:value={item.quantity} min=1 max=100>
            </div>
          </td>						        
            <td class="total">{item.currency}{item.quantity*item.price}</td>
          </tr><!-- END TR-->
        {/each}

    </tbody>
  </table>


</main>

<style>

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>