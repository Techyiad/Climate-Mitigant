if (typeof jQuery == 'undefined') {
    console.log("jQuery library is not found.");
} else {

    // TODO: Add general library information/comments
    // TODO: Add grunt/gulp to the project
    (function($) {

        var timer = null;

        $.fn.al = function(options) {

            // Define defaults
            var defaults = {
                context: "default",
                text: {
                    title: "TITLE",
                    description: "DESCRIPTION",
                    dismiss: "DISMISS"
                },
                classes: {
                    container: "",
                    panel: "",
                    title: "",
                    description: "",
                    hr: "",
                    dismiss: ""
                },
                seconds: "infinite",
                redirect: ""
            };

            // Build settings, merging defaults and options
            var settings = $.extend( true, {}, defaults, options );

            // Build the alBoxPanel
            var html  = '<div id="alBox-panel" class="alBox-panel-' + settings.context + ' ' + settings.classes.panel +'">';
                html += '<span id="alBox-title" class="'+ settings.classes.title +'">'+ settings.text.title +'</span>';
                html += '<span id="alBox-description" class="'+ settings.classes.description +'">'+ settings.text.description +'</span>';
                html += '<hr class="'+ settings.classes.hr +'"/>';
                html += '<button id="alBox-dismiss" class="'+ settings.classes.dismiss +'">'+ settings.text.dismiss +'</button>';
                html += '</div>';

            // Place into DOM
            this.html(html);

            if (settings.classes.container != "") {
                $("#alBox").addClass(settings.classes.container);
            }

            // Add the click handler for the dismiss button
            $("#alBox-dismiss").click(clearAl);

            // Click handler for clicking outside the prompt box
            $("#alBox").click(dismiss);

            // Fade in the alert box
            this.fadeIn();

            // If seconds isn't "infinite" set a timer to clear the box
            if (settings.seconds !== "infinite") {
                timer = setInterval(function () {
                    clearTimeout(timer);
                    clearAl();
                    timer = null;
                }, settings.seconds * 1000);
            }

            // Preserve chaining
            return this;
        };

        /**
         * Dismiss only if the panel, title, description not part of the click event
         * @param e: event
         */
        function dismiss(e) {
            e.preventDefault();
            if(!$(e.target).is('#alBox-panel')
                && !$(e.target).is('#alBox-title')
                && !$(e.target).is('#alBox-description')) {

                // Clear the alert box
                clearAl();
            }
        }

        /**
         * Function that will clear the interval, fade the alert out
         * and remove the HTML structure from the container
         */
        function clearAl() {
            clearInterval(timer);
            $("#alBox").fadeOut();
            $("#alBox").html('');

        }

    }(jQuery));
}