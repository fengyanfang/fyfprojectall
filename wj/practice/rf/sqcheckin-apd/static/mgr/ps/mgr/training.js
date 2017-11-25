// 初始化


frameApp.controller('trainingCtrl', function ($scope,$http,shareSvc) {

    $scope.courseList = null;
    var courseTable = null;

    $scope.theList = null;

    $scope.currentPage = 1;
    $scope.totalNum = 0;
    $scope.pageSize = 100;

    $scope.isOneEditing = false; // 是否当前正在编辑一个信息，只允许一个正在编辑

    $scope.courseSelected = null;


    function listToTable(thelist){
        var table = {};
        for (var i=0; i<thelist.length;i++){
            var one = thelist[i];
            table[one.id] = one;
        }
        return table;
    }

    $scope.pageChangeTo = function(pageNumber) {$http,
        Util.angular_get($http,
            '/api/mgr/sq_mgr/?action=list_training&pagenum='+pageNumber  + '&pagesize='+$scope.pageSize,
            function (ret) {

                if (ret.total==0 && $scope.currentPage>1){
                    $scope.currentPage-=1;
                    return;
                }


                $scope.theList = ret.retlist;
                $scope.totalNum = ret.total;


                // 解码 courseList, 并且以最新的课程列表信息更新
                for (var i=0; i<$scope.theList.length;i++){
                    var courseListStr = $scope.theList[i].courselist;
                    $scope.theList[i].courselist = JSON.parse(courseListStr);

                    var courselist = $scope.theList[i].courselist;
                    for (var j=0; j<courselist.length;j++){

                        var cid = courselist[j].id;
                        if (!(cid in courseTable)){
                            console.log('Error! training has course that has been deleted, cid' + cid);
                            courselist[j].name = '!不存在! ' + courselist[j].name ;
                        }
                        else{
                            courselist[j].name = courseTable[cid].name;
                        }

                    }

                }
            }
        );

    };




    // 得到课程列表
    Util.angular_get($http,
        '/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=100',
        function (ret) {

            $scope.courseList = ret.retlist;
            courseTable = listToTable(ret.retlist);
            $scope.pageChangeTo(1);
        }
    );


    $scope.showAddOne=false;

    // ************* add one  *************


    $scope.addEditData={

        name:'',
        courselist:[],
        desc:'',
        display_idx:1,

        addTeachCourse : function() {
            var cs = $scope.courseSelected;
            if (!cs){
                return
            }

            // 检查是否已经存在
            for (var i=0; i<this.courselist.length;i++){
                if(this.courselist[i].id == cs.id){
                    return
                }
            }
            this.courselist.push({id:cs.id,name:cs.name});
        },
        delTeachCourse : function(one) {
            for (var i=0; i<this.courselist.length;i++){
                if(this.courselist[i].id == one.id){
                    this.courselist.splice(i,1);
                    return
                }
            }
        },

        // 编码成字符串， 以便发送给服务端
        encodeOne : function() {
            var tmp = this.courselist;
            this.courselist = angular.toJson(this.courselist);
            var ret =  encodeURIComponent(angular.toJson($scope.addEditData));
            this.courselist = tmp;
            return ret;
        }

    };


    $scope.addOne = function() {

        $scope.addEditData.name = $scope.addEditData.name.trim();
        if ($scope.addEditData.name.length==0){
            BootstrapDialog.alert('请填写培训班名');
            return
        }
        var paramStr =  'action=add_training&data='+ $scope.addEditData.encodeOne();

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
        $scope.addEditData.courselist=one.courselist;
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


        var paramStr =  'action=modify_training&id='+one.id;
        paramStr += '&newdata='+$scope.addEditData.encodeOne();


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

            var paramStr =  'action=delete_training&id='+one.id;
            Util.angular_delete($http,
                '/api/mgr/sq_mgr/',
                paramStr,
                function(ret){
                    $scope.pageChangeTo($scope.currentPage);
                });
        });
    };








});

