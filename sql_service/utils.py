import re
from models import Parameter
from exception_handler import ParametersMismatch

# Extracts parameter and correspoding values from the given sql string


def extractParams(sql):
    value = ''
    value = sql

    if value.startswith(SqlStatement.INSERT):
        print('INSERT statement received')
        return parseInsertStatement(sql)

    return []


def parseInsertStatement(sql):
    parameters = []
    result = re.findall(Patterns.insert_value, sql)
    if len(result) == 2:
        columns = re.sub('[\(\)]', '', result[0]).split(',')
        values = re.sub('[\(\)]', '', result[1]).split(',')
        if len(columns) != len(values):
            raise ParametersMismatch(
                'Invalid query , Please verify the parameters and values',
                status_code=400)
        unkownKeyIndex = 0
        for i in range(0, len(columns)):
            value = values[i]
            if value != '?':
                key = value
            else:
                unkownKeyIndex = unkownKeyIndex+1
                key = '?' + str(unkownKeyIndex)
            parameters.append(Parameter(columns[i], value, key))
    return parameters


def construct(sql, parameters):
    result = sql
    for param in parameters:

        result = result.replace(param['key'], param['value'])
    return result


# List of REGEX patterns


class Patterns:
    # captures (a,b) (1,2) from 'table(a,b) values (1,2)'
    insert_value = '\([^)(]+\)'
    # captures a=? , b=1 from 'where a=? and b=?'
    clause = "[^\s]+(\s*([=><!]){1}\s*)[^\s]+"
    # captures a=? , b=1 from 'where a between 1 and 2'
    between = "[^\s]+(\s+(between|BETWEEN){1}\s+).+(\s+(and|AND){1}\s+)[^\s]+"

# List of SQL statements supported


class SqlStatement:
    INSERT = 'INSERT INTO'
    SELECT = 'SELECT'
    DELETE = 'DELETE'
    UPDATE = 'UPDATE'
