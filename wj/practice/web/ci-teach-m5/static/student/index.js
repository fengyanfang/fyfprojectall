// 初始化


var frameApp = angular.module('FrameApp',
                              ['ui.router','angularUtils.directives.dirPagination'] // modules that frameApp depends on
);

frameApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);


frameApp.config(['$stateProvider', '$urlRouterProvider',  function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider

        .state('checkin', {
            url:'/',
            templateUrl: 'checkin.html',
            controller: 'checkinCtrl'
        })
}]);


// 创建自定义 shareSvc service, 共享数据
frameApp.factory('shareSvc', function ($http) {

    var shareSvcObj = {


        share: {
            schoolName: undefined
        },

    };


    return shareSvcObj;
});


frameApp.controller('allCtrl', function ($scope,$http,shareSvc) {

    $scope.share = shareSvc.share;

    
    $scope.logout = function () {
        Util.angular_get($http,
            '/api/logout',
            function (ret) {
                window.location.href =  "/login.html"
            });
    };

});

