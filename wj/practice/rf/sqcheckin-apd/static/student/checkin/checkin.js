/**
 * Created by Patrick on 2015/11/26.
 */

frameApp.controller('checkinCtrl', function ($scope,$http,shareSvc,$timeout,$location) {



    $scope.currentPage = 1;
    $scope.pageSize = 50;


    $scope.filter={
        starttime:null,
        endtime:null
    };

    function getclessons() {
        shareSvc.util.get_my_checkinlessons(function(slessons){
            $scope.theList   = slessons;
        });
    }


    getclessons();


    $scope.checkin = function(lesson) {

        shareSvc.util.angular_post2('/api/student/sq_student/',
            {
                action:'checkin_lesson',
                lessonid:lesson.id
            },
            function(ret){

                BootstrapDialog.alert('签到成功');
                getclessons();


            }
        )
    }


});
