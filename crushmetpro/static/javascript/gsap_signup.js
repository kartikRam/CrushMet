const pop = gsap.timeline({
    paused: "true"
})
pop.to(".signup",{
    duration:  1.2,
    opacity: 1,
    y: 0,
    scale:1,
    ease: Power4.easeOut
})  


pop.from(".signup .right h2, .signup .right h3, .signup .right form .d_input, .signup .right form a, .signup .right form .btn1, .signup .right form .btn2, .signup .left .logo img, .signup .left .img img, .signup .close_btn", {
    duration: .7,
    opacity: 0,
    y: 25,
    stagger: {
        amount: 0.8
    }
},"-=.3")

pop.play();
function pop_close()
{
    pop.reverse();
    var interval = setInterval(myURL, 3000);
    var result = document.getElementById("result");
}
function myURL() {
    document.location.href = 'login.html';
    clearInterval(interval);
 }