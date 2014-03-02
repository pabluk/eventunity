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
        $.each(data, function(i, community) {
            communityItem = community_list.append(
                community.name,
                null,
                community.id,
                function(target, community) {loadEvents(community);},
                community
            );
            $('a', communityItem).prepend('<aside><img src="' + community.logo_url + '"></aside>');
            $('a', communityItem).append('<br><span class="small-font">' + community.events_count + ' events</span>');
        });
    });

    function loadEvents(community) {
        UI.pagestack.push("event-page")
        var event_list = UI.list('[id="events"]');
        event_list.removeAllItems();
        $.getJSON(eventunityAPI + "/communities/" + community.id +"/events/", function(data) {
            $.each(data, function(i, e) {
                eventItem = event_list.append(
                    e.title,
                    null,
                    e.id,
                    function(target, e) {loadEventDetail(e);},
                    e
                );
                $('a', eventItem).append('<br><span class="event-date"> ' + e.date + '</span> <span class="event-location"> ' + e.location + '</span>');
            });
        });

    }

    function loadEventDetail(e) {
        UI.pagestack.push("detail-page")
        $('#detail-title').text('');
        $('#detail-date').text('');
        $('#detail-location').text('');
        $('#detail-description').text('');
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

