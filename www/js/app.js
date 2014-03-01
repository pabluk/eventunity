/**
 * Wait before the DOM has been loaded before initializing the Ubuntu UI layer
 */
window.onload = function () {
    var eventunityAPI = 'http://eventunity.debugstack.com';
    var UI = new UbuntuUI();
    UI.init();
    UI.pagestack.push("main");

    $.getJSON(eventunityAPI + "/communities/", function(data) {
        var community_list = UI.list('[id="communities"]');
        community_list.removeAllItems();
        community_list.setHeader("Choose a community");
        $.each(data, function(i, community) {
            community_list.append(
                community.name,
                null,
                community.id,
                function(target, community) {loadEvents(community);},
                community
            );
        });
    });

    function loadEvents(community) {
        UI.pagestack.push("event-page")
        $.getJSON(eventunityAPI + "/communities/" + community.id +"/events/", function(data) {
            var event_list = UI.list('[id="events"]');
            event_list.removeAllItems();
	        event_list.setHeader("Upcoming events for " + community.name);
            $.each(data, function(i, e) {
                event_list.append(
                    e.title,
                    null,
                    e.id,
                    function(target, e) {loadEventDetail(e);},
                    e
                );
            });
        });

    }

    function loadEventDetail(e) {
        UI.pagestack.push("detail-page")
        $.getJSON(eventunityAPI + "/events/" + e.id + "/detail/", function(detail) {
            $('#detail-title').text(detail.title);
            $('#detail-date').text(detail.date);
            $('#detail-location').text(detail.location);
            $('#detail-description').text(detail.description);
        });
    }

    // Add an event listener that is pending on the initialization
    //  of the platform layer API, if it is being used.
    document.addEventListener("deviceready", function() {
        if (console && console.log)
            console.log('Platform layer API ready');
    }, false);
};

