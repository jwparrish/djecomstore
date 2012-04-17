function prepareDocument(){
	jQuery("form#search").submit(function() {
		text = jQuery("#id_q").val();
		if (text == "" || text == "Search") {
			// if empty, pop up alert
			alert("Enter a search term.");
			// halt submission of form
			return false;
		}
	});
}

jQuery(document).ready(prepareDocument);