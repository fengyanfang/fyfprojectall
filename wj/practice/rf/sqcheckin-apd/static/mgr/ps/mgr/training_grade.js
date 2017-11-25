// 初始化


frameApp.controller('traininggradeCtrl', function ($scope,$http,shareSvc) {

    $scope.trainingList = null;
    $scope.theList = null;

    $scope.currentPage = 1;
    $scope.totalNum = 0;
    $scope.pageSize = 20;

    $scope.isOneEditing = false; // 是否当前正在编辑一个信息，只允许一个正在编辑

    $scope.trainingSelected = null;

    $scope.pageChangeTo = function(pageNumber) {$http,
        Util.angular_get($http,
            '/api/mgr/sq_mgr/?action=list_training_grade&pagenum='+pageNumber  + '&pagesize='+$scope.pageSize,
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


    // 得到培训班列表
    Util.angular_get($http,
        '/api/mgr/sq_mgr/?action=list_training&pagenum=1&pagesize=100',
        function (ret) {

            $scope.trainingList = ret.retlist;
        }
    );


    $scope.showAddOne=false;

    // ************* add one  *************


    $scope.addEditData={

        name:'',
        training_id:null,
        desc:'',
        display_idx:1,

    };


    $scope.addOne = function() {

        $scope.addEditData.name = $scope.addEditData.name.trim();
        if ($scope.addEditData.name.length==0){
            BootstrapDialog.alert('请填写培训班名');
            return
        }
        var paramStr =  'action=add_training_grade&data='+encodeURIComponent(JSON.stringify($scope.addEditData));

        if($scope.addEditData.display_idx==null||$scope.addEditData.display_idx==''){
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

        if($scope.isOneEditing){
            BootstrapDialog.alert('同时只能编辑一个，请先完成当前编辑!!');
            return
        }
        $scope.isOneEditing = true;
        one.editing=true;

        $scope.addEditData.name=one.name;
        $scope.addEditData.training_id=one.training_id;
        $scope.addEditData.desc=one.desc;
        $scope.addEditData.display_idx=one.display_idx;

        // $scope.addEditData = JSON.parse(JSON.stringify(one))
    };
    $scope.editOneCancel = function(one) {

        one.editing=false;
        $scope.isOneEditing = false;
    };

    $scope.editOneSubmit = function(one) {

        one.editing = false;
        $scope.isOneEditing = false;


        var paramStr =  'action=modify_training_grade&id='+one.id;
        paramStr += '&newdata=' + encodeURIComponent(JSON.stringify($scope.addEditData));


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

            var paramStr =  'action=delete_training_grade&id='+one.id;
            Util.angular_delete($http,
                '/api/mgr/sq_mgr/',
                paramStr,
                function(ret){
                    $scope.pageChangeTo($scope.currentPage);
                });
        });
    };








});

