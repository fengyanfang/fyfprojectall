// 初始化



frameApp.controller('studentcheckinhistoryCtrl', function ($scope,$http,shareSvc,$stateParams) {

    var studentid = $stateParams.uid;
    $scope.checkinList = null;

    $scope.currentPage = 1;
    $scope.totalNum = 0;
    $scope.pageSize = 15;


    $scope.filter={
        starttime:null,
        endtime:null
    };


    // $scope.filter.starttime.setHours(0,0,0,0);
    // $scope.filter.endtime.setHours(0,0,0,0);

    $scope.pageChangeTo = function(pageNumber) {

        $scope.checkinList = null;

        var url = '/api/teacher/sq_teacher/?action=list_student_checkins&pagenum=1&pagesize=1000';
        if ($scope.filter.starttime)
            url += '&starttime='+ encodeURIComponent(JSON.stringify($scope.filter.starttime));
        if ($scope.filter.endtime)
            url += '&endtime='+ encodeURIComponent(JSON.stringify($scope.filter.endtime));
        url += '&studentid='+ studentid;

        Util.angular_get($http,
            url,
            function (ret) {

                if (ret.total==0 && $scope.currentPage>1){
                    $scope.currentPage-=1;
                    return;
                }


                $scope.checkinList = ret.retlist;
                $scope.totalNum = ret.total;


                // 解码 checkintime
                for (var i=0; i<$scope.checkinList.length;i++){

                    var stStr = $scope.checkinList[i].checkintime;
                    $scope.checkinList[i].checkintime = new Date(stStr);
                    var stStr = $scope.checkinList[i].lesson__starttime;
                    $scope.checkinList[i].lesson__starttime = new Date(stStr);

                }

            }
        );

    };

    $scope.pageChangeTo(1);



});

