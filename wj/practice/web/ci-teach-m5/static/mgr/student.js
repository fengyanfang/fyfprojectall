// 初始化


frameApp.controller('studentCtrl', function ($scope,$http,$state) {

    $scope.trainingList = null;
    var trainingTable = null;

    $scope.traininggradeListOri = null;
    $scope.traininggradeList = null;
    var traininggradeTable = null;

    $scope.theList = null;

    $scope.currentPage = 1;
    $scope.totalNum = 0;
    $scope.pageSize = 5;

    $scope.isOneEditing = false; // 是否当前正在编辑一个信息，只允许一个正在编辑

    $scope.trainingSelected = null;
    $scope.traininggradeSelected = null;

    $scope.filter = {
        training_id      : null,
        traininggrade_id : null,
        name : null

    };

    function listToTable(thelist){
        var table = {};
        for (var i=0; i<thelist.length;i++){
            var one = thelist[i];
            table[one.id] = one;
        }
        return table;
    }

    $scope.pageChangeTo = function(pageNumber) {
        var url = '/api/mgr_student?action=list_student&pagenum='+pageNumber  + '&pagesize='+$scope.pageSize;


        Util.angular_get($http,
            url,
            function (ret) {

                if (ret.total==0 && $scope.currentPage>1){
                    $scope.currentPage-=1;
                    return;
                }


                $scope.theList = ret.retlist;
                $scope.totalNum = ret.total;





            }
        );

    };



    $scope.pageChangeTo(1);





    // ************* add one  *************

    $scope.showAddOne=false;

    $scope.addEditData={

        username:'',
        realname:'',
        password:'',



    };


    $scope.addOne = function() {

        $scope.addEditData.username = $scope.addEditData.username.trim();
        $scope.addEditData.realname = $scope.addEditData.realname.trim();
        if ($scope.addEditData.username.length==0){
            BootstrapDialog.alert('请填写登录名');
            return
        }
        if ($scope.addEditData.realname.length==0){
            BootstrapDialog.alert('请填写真实姓名');
            return
        }
        var paramStr =  'action=add_student&data='+ encodeURIComponent(angular.toJson($scope.addEditData));


        Util.angular_post($http,
            '/api/mgr_student',
            paramStr,
            function(ret){
                $scope.pageChangeTo(1);
            });
    };


    // ************* edit one *************



    $scope.editOneBegin = function(one) {

        if($scope.isOneEditing){
            BootstrapDialog.alert('同时只能编辑一个，请先完成当前编辑!!');
            return
        }
        $scope.isOneEditing = true;
        one.editing=true;

        $scope.addEditData.username=one.username;
        $scope.addEditData.realname=one.realname;

        // $scope.addEditData = JSON.parse(JSON.stringify(one))
    };
    $scope.editOneCancel = function(one) {

        one.editing=false;
        $scope.isOneEditing = false;
    };

    $scope.editOneSubmit = function(one) {

        one.editing = false;
        $scope.isOneEditing = false;


        var paramStr =  'action=modify_student&id='+one.id;
        paramStr += '&newdata='+encodeURIComponent(angular.toJson($scope.addEditData));


        Util.angular_put($http,
            '/api/mgr_student',
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

            var paramStr =  'action=delete_student&id='+one.id;
            Util.angular_delete($http,
                '/api/mgr_student',
                paramStr,
                function(ret){
                    $scope.pageChangeTo($scope.currentPage);
                });
        });


    };






});

