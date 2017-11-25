
frameApp.controller('courseCtrl', function ($scope,$http,shareSvc) {

    // $scope.theList 变量用来存储课程列表信息
    // 我们指定 angular 就是根据这个值来 显示 课程列表中的信息的
    $scope.theList = null;

    // ************* list all  *************

    // 定义getall函数到服务端获取所有的 课程信息
    $scope.getall = function() {

        $scope.theList = null;

        // 发起http请求，注意参数


        Util.angular_get($http,
            '/api/mgr_course?action=list_course',
            function (ret) {

                // 更新$scope.theList， angularjs 随后会 自动更新界面内容。
                $scope.theList = ret.data
            }
        );

    };

    // 调用   getall函数到服务端获取所有的 课程信息，更新$scope.theList内容
    //    更新界面 课程表 内容
    $scope.getall();


    $scope.showAddOne=false;



    // ************* add one  *************


    //添加课程填入的数据，都自动传入 $scope.addData 中
    $scope.addData={
        name:'',
        desc:'',
        display_idx:1,

    };

    // 定义点击添加课程的处理函数
    $scope.addOne = function() {

        // 检查参数，是否有没有填的
        if($scope.addData.display_idx==null||$scope.addData.display_idx==''){
            BootstrapDialog.alert('请填写展示次序字段');
            return
        }

        // 构建参数
        var params =  {action:'add_course',data:JSON.stringify($scope.addData)};

        // 发起post请求到后端，提交 新添加的课程数据
        $http({
            method: 'POST',
            url: '/api/mgr_course',
            data: $.param(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function success(response) {
            if(response.data.retcode!=0)
                alert(response.data.err)
            $scope.getall();
        }, function error(response) {$scope.getall();});



    };




    // ************* edit one *************



    $scope.editOneBegin = function(one) {

        one.editing=true;
        $scope.editOne = JSON.parse(JSON.stringify(one))
    };
    $scope.editOneCancel = function(one) {

        one.editing=false;
    };

    $scope.editOneSubmit = function(one) {

        one.editing = false;
        var eone = $scope.editOne;

        if(eone.display_idx==null ||eone.display_idx==''){
            BootstrapDialog.alert('请填写展示次序字段');
            return
        }

        // 构建参数
        var params =  {action:'modify_course',
                        id: one.id,
                        newdata:JSON.stringify(eone)};


        // 发起post请求到后端，提交 修改的课程数据
        $http({
            method: 'POST',
            url: '/api/mgr_course',
            data: $.param(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function success(response) {
            if(response.data.retcode!=0)
                alert(response.data.err)
            $scope.getall();

        }, function error(response) {$scope.getall();});


    };



    $scope.delOne = function(one) {

        BootstrapDialog.confirm('确定删除吗?', function (result) {

            if (!result) {
                return;
            }


            // 构建参数
            var params =  {action:'delete_course',id: one.id};


            // 发起post请求到后端，提交 修改的课程数据
            $http({
                method: 'POST',
                url: '/api/mgr_course',
                data: $.param(params),
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(function success(response) {
                if(response.data.retcode!=0)
                    alert(response.data.err)
                $scope.getall();

            }, function error(response) {$scope.getall();});





    });

    }
});

