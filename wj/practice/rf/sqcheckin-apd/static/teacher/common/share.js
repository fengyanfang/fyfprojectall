/**
 * Created by pj on 2015/10/22.
 */


var getUrlParameter = function getUrlParameter(sParam) {
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
};


Util = {


    ajax_get : function (pUrl,pData,callBack,callBackOtherParamList){

        $.ajax({
            url:  pUrl,
            type: 'GET',
            data: pData,
            success: function (ret) {

                if (ret.retcode != 0){
                    if (ret.retcode === 302) window.top.location.href = ret.redirect;
                    alert('错误: ' + ret.reason);
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
                    if (ret.retcode === 302) window.top.location.href = ret.redirect;
                    alert('错误: ' + ret.reason);
                    return;
                }

                callBack(ret,callBackOtherParamList)

            },
            error:function (xhr, ajaxOptions, thrownError){
                if(xhr.status !=0) alert('HTTP 错误 : ' + xhr.status + thrownError);
            }

        });
    },


    angular_get: function ($http,pUrl,successCallBack) {

        $http({
            method: 'GET',
            url: pUrl
        })
        .success(function(ret) {
            if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
            if (successCallBack) successCallBack(ret);

        });
    },

    angular_post: function ($http,pUrl,pData,successCallBack) {

        $http({
            method: 'POST',
            url: pUrl,
            data: pData,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}

        })
        .success(function(ret) {
            if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
            if (successCallBack) successCallBack(ret);

        });
    },


    // pData 是对象， 比如 {action: "create", newgroupname:3}
    angular_post2: function ($http,pUrl,pDataObj,successCallBack) {

        $http({
            method: 'POST',
            url: pUrl,
            data: $.param(pDataObj),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}

        })
            .success(function(ret) {
                if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
                if (successCallBack) successCallBack(ret);

            });
    },

    angular_put: function ($http,pUrl,pData,successCallBack) {

        $http({
            method: 'PUT',
            url: pUrl,
            data: pData,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}

        })
            .success(function(ret) {
                if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
                if (successCallBack) successCallBack(ret);

            });
    },

    angular_delete: function ($http,pUrl,pData,successCallBack) {

        $http({
            method: 'DELETE',
            url: pUrl,
            data: pData,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}

        })
            .success(function(ret) {
                if (ret.retcode != 0){ if (ret.retcode === 302) window.top.location.href = ret.redirect;BootstrapDialog.alert('错误 : ' + ret.reason); return;}
                if (successCallBack) successCallBack(ret);

            });
    },

};



