let menuParent = document.querySelector('.menu-parent') 
let subMenu = document.querySelector('.sub-menu'); 

menuParent.addEventListener('click', ()=>{
    if (subMenu.style.display == 'none') {
        subMenu.style.display = 'block';
    } else {
        subMenu.style.display = 'none';
    }
})
