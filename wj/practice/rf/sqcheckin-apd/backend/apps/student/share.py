# coding=utf-8

import traceback

from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import operator
import json




import logging
app_logger =  logging.getLogger("student")



def filter_search_by_keyword(result_queryset, param_dict, query_field):
    if param_dict.get('searchkeyword', ''):
        name_query_Q_list = []
        keywords_list = param_dict['searchkeyword'].split(' ')
        for keyword in keywords_list:
            name_query_Q_list.append(Q(**{query_field + '_icontains': keyword}))
        result_queryset = result_queryset.filter(
            reduce(operator.__or__, name_query_Q_list))
    return result_queryset


def filter_search_by_db_field(result_queryset, param_dict, search_fields_list):
    id_query_Q_list = []
    for key in search_fields_list:
        if key in param_dict:
            id_query_Q_list.append(
                Q(**{'{}__exact'.format(key): param_dict[key]}))
    if id_query_Q_list:
        result_queryset = result_queryset.filter(
            reduce(operator.__and__, id_query_Q_list)).distinct()
    return result_queryset


def get_queryset_result_pagination(result_queryset,
                                   param_dict,
                                   pagination_lower_limit):

    try:
        if param_dict['direction'] == 'ASC':
            result_queryset = result_queryset.filter(
                id__gt=param_dict['lastid'])[0:pagination_lower_limit]
        elif param_dict['direction'] == 'DESC':
            result_queryset = result_queryset.filter(
                id__lt=param_dict['firstid']).order_by('-id')[
                    0:pagination_lower_limit]
    except IndexError:
        return HttpResponse(
            json.dumps(
                {'retcode': 404, 'reason': '查询id范围出现错误。'}
            ),
            content_type='application/json'
        )

    return result_queryset
