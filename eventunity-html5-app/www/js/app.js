/**
 * Wait before the DOM has been loaded before initializing the Ubuntu UI layer
 */
window.onload = function () {
    var eventunityAPI = 'http://eventunity.seminar.io/api';
    var UI = new UbuntuUI();
    UI.init();
    UI.pagestack.push("main");

    var locationsOS = UI.optionselector("locations");
    locationsOS.onClicked(function (selected) {
        console.log("optionselector1 values: " + selected.values);
        $.getJSON(eventunityAPI + "/events/location/" + selected.values +"/?callback=?", function(data) {
            console.log(data);
            var localEventList = UI.list('[id="local-events"]');
            localEventList.removeAllItems();
            $.each(data, function(i, e) {
                eventItem = localEventList.append(
                    e.name,
                    null,
                    e.id,
                    function(target, e) {loadEventDetail(e);},
                    e
                );
                $('a', eventItem).append('<br><span class="event-date"> ' + e.date + '</span><br><span class="event-location"> ' + e.location + '</span>');
            });
        });
    });

    $.getJSON(eventunityAPI + "/home/?callback=?", function(data) {
        var localEventList = UI.list('[id="local-events"]');
        var communityList = UI.list('[id="communities"]');

        localEventList.removeAllItems();
        $.each(data.events, function(i, e) {
            eventItem = localEventList.append(
                e.name,
                null,
                e.id,
                function(target, e) {loadEventDetail(e);},
                e
            );
            $('a', eventItem).append('<br><span class="event-date"> ' + e.date + '</span><br><span class="event-location"> ' + e.location + '</span>');
        });

        communityList.removeAllItems();
        $.each(data.communities, function(i, community) {
            communityItem = communityList.append(
                community.name,
                null,
                community.id,
                function(target, community) {loadEvents(community);},
                community
            );
            $('a', communityItem).prepend('<aside><img src="' + community.logo + '"></aside>');
            $('a', communityItem).append('<br><span class="small-font">' + community.events_count + ' events</span>');
        });
    });

    function loadEvents(community) {
        UI.pagestack.push("event-page")
        var event_list = UI.list('[id="events"]');
        event_list.removeAllItems();
        $.getJSON(eventunityAPI + "/communities/" + community.id +"/events/?callback=?", function(data) {
            $.each(data, function(i, e) {
                eventItem = event_list.append(
                    e.name,
                    null,
                    e.id,
                    function(target, e) {loadEventDetail(e);},
                    e
                );
                $('a', eventItem).append('<br><span class="event-date"> ' + e.date + '</span><br><span class="event-location"> ' + e.location + '</span>');
            });
        });

    }

    function loadEventDetail(e) {
        UI.pagestack.push("detail-page")
        $('#detail-name').text('');
        $('#detail-date').text('');
        $('#detail-location').text('');
        $('#detail-description').text('');
        $.getJSON(eventunityAPI + "/events/" + e.id + "/?callback=?", function(detail) {
            $('#detail-name').text(detail.name);
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

