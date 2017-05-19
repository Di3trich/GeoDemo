(function () {
    'use strict';

    angular
        .module('GeoDemo')
        .component('gdMap', gdMap());

    function gdMap() {
        var component = {
            'templateUrl': 'partials/map.html',
            'controller': GdMapController,
            'controllerAs': 'vm'
        };
        return component;
    }

    GdMapController.$inject = ['NgMap'];
    function GdMapController(NgMap) {
        var vm = this;
        vm.map = null;
        vm.openMenu = true;
        vm.currentLocation = currentLocation;

        NgMap.getMap().then(initMap);
        function initMap(map) {
            vm.map = map;
        }

        function currentLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    var pos = {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude
                    };
                    vm.map.setCenter(pos);
                    vm.map.setZoom(17);
                }, function () {
                    handleLocationError(true, infoWindow, map.getCenter());
                });
            } else {
                handleLocationError(false, infoWindow, map.getCenter());
            }
        }
    }
})();
