

export let  cart = JSON.parse(localStorage.getItem('cart'));
if (cart === null) {
    cart = [];
}


function cartLocale() {
    localStorage.setItem('cart', JSON.stringify(cart));
};


export function cartupdate(productId) {
    let matchingItem;
        
    cart.forEach((cartItem) => {
        if(productId === cartItem.productId) {
            matchingItem = cartItem
        }
        


    });
    if (matchingItem) {
        matchingItem.quantity +=1;
    } else {
        cart.push(
            {
            productId:productId, quantity:1
        });
    };
    cartLocale() 
};
export function removeFromCart(productId) {
    let newCart = [];
    cart.forEach((cartItem) => {
        if (cartItem.productId !== productId) {
            newCart.push(cartItem);
        }

    });

    
    cart = newCart;
    //console.log(cart);
    cartLocale();
}