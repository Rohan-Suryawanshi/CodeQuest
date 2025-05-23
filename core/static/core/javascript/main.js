const circle = document.querySelector(".circle");
function mouseMove(e) {
   gsap.to(circle, {
      x: e.x, // Set the x position to the mouse x
      y: e.y, // Set the y position to the mouse y
      duration: 0.8, // Animation duration for smooth effect
      ease: "power2.out", // Easing function for a smooth transition
   });
   console.log(e.x, e.y);
}

gsap.from(".navigation_bar a", {
   opacity: 0,
   y: -20,
   duration: 1,
   stagger: 0.2,
   ease: "power2.out",
});

document.addEventListener("mousemove", mouseMove);
