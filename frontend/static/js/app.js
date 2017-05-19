(function () {
    'use strict';
    angular
        .module('GeoDemo', [
            'ngMap',
            'ngMaterial',
            'ui.router'
        ])
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider'];
    function config($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise("/");
        $stateProvider
            .state('map', {
                url: '/',
                template: '<gd-map></gd-map>'
            });
    }
})();
