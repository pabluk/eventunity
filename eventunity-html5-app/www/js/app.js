/**
 * Wait before the DOM has been loaded before initializing the Ubuntu UI layer
 */
window.onload = function () {
    var eventunityAPI = 'http://eventunity.seminar.io/api';
    var UI = new UbuntuUI();

    var locations;
    var locationsOptionSelector;
    var currentCoordinates;
    var localEvents;
    var localEventList = UI.list('[id="local-events"]');
    var communities;
    var communityList = UI.list('[id="communities"]');

    UI.init();
    UI.pagestack.push("main");

    restoreLocationsOptionSelector();
    restoreLocalEvents();
    restoreCommunities();

    // Fetch updated data
    fetchHomeData(currentCoordinates);

    locationsOptionSelector.onClicked(function (e) {
        currentCoordinates = e.values;
        fetchHomeData(currentCoordinates);
        $('#local-events-more').val(currentCoordinates);
    })

    UI.button('local-events-more').click(function (e) {
        loadEventsByLocation(e.target.value);
    });

    UI.button('button-website').click(function (e) {
        console.log("Open website " + e.target.value);
        window.open(e.target.value, '_blank');
    });


    /* Functions and callbacks */

    function restoreLocationsOptionSelector() {
        locations = JSON.parse(localStorage.getItem("locations"));
        if (!locations) {
            // Set default locations
            locations = [
                {"name":"San Francisco, CA, United States", "coordinates": "37.7577,-122.4376"},
                {"name":"London, United Kingdom", "coordinates": "51.5286416,-0.1015987"},
                {"name":"Paris, France", "coordinates": "48.8588589,2.3470599"},
            ];
            localStorage.setItem("locations", JSON.stringify(locations));
        }
        // Populate option selector
        $.each(locations, function(i, loc) {
            $('#locations ul').append('<li data-value="' + loc.coordinates + '"><p>' + loc.name + '</p></li>');
        });
        locationsOptionSelector = UI.optionselector("locations");
        currentCoordinates = locations[0].coordinates;
        $('#local-events-more').val(currentCoordinates);
    }

    function restoreLocalEvents() {
        localEvents = JSON.parse(localStorage.getItem("localevents"));
        if (localEvents) {
            // Populate event list
            populateLocalEvents();
        }
    }

    function restoreCommunities() {
        communities = JSON.parse(localStorage.getItem("communities"));
        if (communities) {
            populateCommunities();
        }
    }

    function populateLocalEvents() {
        localEventList.removeAllItems();
        if (localEvents.events.length > 0) {
            $.each(localEvents.events, function(i, e) {
                eventItem = localEventList.append(
                    e.name,
                    null,
                    e.id,
                    function(target, e) {loadEventDetail(e);},
                    e
                );
                $('a', eventItem).append('<br><span class="event-date"> ' + e.date + '</span><br><span class="event-location"> ' + e.location + '</span>');
            });
            if (localEvents.events_total > localEvents.events.length) {
                $('#local-events-more').show();
            } else {
                $('#local-events-more').hide();
            }
            $('#local-events-msg').hide();
        } else {
            $('#local-events-msg').show();
            $('#local-events-more').hide();
        }
    }

    function populateCommunities() {
        communityList.removeAllItems();
        $.each(communities, function(i, community) {
            communityItem = communityList.append(
                community.name,
                null,
                community.id,
                function(target, community) {loadEventsByCommunity(community);},
                community
            );
            $('a', communityItem).prepend('<aside><img src="' + community.logo + '"></aside>');
            $('a', communityItem).append('<br><span class="small-font">' + community.events_count + ' events</span>');
        });
    }

    function fetchHomeData(coordinates) {
        $('#locations ul li.closed').addClass("closed-progress");
        $.getJSON(eventunityAPI + "/home/" + coordinates + "/?callback=?")
        .done(function(data) {
            // Only update when events change
            if (JSON.stringify(localEvents) !== JSON.stringify(data.local_events)) {
                localStorage.setItem("localevents", JSON.stringify(data.local_events));
                localEvents = data.local_events;
                populateLocalEvents();
            }
            // Only update when communities change
            if (JSON.stringify(communities) !== JSON.stringify(data.communities)) {
                localStorage.setItem("communities", JSON.stringify(data.communities));
                communities = data.communities;
                populateCommunities();
            }
        })
        .always(function() {
            $('#locations ul li.closed').removeClass("closed-progress");
        });
    }

    function loadEventsByCommunity(community) {
        var eventList = UI.list('[id="events"]');
        eventList.setHeader(community.name);
        url = eventunityAPI + "/events/community/" + community.id +"/?callback=?";
        populateEventsPage(url, eventList)
    }

    function loadEventsByLocation(coordinates) {
        var eventList = UI.list('[id="events"]');
        eventList.setHeader("Events by location");
        url = eventunityAPI + "/events/location/" + coordinates +"/?callback=?";
        populateEventsPage(url, eventList)
    }

    function populateEventsPage(url, eventList) {
        UI.pagestack.push("event-page")
        eventList.removeAllItems();
        $('#event-list-progress').show();
        $.getJSON(url)
        .done(function(data) {
            $.each(data, function(i, e) {
                eventItem = eventList.append(
                    e.name,
                    null,
                    e.id,
                    function(target, e) {loadEventDetail(e);},
                    e
                );
                $('a', eventItem).append('<br><span class="event-date"> ' + e.date + '</span><br><span class="event-location"> ' + e.location + '</span>');
            });
        })
        .always(function() {
            $('#event-list-progress').hide();
        });
    }

    function loadEventDetail(e) {
        UI.pagestack.push("detail-page")

        $('#detail-name').text(e.name);
        $('#detail-date').text(e.date);
        $('#detail-location').text(e.location);
        $('#button-website').val(e.url);
        $('#detail-description').text('');
        $('#event-detail-progress').show();
        $.getJSON(eventunityAPI + "/events/" + e.id + "/?callback=?")
        .done(function(detail) {
            $('#detail-description').text(detail.description);
        })
        .always(function() {
            $('#event-detail-progress').hide();
        });

    }

    // Add an event listener that is pending on the initialization
    //  of the platform layer API, if it is being used.
    document.addEventListener("deviceready", function() {
        if (console && console.log)
            console.log('Platform layer API ready');
    }, false);
};
