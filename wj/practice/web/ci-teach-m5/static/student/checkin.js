frameApp.controller('checkinCtrl', function ($scope,$http,shareSvc,$timeout,$location) {

    $scope.currentPage = 1;
    $scope.pageSize = 50;

    function getclessons() {

        Util.angular_get($http,
            '/api/student?action=list_ci_lesson',
            function(ret){

                // 解码 starttime, endtime
                for (var i=0; i<ret.retlist.length;i++){

                    var stStr = ret.retlist[i].starttime;
                    ret.retlist[i].starttime = new Date(stStr);
                    var etStr = ret.retlist[i].endtime;
                    ret.retlist[i].endtime = new Date(etStr);

                }

                $scope.theList   = ret.retlist;

            }
        )
    }


    getclessons();


    $scope.checkin = function(lesson) {

        Util.angular_post2($http,'/api/student',
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
