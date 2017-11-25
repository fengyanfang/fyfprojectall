// 初始化


frameApp.controller('studentCheckinByCourseCtrl', function ($scope,$http,shareSvc,$stateParams) {

    var studentid = $stateParams.uid;
    
    $scope.courseList = null;
    $scope.theList = null;


    $scope.checkinRate = null;
    $scope.trainingSelected = null;

    $scope.filter={
        starttime:null,
        endtime:null,
        course_id:null,

        training_id:null,
        traininggrade:null
    };


    $scope.tryToShowCheckinList = function() {

        $scope.theList = null;
        $scope.checkinRate = null;

        if(!$scope.filter.course_id || !$scope.filter.starttime || !$scope.filter.endtime){
            return;
        }

        var url = '/api/mgr/sq_mgr/?action=list_lesson&pagenum=1&pagesize=200';
        if ($scope.filter.starttime)
            url += '&starttime='+ encodeURIComponent(JSON.stringify($scope.filter.starttime));
        if ($scope.filter.endtime)
            url += '&endtime='+ encodeURIComponent(JSON.stringify($scope.filter.endtime));
        if ($scope.filter.course_id)
            url += '&course_id='+ encodeURIComponent(JSON.stringify($scope.filter.course_id));


        Util.angular_get($http,
            url,
            function (ret) {

                $scope.theList = ret.retlist;

                var ciCount = 0;
                //处理 每节课的信息， 解码 starttime, endtime，检查是否checkin
                for (var i=0; i<$scope.theList.length;i++){
                    var curLesson = $scope.theList[i];
                    var stStr = curLesson.starttime;
                    curLesson.starttime = new Date(stStr);
                    var etStr = curLesson.endtime;
                    curLesson.endtime = new Date(etStr);
                    if (isLessonCheckin(curLesson.id)){
                        curLesson.ci = true;
                        ciCount += 1;
                    }
                    else
                        curLesson.ci = false;                    

                }

                if($scope.theList.length>0){
                    $scope.checkinRate =  "总计 " + $scope.theList.length + " 节课,  签到 "  + ciCount + 
                    " 节课,  签到率 : "  + (ciCount*100/$scope.theList.length) + "%"
                }

            }
        );

    };

    


    // 得到课程列表
    Util.angular_get($http,
        '/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=100',
        function (ret) {

            $scope.courseList = ret.retlist;
        }
    );




    function getCheckinList () {

        g_studentCheckinList = null;

        var url = '/api/mgr/sq_mgr/?action=list_student_checkins&pagenum=1&pagesize=1000';
       
        url += '&studentid='+ studentid;

        Util.angular_get($http,
            url,
            function (ret) {
          

                g_studentCheckinList = ret.retlist;

                // // 解码 checkintime
                // for (var i=0; i<g_studentCheckinList.length;i++){

                //     var stStr = g_studentCheckinList[i].checkintime;
                //     g_studentCheckinList[i].checkintime = new Date(stStr);
                //     var stStr = g_studentCheckinList[i].lesson__starttime;
                //     g_studentCheckinList[i].lesson__starttime = new Date(stStr);
                // }

            }
        );

    };

    // 获取学生所有的签到信息
    getCheckinList();

    // 对于某节课，该学生是否签到
    function isLessonCheckin (lid) {
        
        // 解码 checkintime
        for (var i=0; i<g_studentCheckinList.length;i++){

            if(g_studentCheckinList[i].lesson__id == lid){
                return true;
            }

        }
        return false;
    }


});

