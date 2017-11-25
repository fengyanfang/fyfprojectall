
GUI_base = {

};


BaseUtil={
    getUrlParameter : function (sParam) {
        var sPageURL = decodeURIComponent(window.location.search.substring(1)),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;

        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : sParameterName[1];
            }
        }
    },

    ajax_get : function (pUrl,pData,callBack,callBackOtherParamList){

        $.ajax({
            url:  pUrl,
            type: 'GET',
            data: pData,
            success: function (ret) {
                if (ret.retcode != 0){
                    BootstrapDialog.alert('错误 : ' + ret.reason);
                    return;
                }

                callBack(ret,callBackOtherParamList)

            },
            error:function (xhr, ajaxOptions, thrownError){
                if(xhr.status !=0) alert('HTTP 错误 : ' + xhr.status + thrownError);
            }

        });
    },
    ajax_post : function (pUrl,pData,callBack,callBackOtherParamList){

        $.ajax({
            url:  pUrl,
            type: 'POST',
            data: pData,
            success: function (ret) {
                if (ret.retcode != 0){
                    BootstrapDialog.alert('错误 : ' + ret.reason);
                    return;
                }

                callBack(ret,callBackOtherParamList)

            },
            error:function (xhr, ajaxOptions, thrownError){
                if(xhr.status !=0) alert('HTTP 错误 : ' + xhr.status + thrownError);
            }

        });
    },




};





AngularUtil={


    grade_table : undefined,

    getGradeTable : function ($http,api_type,callback){


        if (AngularUtil.grade_table){
            callback && callback(AngularUtil.grade_table);;
        }

        $http.get('/api/%s/yj_grades/'.replace('%s',api_type)).success(function(ret) {
            if (ret.retcode != 0){ BootstrapDialog.alert('错误 : ' + ret.reason); return;}

            for (var i = 0; i < ret.retlist.length; i++) {
                var one  = ret.retlist[i]; var id = one[0]; var name = one[1];
                AngularUtil.grade_table[id] = name;

            }

            callback && callback(AngularUtil.grade_table);
        });
    },


};