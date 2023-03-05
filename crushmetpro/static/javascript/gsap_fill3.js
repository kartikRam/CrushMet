const pop = gsap.timeline({
  paused: "true"
})

pop.to(".fill",{
  duration:  1,
  opacity: 1,
  y: -50,
  scale:1,
  ease: Power4.easeOut
})

pop.from(".fill .left .logo .l_img, .fill .left .logo .c_img, .fill .right h2, .fill .right h3, .fill .right form .d_input, .fill .fg, .fill .btn1, .fill .btn2, .fill .btn3,.fill .close_btn", {
  duration: .5,
  opacity: 0,
  y: 25,
  stagger: {
      amount: 1
  }
},"-=.3")

pop.play();
// function pop_close()
// {
//     pop.reverse();
//     var interval = setInterval(myURL, 3000);
//     var result = document.getElementById("result");
// }
// function myURL() {
//     document.location.href = 'login.html';
//     clearInterval(interval);
//  }