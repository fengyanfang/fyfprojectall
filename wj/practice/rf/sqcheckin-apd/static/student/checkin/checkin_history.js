// 初始化


frameApp.controller('checkinhistoryCtrl', function ($scope,$http,shareSvc) {

    $scope.theList = null;

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

        var url = '/api/student/sq_student/?action=listmycheckinrecords&pagenum='+pageNumber  + '&pagesize='+$scope.pageSize;
        if ($scope.filter.starttime)
            url += '&starttime='+ encodeURIComponent(JSON.stringify($scope.filter.starttime));
        if ($scope.filter.endtime)
            url += '&endtime='+ encodeURIComponent(JSON.stringify($scope.filter.endtime));


        shareSvc.util.angular_get(
            url,
            function (ret) {

                if (ret.total==0 && $scope.currentPage>1){
                    $scope.currentPage-=1;
                    return;
                }


                $scope.theList = ret.retlist;
                $scope.totalNum = ret.total;


                // 解码 checkintime
                for (var i=0; i<$scope.theList.length;i++){

                    var stStr = $scope.theList[i].checkintime;
                    $scope.theList[i].checkintime = new Date(stStr);
                    var stStr = $scope.theList[i].lesson__starttime;
                    $scope.theList[i].lesson__starttime = new Date(stStr);

                }

            }
        );

    };

    $scope.pageChangeTo(1);



});

