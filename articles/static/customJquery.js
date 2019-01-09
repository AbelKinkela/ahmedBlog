// $(window).on('scroll', function (event) {
//     var scrollValue = $(window).scrollTop();
//     if (scrollValue > 120) {
//         $('.navbar').addClass('affix');
//     } else {
//         $('.navbar').removeClass('affix');
//     }
// });

// $(window).on('scroll', function (event) {
//     var scrollValue = $(window).scrollTop();
//     if (scrollValue == settings.scrollTopPx || scrollValue > 70) {
//         $('.navbar').addClass('fixed-top');
//     }
// });


$(document).ready(function () {

    var toggleAffix = function (affixElement, scrollElement, wrapper) {

        var height = affixElement.outerHeight(),
            top = wrapper.offset().top;

        if (scrollElement.scrollTop() >= top) {
            wrapper.height(height);
            affixElement.addClass("affix");
        }
        else {
            affixElement.removeClass("affix");
            wrapper.height('auto');
        }

    };


    $('[data-toggle="affix"]').each(function () {
        var ele = $(this),
            wrapper = $('<div></div>');

        ele.before(wrapper);
        $(window).on('scroll resize', function () {
            toggleAffix(ele, $(this), wrapper);
        });

        // init
        toggleAffix(ele, $(window), wrapper);
    });

});