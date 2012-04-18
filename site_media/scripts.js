// toggles visibility of "write review" link
// and the review form.
function slideToggleReviewForm() {
	jQuery("#review_form").slideToggle();
	jQuery("#add_review").slideToggle();
}

function addProductReview() {
	// build an object of review data to submit
	var review = {
		title: jQuery("#id_title").val(),
		content: jQuery("#id_content").val(),
		rating: jQuery("#id_rating").val(),
		slug: jQuery("#id_slug").val() };
	// make request, process response
	jQuery.post("/review/product/add", review,
		function(response){
			jQuery("#review_errors").empty();
			// evaluate the "success" parameter
			if(response.success == "True"){
				// disable the submit button to prevent duplicates
				jQuery("#submit_review").attr('disabled', 'disabled');
				// if this is first review, get rid of "no reviews" text
				jQuery("#no_reviews").empty();
				// add the new review to the reviews section
				jQuery("#reviews").prepend(response.html).slideDown();
				// get the newly added review and style it with color
				new_review = jQuery("#reviews").children(":first");
				new_review.addClass('new_review');
				// hide the review form
				jQuery("#review_form").slideToggle();
			}
			else{
				// add the error text to the review_errors div
				jQuery("#review_errors").append(response.html);
			}
		}, "json");
	}

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
	jQuery("#submit_review").click(addProductReview);
	jQuery("#review_form").addClass('hidden');
	jQuery("#add_review").click(slideToggleReviewForm);
	jQuery("#add_review").addClass('visible');
	jQuery("#cancel_review").click(slideToggleReviewForm);
}

jQuery(document).ready(prepareDocument);