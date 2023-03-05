const pop = gsap.timeline({
    paused: "true"
})

pop.to(".login",{
    duration:  1,
    opacity: 1,
    y: -50,
    scale:1,
    ease: Power4.easeOut
})

pop.from(".login .left .logo .l_img, .login .left .logo .c_img, .login .right h2, .login .right h3, .login .right form .d_input, .login .fg, .login .btn1, .login .btn2, .login .btn3,.login .close_btn", {
    duration: .5,
    opacity: 0,
    y: 25,
    stagger: {
        amount: 1
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