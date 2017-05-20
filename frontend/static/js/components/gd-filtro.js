(function () {
    'use strict';

    angular
        .module('GeoDemo')
        .component('gdFiltro', gdFiltro());

    function gdFiltro() {
        var component = {
            templateUrl: 'partials/filtro.html',
            controller: GdFiltroController,
            controllerAs: 'vm'
        };
        return component;
    }

    GdFiltroController.$inject = ['$http', '$mdDialog'];
    function GdFiltroController($http, $mdDialog) {
        var vm = this;
        vm.cancelar = cancelar;

        function cancelar() {
            $mdDialog.cancel();
        }
    }
})();