// 初始化


frameApp.controller('courseCtrl', function ($scope,$http,shareSvc) {

    $scope.theList = null;

    $scope.currentPage = 1;
    $scope.totalNum = 0;
    $scope.pageSize = 20;

    $scope.pageChangeTo = function(pageNumber) {$http,
        Util.angular_get($http,
            '/api/mgr/sq_mgr/?action=list_course&pagenum='+pageNumber  + '&pagesize='+$scope.pageSize,
            function (ret) {

                if (ret.total==0 && $scope.currentPage>1){
                    $scope.currentPage-=1;
                    return;
                }

                $scope.theList = ret.retlist;
                $scope.totalNum = ret.total
            }
        );

    };

    $scope.pageChangeTo(1);


    $scope.showAddOne=false;

    // ************* add one  *************


    $scope.addData={
        name:'',
        desc:'',
        display_idx:1,

    };


    $scope.addOne = function() {

        var paramStr =  'action=add_course&data='+encodeURIComponent(JSON.stringify($scope.addData));

        if($scope.addData.display_idx==null||$scope.addData.display_idx==''){
            BootstrapDialog.alert('请填写展示次序字段');
            return
        }

        Util.angular_post($http,
            '/api/mgr/sq_mgr/',
            paramStr,
            function(ret){
                $scope.pageChangeTo(1);
            });
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


        var paramStr =  'action=modify_course&id='+one.id;
        paramStr += '&newdata='+encodeURIComponent(JSON.stringify(eone));


        Util.angular_put($http,
            '/api/mgr/sq_mgr/',
            paramStr,
            function(ret){
                $scope.pageChangeTo($scope.currentPage);
            });
    };



    $scope.delOne = function(one) {


        BootstrapDialog.confirm('确定删除吗?', function (result) {

            if (!result) {
                return;
            }

            var paramStr =  'action=delete_course&id='+one.id;
            Util.angular_delete($http,
                '/api/mgr/sq_mgr/',
                paramStr,
                function(ret){
                    $scope.pageChangeTo($scope.currentPage);
                });
        });


    };








});

