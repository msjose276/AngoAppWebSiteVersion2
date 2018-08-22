// Animations init
$(".mainmenu ul#primary-menu").slicknav({
		allowParentLinks: true,
		prependTo: '.responsive-menu',
	});

jQuery(window).on('scroll', function() {
	if ($(this).scrollTop() > 10) {
		$('.header').addClass("sticky");
		$('.header').addClass("blackkkk");
	} else {
		$('.header').removeClass("sticky");
	}
});