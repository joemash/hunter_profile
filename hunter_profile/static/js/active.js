(function ($) {
    'use strict';

    if ($.fn.owlCarousel) {
        // :: 1.0 Welcome Post Slider Active Code
        $(".welcome-post-sliders").owlCarousel({
            items: 4,
            loop: true,
            autoplay: true,
            smartSpeed: 1500,
            margin: 10,
            nav: true,
            navText: ['', ''],
            responsive: {
                320: {
                    items: 1
                },
                576: {
                    items: 2
                },
                992: {
                    items: 3
                },
                1200: {
                    items: 4
                }
            }
        })
        // :: 2.0 Instagram Slider Active Code
        $(".instargram_area").owlCarousel({
            items: 6,
            loop: true,
            autoplay: true,
            smartSpeed: 800,
            nav: true,
            navText: ['', ''],
            responsive: {
                320: {
                    items: 1
                },
                480: {
                    items: 2
                },
                576: {
                    items: 3
                },
                768: {
                    items: 4
                },
                992: {
                    items: 5
                },
                1200: {
                    items: 6
                }
            }
        })
        
    }

    // :: 4.0 ScrollUp Active JS
    if ($.fn.scrollUp) {
        $.scrollUp({
            scrollSpeed: 1500,
            scrollText: '<i class="fa fa-arrow-up" aria-hidden="true"></i>'
        });
    }

    // :: 5.0 CounterUp Active JS
    if ($.fn.counterUp) {
        $('.counter').counterUp({
            delay: 10,
            time: 2000
        });
    }

    // :: 6.0 PreventDefault a Click
    $("a[href='#']").on('click', function ($) {
        $.preventDefault();
    });

    // :: 7.0 Search Form Active Code
    $(".searchBtn").on('click', function () {
        $(".search-hidden-form").toggleClass("search-form-open");
    });

    // :: 8.0 Search Form Active Code
    $("#pattern-switcher").on('click', function () {
        $("body").toggleClass("bg-pattern");
    });
    $("#patter-close").on('click', function () {
        $(this).hide("slow");
        $("#pattern-switcher").addClass("pattern-remove");
    });

    // :: 9.0 wow Active Code
    if ($.fn.init) {
        new WOW().init();
    }

    // :: 10.0 matchHeight Active JS
    if ($.fn.matchHeight) {
        $('.item').matchHeight();
    }

    var $window = $(window);

    // :: 11.0 Preloader active code
    $window.on('load', function () {
        $('#preloader').fadeOut('slow', function () {
            $(this).remove();
        });
    });

  //cube portfolio
  var gridContainer = $('#grid-container'),
    filtersContainer = $('#filters-container');

  // init cubeportfolio
  gridContainer.cubeportfolio({

    defaultFilter: '*',

    animationType: 'flipOutDelay',

    gapHorizontal: 45,

    gapVertical: 30,

    gridAdjustment: 'responsive',

    caption: 'overlayBottomReveal',

    displayType: 'lazyLoading',

    displayTypeSpeed: 100,

    // lightbox
    lightboxDelegate: '.cbp-lightbox',
    lightboxGallery: true,
    lightboxTitleSrc: 'data-title',
    lightboxShowCounter: true

  });

  // add listener for filters click
  filtersContainer.on('click', '.cbp-filter-item', function(e) {

    var me = $(this),
      wrap;

    // get cubeportfolio data and check if is still animating (reposition) the items.
    if (!$.data(gridContainer[0], 'cubeportfolio').isAnimating) {

      if (filtersContainer.hasClass('cbp-l-filters-dropdown')) {
        wrap = $('.cbp-l-filters-dropdownWrap');

        wrap.find('.cbp-filter-item').removeClass('cbp-filter-item-active');

        wrap.find('.cbp-l-filters-dropdownHeader').text(me.text());

        me.addClass('cbp-filter-item-active');
      } else {
        me.addClass('cbp-filter-item-active').siblings().removeClass('cbp-filter-item-active');
      }

    }

    // filter the items
    gridContainer.cubeportfolio('filter', me.data('filter'), function() {});

  });

  // activate counters
  gridContainer.cubeportfolio('showCounter', filtersContainer.find('.cbp-filter-item'));


  // add listener for load more click
  $('.cbp-l-loadMore-button-link').on('click', function(e) {

    e.preventDefault();

    var clicks, me = $(this),
      oMsg;

    if (me.hasClass('cbp-l-loadMore-button-stop')) return;

    // get the number of times the loadMore link has been clicked
    clicks = $.data(this, 'numberOfClicks');
    clicks = (clicks) ? ++clicks : 1;
    $.data(this, 'numberOfClicks', clicks);

    // set loading status
    oMsg = me.text();
    me.text('LOADING...');

    // perform ajax request
    $.ajax({
        url: me.attr('href'),
        type: 'GET',
        dataType: 'HTML'
      })
      .done(function(result) {
        var items, itemsNext;

        // find current container
        items = $(result).filter(function() {
          return $(this).is('div' + '.cbp-loadMore-block' + clicks);
        });

        gridContainer.cubeportfolio('appendItems', items.html(),
          function() {
            // put the original message back
            me.text(oMsg);

            // check if we have more works
            itemsNext = $(result).filter(function() {
              return $(this).is('div' + '.cbp-loadMore-block' + (clicks + 1));
            });

            if (itemsNext.length === 0) {
              me.text('NO MORE WORKS');
              me.addClass('cbp-l-loadMore-button-stop');
            }

          });

      })
      .fail(function() {
        // error
      });

  });

















})(jQuery);