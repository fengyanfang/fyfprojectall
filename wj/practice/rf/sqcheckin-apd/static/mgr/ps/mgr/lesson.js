// 初始化


frameApp.controller('lessonCtrl', function ($scope,$http,shareSvc) {

    $scope.courseList = null;
    $scope.theList = null;

    $scope.currentPage = 1;
    $scope.totalNum = 0;
    $scope.pageSize = 8;

    $scope.isOneEditing = false; // 是否当前正在编辑一个信息，只允许一个正在编辑

    $scope.trainingSelected = null;

    $scope.filter={
        starttime:null,
        endtime:null,
        course_id:null,

        training_id:null,
        traininggrade:null
    };


    $scope.pageChangeTo = function(pageNumber) {

        var url = '/api/mgr/sq_mgr/?action=list_lesson&pagenum='+pageNumber  + '&pagesize='+$scope.pageSize;
        if ($scope.filter.starttime)
            url += '&starttime='+ encodeURIComponent(JSON.stringify($scope.filter.starttime));
        if ($scope.filter.endtime)
            url += '&endtime='+ encodeURIComponent(JSON.stringify($scope.filter.endtime));
        if ($scope.filter.course_id)
            url += '&course_id='+ encodeURIComponent(JSON.stringify($scope.filter.course_id));


        Util.angular_get($http,
            url,
            function (ret) {

                if (ret.total==0 && $scope.currentPage>1){
                    $scope.currentPage-=1;
                    return;
                }


                $scope.theList = ret.retlist;
                $scope.totalNum = ret.total;


                // 解码 starttime, endtime
                for (var i=0; i<$scope.theList.length;i++){

                    var stStr = $scope.theList[i].starttime;
                    $scope.theList[i].starttime = new Date(stStr);
                    var etStr = $scope.theList[i].endtime;
                    $scope.theList[i].endtime = new Date(etStr);

                }

            }
        );

    };

    $scope.pageChangeTo(1);


    // 得到课程列表
    Util.angular_get($http,
        '/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=100',
        function (ret) {

            $scope.courseList = ret.retlist;
        }
    );




    // ************* add one  *************

    $scope.showAddOne=false;

    $scope.addEditData={

        course_id:null,
        starttime:new Date(),
        endtime:new Date(),
        desc:'',

    };
    $scope.addEditData.starttime.setSeconds(0,0);//$scope.addEditData.starttime.setMinutes(0);
    $scope.addEditData.endtime.setSeconds(0,0);//$scope.addEditData.endtime.setMinutes(0);


    $scope.addOne = function() {

        if (!$scope.addEditData.course_id){
            BootstrapDialog.alert('请选择课程');
            return
        }

        // var tmpData = JSON.parse(JSON.stringify($scope.addEditData));
        // tmpData.starttime = tmpData.starttime.toLocaleDateString();
        var paramStr =  'action=add_lesson&data='+encodeURIComponent(JSON.stringify($scope.addEditData));



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

        $scope.addEditData.course_id=one.course_id;
        $scope.addEditData.starttime=one.starttime;
        $scope.addEditData.endtime=one.endtime;
        $scope.addEditData.desc=one.desc;

        // $scope.addEditData = JSON.parse(JSON.stringify(one))
    };
    $scope.editOneCancel = function(one) {

        one.editing=false;
        $scope.isOneEditing = false;
    };

    $scope.editOneSubmit = function(one) {

        one.editing = false;
        $scope.isOneEditing = false;


        var paramStr =  'action=modify_lesson&id='+one.id;
        paramStr += '&newdata=' + encodeURIComponent(JSON.stringify($scope.addEditData));


        Util.angular_put($http,
            '/api/mgr/sq_mgr/',
            paramStr,
            function(ret){
                $scope.pageChangeTo($scope.currentPage);
            });
    };



    $scope.delOne = function(lesson) {

        BootstrapDialog.confirm('确定删除吗?', function (result) {

            if (!result) {
                return;
            }

            var paramStr =  'action=delete_lesson&id='+lesson.id;
            Util.angular_delete($http,
                '/api/mgr/sq_mgr/',
                paramStr,
                function(ret){
                    $scope.pageChangeTo($scope.currentPage);
                });
        });
    };





    // ************************** 课程 签到 总名单 显示 **************

 

    $scope.checkinList = [];
    $scope.classStudentsWithCheckin = [];
    $scope.showCheckinByClass = false;

    $scope.showCheckins = function(lesson) {

        $scope.lessonViewCheckin = lesson;
        $scope.checkinList = [];
        $scope.showCheckinByClass = false;

        $scope.filter.training_id = null;
        $scope.filter.traininggrade = null;

        Util.angular_get($http,
            '/api/mgr/sq_mgr/?action=list_lesson_checkins&lessonid='+lesson.id,
            function (ret) {

                $scope.checkinList = ret.retlist;

            }
        );
    };

    // ************************** 签到 按班级 显示 **************
    // 得到培训类型/班期 列表,

    $scope.trainingList = null;
    $scope.traininggradeListOri = null;
    $scope.traininggradeList = null;  

    Util.angular_get($http,
        '/api/mgr/sq_mgr/?action=list_training&pagenum=1&pagesize=100',
        function (ret) {

            $scope.trainingList = ret.retlist;
            Util.angular_get($http,
                '/api/mgr/sq_mgr/?action=list_training_grade&pagenum=1&pagesize=100',
                function (ret) {
                    $scope.traininggradeList = ret.retlist;
                    $scope.traininggradeListOri = ret.retlist;
                }
            );
        }
    );

    // 用户选择了一个培训类型
    $scope.filter_trainingchanged = function() {

        var newTraininggradeList=[];
        for (var i=0;i<$scope.traininggradeListOri.length;i++){
            if($scope.traininggradeListOri[i].training__id == $scope.filter.training_id){
                newTraininggradeList.push($scope.traininggradeListOri[i])
            }
        }
        $scope.traininggradeList = newTraininggradeList;        

    }

    // 培训班期改变了
    $scope.filter_traininggradechanged = function() {
        
        $scope.classStudentsWithCheckin = [];
        $scope.showCheckinByClass = true;

        var selectedClass = $scope.filter.traininggrade
        if(!selectedClass){
            return
        }
     
        //获取班级学员签到信息
        Util.angular_post($http,
            '/api/mgr/sq_mgr/',
            'action=get_classstudent_checkins&traininggrade_id=' + selectedClass.id 
            + '&checkinlist=' + encodeURIComponent(JSON.stringify($scope.checkinList)),
            function (ret) {     
                $scope.classStudentsWithCheckin = ret.retlist;  
            }
        );
        
        


    }




});

