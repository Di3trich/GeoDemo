(function () {
    'use strict';

    angular
        .module('GeoDemo')
        .component('gdCliente', gdCliente());

    function gdCliente() {
        var component = {
            templateUrl: 'partials/cliente.html',
            controller: GdClienteController,
            controllerAs: 'vm'
        };
        return component;
    }

    GdClienteController.$inject = ['$http', '$mdDialog'];
    function GdClienteController($http, $mdDialog) {
        var vm = this;
        vm.cancelar = cancelar;

        function cancelar() {
            $mdDialog.cancel();
        }
    }
})();