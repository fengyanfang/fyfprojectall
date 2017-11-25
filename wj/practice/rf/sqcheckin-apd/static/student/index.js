//only allow numbers, backspace, delet, left arrow and right arrow keys in textbox
function validateQty(event) {
    var key = window.event ? event.keyCode : event.which;

    if (event.keyCode == 8 || event.keyCode == 46
        || event.keyCode == 37 || event.keyCode == 39) {
        return true;
    }
    else if ( key < 48 || key > 57 ) {
        return false;
    }
    else return true;
};

function _endsWith (str, suffix) {
    return str.indexOf(suffix, str.length - suffix.length) !== -1;
};



var frameApp = angular.module('FrameApp', ['ngRoute','ngSanitize',
    'angularUtils.directives.dirPagination',
]);

frameApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

frameApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
        when('/home', {
            templateUrl: 'home/home.html',
            controller: 'homeCtrl'
        }).
        when('/checkin', {
            templateUrl: 'checkin/checkin.html',
            controller: 'checkinCtrl'
        }).
        when('/checkinhistory', {
            templateUrl: 'checkin/checkin_history.html',
            controller: 'checkinhistoryCtrl'
        }).
        when('/changepasswd', {
            templateUrl: 'others/changepasswd.html',
            controller: 'changepasswdCtrl'
        }).
        otherwise({
            redirectTo: '/home'
        });
    }]);


// 创建自定义 shareSvc service, 共享数据
frameApp.factory('shareSvc', function ($http) {
    var obj = {




        util : {

            topBarScope : undefined,

            saved :{
                lasttime_refreshnotify : 5000000000, //初始值设置为2128年，防止首次就捎带刷新通知
            },




            studentInfo:{
                info : undefined,
                slessons: undefined,
                clessons: undefined,
            },


            lessonTable:{},



            curTimestamp : function() {
                var theDate = new Date().getTime();
                return Math.floor(theDate / 1000);
            },

            delObjFromList : function(theList,obj){
                var index = theList.indexOf(obj);
                if (index > -1) {
                    theList.splice(index, 1);
                }
            },

            createParamStrSearchingDateRange: function(){
                var paramStr = "";
                var checkTimeAfterStr = $("#createTimeAfter").val();
                if (checkTimeAfterStr != ""){
                    var checkTimeDate = new Date(checkTimeAfterStr + "T00:00:00");
                    var checkTimeInt =     Math.floor(checkTimeDate.getTime() / 1000);
                    paramStr += '&createtimeafter=' + checkTimeInt;
                }

                var checkTimeBeforeStr = $("#createTimeBefore").val();
                if (checkTimeBeforeStr != ""){
                    var checkTimeDate = new Date(checkTimeBeforeStr + "T23:59:59");
                    var checkTimeInt =     Math.floor(checkTimeDate.getTime() / 1000);
                    paramStr += '&createtimebefore=' + checkTimeInt;
                }

                return paramStr;
            },

            angular_get: function (pUrl,successCallBack) {

                $http({
                    method: 'GET',
                    url: pUrl
                })
                    .success(function(ret) {
                        if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
                        if (successCallBack) successCallBack(ret);

                    });
            },

            // pData 是字符串， 调用者负责拼接
            angular_post: function (pUrl,pData,successCallBack) {

                if (this.topBarScope){
                    this._checkNotify();
                }

                $http({
                    method: 'POST',
                    url: pUrl,
                    data: pData,
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}

                })
                    .success(function(ret) {
                        if (ret.retcode != 0){
                            if (ret.retcode === 302)
                                window.top.location.href = ret.redirect;

                            BootstrapDialog.alert('错误 : ' + ret.reason);
                            return;
                        }
                        if (successCallBack) successCallBack(ret);

                    });
            },



            // pData 是对象， 比如 {action: "create", newgroupname:3}
            angular_post2: function (pUrl,pData,successCallBack) {

                $http({
                    method: 'POST',
                    url: pUrl,
                    data: $.param(pData),
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}

                })
                    .success(function(ret) {
                        if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
                        if (successCallBack) successCallBack(ret);

                    });
            },

            angular_put: function (pUrl,pData,successCallBack) {

                $http({
                    method: 'PUT',
                    url: pUrl,
                    data: pData,
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}

                })
                    .success(function(ret) {
                        if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
                        if (successCallBack) successCallBack(ret);

                    });
            },

            angular_put2: function (pUrl,pData,successCallBack) {

                $http({
                    method: 'PUT',
                    url: pUrl,
                    data: $.param(pData),
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}

                })
                    .success(function(ret) {
                        if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
                        if (successCallBack) successCallBack(ret);

                    });
            },

            angular_delete: function (pUrl,pData,successCallBack) {

                $http({
                    method: 'DELETE',
                    url: pUrl,
                    data: pData,
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}

                })
                    .success(function(ret) {
                        if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
                        if (successCallBack) successCallBack(ret);

                    });
            },


            get_my_info : function (callBack){

                var ref_studentInfo = this.studentInfo;
                if(ref_studentInfo.info){
                    if (callBack) callBack(ref_studentInfo.info);
                    return;
                }

                this.angular_get('/api/student/sq_student/?action=getmyinfo',
                    function(ret){
                        ref_studentInfo.info= ret.info;

                        if (callBack) callBack((ret.info))

                    }
                )
            },

            get_my_scheduledlessons : function (callBack){

                var ref_studentInfo = this.studentInfo;
                if(ref_studentInfo.slessons){
                    if (callBack) callBack(ref_studentInfo.slessons);
                    return;
                }

                this.angular_get('/api/student/sq_student/?action=getmyslessons',
                    function(ret){

                        // 解码 starttime, endtime
                        for (var i=0; i<ret.slessons.length;i++){

                            var stStr = ret.slessons[i].starttime;
                            ret.slessons[i].starttime = new Date(stStr);
                            var etStr = ret.slessons[i].endtime;
                            ret.slessons[i].endtime = new Date(etStr);

                        }

                        ref_studentInfo.slessons= ret.slessons;

                        if (callBack) callBack((ret.slessons))

                    }
                )
            },


            get_my_checkinlessons : function (callBack){



                this.angular_get('/api/student/sq_student/?action=getmyclessons',
                    function(ret){

                        // 解码 starttime, endtime
                        for (var i=0; i<ret.clessons.length;i++){

                            var stStr = ret.clessons[i].starttime;
                            ret.clessons[i].starttime = new Date(stStr);
                            var etStr = ret.clessons[i].endtime;
                            ret.clessons[i].endtime = new Date(etStr);

                        }

                        // ref_studentInfo.clessons= ret.clessons;

                        if (callBack) callBack((ret.clessons))

                    }
                )
            },


            checkin : function (lesson){



            },


        },


    };

    return obj;
});


frameApp.controller('topbarCtrl', function ($scope,$http,$location,shareSvc) {

    shareSvc.util.topBarScope = $scope;

    $scope.schoolname = "松勤";
    $scope.realname = "个人中心";
    
    $scope.avatar_url = "/jojo_cdn/images/public/profile_icon.jpg";


    $scope.$on('userinfochange', function () {
        $scope.avatar_url = shareSvc.util.studentInfo.basicInfo.avatar_url;
        $scope.realname = shareSvc.util.studentInfo.basicInfo.realname;
    });



    $scope.logout = function () {

        shareSvc.util.angular_get(
            '/api/student/logoutreq',
            function (ret) {
                window.location.href =  "/student/login/login.html"
            });
    };

    shareSvc.util.get_my_info(function(info){

        $scope.realname   = info.realname;
        // $scope.avatar_url = info.avatar_url;

    });
});



function isIE () {
    var myNav = navigator.userAgent.toLowerCase();
    return (myNav.indexOf('msie') != -1) ? parseInt(myNav.split('msie')[1]) : false;
}
if (isIE()) {
    BootstrapDialog.alert("\n\n您使用的IE浏览器已经过时了哦.\n\n如果您使用的是360、搜狗浏览器，请选择极速模式\n\n" +
        "<a href='http://rj.baidu.com/soft/detail/14744.html?ald' target='_blank' style='color: rgba(0,136,255,1)'>推荐您使用谷歌浏览器,点击下载</a>\n\n");
}


