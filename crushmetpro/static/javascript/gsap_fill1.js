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

// pop.from(".fill .left .l_hd, .fill .left .d_input, .fill .left .btn1, .fill .right .logo img, .linebar .cubes .cube1, .linebar .cubes .cube2, .linebar .cubes .cube3,", {
//     duration: .5,
//     opacity: 0,
//     y: 25,
//     stagger: {
//         amount: 1
//     }
// },"-=.3")

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