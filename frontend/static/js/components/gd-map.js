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

    GdMapController.$inject = ['NgMap', '$mdDialog'];
    function GdMapController(NgMap, $mdDialog) {
        var vm = this;
        vm.map = null;
        vm.openMenu = true;
        vm.currentLocation = currentLocation;
        vm.launchComponent = launchComponent;
        vm.clienteDialog = {
            template: '<gd-cliente></gd-cliente>',
            clickOutsideToClose: true
        };
        vm.filtroDialog = {
            template: '<gd-filtro></gd-filtro>',
            clickOutsideToClose: true
        };

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
                    //handleLocationError(true, infoWindow, map.getCenter());
                });
            } else {
                //handleLocationError(false, infoWindow, map.getCenter());
            }
        }

        function launchComponent(config) {
            var template = '<md-dialog flex>' +
                (config.template || '(No Template)') +
                '</md-dialog>';
            var dialog = {
                template: template,
                clickOutsideToClose: !!config.clickOutsideToClose,
                escapeToClose: !!config.escapeToClose,
                parent: config.parent || angular.element(document.body),
                locals: config.locals || {},
                fullscreen: config.fullscreen || true
            };

            var promise = $mdDialog.show(dialog);

            promise.then(config.accept || emptyFn, config.cancel || emptyFn);

            function emptyFn() {
                return undefined;
            }
        }
    }
})();
