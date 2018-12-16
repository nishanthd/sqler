import re
from models import Parameter
from enum import Enum
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
    result = re.findall(Patterns.brace,sql)
    if len(result) == 2:
        keys = re.sub('[\(\)]','',result[0]).split(',')
        values = re.sub('[\(\)]','',result[1]).split(',')
        if len(keys)!=len(values):
            raise ParametersMismatch('Invalid query , Please verify the parameters and values',status_code=400)
        for i in range(0,len(keys)):
            parameters.append(Parameter(keys[i],values[i]))

    return parameters;

# List of REGEX patterns
class Patterns:
    # captures (a,b) (1,2) from 'table(a,b) values (1,2)'
    brace = '\([^)(]+\)'
    # captures a=? , b=1 from 'where a=? and b=?'
    symbols = "[^\s]+(\s*([=><!]){1}\s*)[^\s]+"
    # captures a=? , b=1 from 'where a between 1 and 2'
    between = "[^\s]+(\s+(between|BETWEEN){1}\s+).+(\s+(and|AND){1}\s+)[^\s]+"

# List of SQL statements supported
class SqlStatement:
    INSERT = 'INSERT INTO'
    SELECT = 'SELECT'
    DELETE = 'DELETE'
    UPDATE = 'UPDATE'
