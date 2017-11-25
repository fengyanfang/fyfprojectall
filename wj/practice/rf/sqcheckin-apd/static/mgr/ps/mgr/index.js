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
        .state('course', {
            url:'/',
            templateUrl: 'course.html',
            controller: 'courseCtrl'
        })
        .state('teacher', {
            url:'/teacher',
            templateUrl: 'teacher.html',
            controller: 'teacherCtrl'
        })
        .state('training', {
            url:'/training',
            templateUrl: 'training.html',
            controller: 'trainingCtrl'
        })
        .state('traininggrade', {
            url:'/traininggrade',
            templateUrl: 'training_grade.html',
            controller: 'traininggradeCtrl'
        })
        .state('lesson', {
            url:'/lesson',
            templateUrl: 'lesson.html',
            controller: 'lessonCtrl'
        })
        .state('student', {
            url:'/student',
            templateUrl: 'student.html',
            controller: 'studentCtrl'
        })
        .state('student.checkin_history', {
            url:'/student_checkin_history/:uid',
            templateUrl: 'student_checkin_history.html',
            controller: 'studentcheckinhistoryCtrl'
        })
        .state('student_checkin_by_course', {
            url:'/student_checkin_by_course/:uid',
            templateUrl: 'student_checkin_by_course.html',
            controller: 'studentCheckinByCourseCtrl'
        })
        .state('changepasswd', {
            url:'/changepasswd',
            templateUrl: 'changepasswd.html',
            controller: 'changepasswdCtrl'
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

    //var schoolId = $state.params.schoolid;
    $scope.share = shareSvc.share;

    
    $scope.logout = function () {
        Util.angular_get($http,
            '/api/mgr/logoutreq',
            function (ret) {
                window.location.href =  "/mgr/login/login.html"
            });
    };

});

