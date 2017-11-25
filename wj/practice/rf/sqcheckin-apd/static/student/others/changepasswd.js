// 初始化


frameApp.controller('changepasswdCtrl', function ($scope,$http,shareSvc) {


    //修改密码
    $scope.modifyPassword=function(){
        if(!$scope.MyPassWord || $scope.MyPassWord===""  ){
            BootstrapDialog.alert('请输入当前使用的密码！！');
            return
        }

        var oldpassword=$scope.MyPassWord;//旧密码
        if(!$scope.MyNewPassWord1 || $scope.MyNewPassWord1===""  ){
            BootstrapDialog.alert('请输入新密码！！');
            return
        }
        if($scope.MyNewPassWord2 !=$scope.MyNewPassWord1 ){
            BootstrapDialog.alert('新密码和确认密码不同！');
            return
        }

        if($scope.MyNewPassWord1.length<5 ){
            BootstrapDialog.alert('新密码至少需要5位字符！');
            return
        }

        var newpassword = $scope.MyNewPassWord1;//新密码
        shareSvc.util.angular_put('/api/student/sq_student/',
            'action=changeuserpassword&oldpassword=' + encodeURIComponent(oldpassword) + '&newpassword=' + encodeURIComponent(newpassword),
            function (ret) {

                BootstrapDialog.alert('用户密码修改成功，点击确定，重新登录',
                    function() {
                        shareSvc.util.angular_get(
                            '/api/student/logoutreq',
                            function () {
                                window.location.href =  "/student/login/login.html"
                            });
                    }
                );
            }
        );

    };





});

