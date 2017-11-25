/**
 * Created by Patrick on 2015/11/26.
 */


frameApp.controller('homeCtrl', function ($scope,$http,shareSvc,$timeout,$location) {



    $scope.currentPage = 1;
    $scope.pageSize = 20;


    $scope.filter={
        starttime:null,
        endtime:null
    };

    shareSvc.util.get_my_scheduledlessons(function(slessons){

        $scope.theList   = slessons;
        // $scope.avatar_url = info.avatar_url;

    });

    // $scope.pageChangeTo = function(pageNumber) {
    //
    //     var url = '/api/mgr/sq_mgr/?action=list_lesson&pagenum='+pageNumber  + '&pagesize='+$scope.pageSize;
    //     if ($scope.filter.starttime)
    //         url += '&starttime='+ encodeURIComponent(JSON.stringify($scope.filter.starttime));
    //     if ($scope.filter.endtime)
    //         url += '&endtime='+ encodeURIComponent(JSON.stringify($scope.filter.endtime));
    //
    //
    //     Util.angular_get($http,
    //         url,
    //         function (ret) {
    //
    //             if (ret.total==0 && $scope.currentPage>1){
    //                 $scope.currentPage-=1;
    //                 return;
    //             }
    //
    //
    //             $scope.theList = ret.retlist;
    //             $scope.totalNum = ret.total;
    //
    //
    //             // 解码 starttime, endtime
    //             for (var i=0; i<$scope.theList.length;i++){
    //
    //                 var stStr = $scope.theList[i].starttime;
    //                 $scope.theList[i].starttime = new Date(stStr);
    //                 var etStr = $scope.theList[i].endtime;
    //                 $scope.theList[i].endtime = new Date(etStr);
    //
    //             }
    //
    //         }
    //     );
    //
    // };
    //
    // $scope.pageChangeTo(1);





    // shareSvc.util.angular_get(
    //     '/api/student/yj_notice/?action=get_my_notice',
    //     function(ret) {
    //         $scope.resultlist = ret.retlist;
    //         $timeout(
    //             function(){
    //                 createBannerSlider();
    //             },100
    //         )
    //
    //     }
    // );



});
