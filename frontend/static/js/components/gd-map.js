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
        NgMap.getMap().then(initMap);

        function initMap(map) {
            vm.map = map;
        }
    }
})();
