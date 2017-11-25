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

        if($scope.MyNewPassWord1.length<6 ){
            BootstrapDialog.alert('新密码要有6位以上字符组成！');
            return
        }

        var newpassword = $scope.MyNewPassWord1;//新密码
        Util.angular_put($http,'/api/mgr/sq_mgr/',
            'action=changeuserpassword&oldpassword=' + encodeURIComponent(oldpassword) + '&newpassword=' + encodeURIComponent(newpassword),
            function (ret) {

                BootstrapDialog.alert('用户密码修改成功，点击确定，重新登录',
                    function() {
                        window.parent.location.href =  "/mgr/login/login.html"
                    }
                );
            }
        );

    };





});

