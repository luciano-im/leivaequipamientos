$(document).ready(function() {

    /*######## SLIDERS #######*/
    
    //$('#slider_crs').carouFredSel();

    $('#slider_crs').carouFredSel({
        align: "center",
        auto: true,
        circular: true,
        items: 1,
        direction: "left",
        /*swipe: {
            onMouse: true,
            onTouch: true
        },*/
        scroll: 1000,
        pagination: {
            container: '#slider_crs_pag',
            anchorBuilder: false
        }
    });
  
});