from examon_pcep_package import *
from examon_core.examon_in_memory_db import ExamonInMemoryDatabase
from examon_mongo.documents.question import Question
from examon_mongo.documents.metrics import Metrics


class Ingest:
    @staticmethod
    def run():
        inmemory_models = ExamonInMemoryDatabase.load()
        print(f'Ingesting {len(inmemory_models)} questions')

        for inmemory_model in inmemory_models:
            question = Question(
                unique_id=inmemory_model.unique_id,
                internal_id=inmemory_model.internal_id,
                function_src=inmemory_model.function_src,
                repository=inmemory_model.repository,
                hints=inmemory_model.hints,
                print_logs=inmemory_model.print_logs,
                tags=inmemory_model.tags,
                metrics=Metrics(
                    no_of_functions=inmemory_model.metrics.no_of_functions,
                    loc=inmemory_model.metrics.loc,
                    lloc=inmemory_model.metrics.lloc,
                    sloc=inmemory_model.metrics.sloc,
                    difficulty=inmemory_model.metrics.difficulty,
                    categorised_difficulty=inmemory_model.metrics.categorised_difficulty,
                    imports=inmemory_model.metrics.imports,
                    calls=inmemory_model.metrics.calls,
                    addCount=inmemory_model.metrics.counts['Add'],
                    aliasCount=inmemory_model.metrics.counts['Alias'],
                    andCount=inmemory_model.metrics.counts['And'],
                    annAssignCount=inmemory_model.metrics.counts['AnnAssign'],
                    argCount=inmemory_model.metrics.counts['Arg'],
                    argumentsCount=inmemory_model.metrics.counts['Arguments'],
                    assertCount=inmemory_model.metrics.counts['Assert'],
                    assignCount=inmemory_model.metrics.counts['Assign'],
                    asyncForCount=inmemory_model.metrics.counts['AsyncFor'],
                    asyncWithCount=inmemory_model.metrics.counts['AsyncWith'],
                    attributeCount=inmemory_model.metrics.counts['Attribute'],
                    augAssignCount=inmemory_model.metrics.counts['AugAssign'],
                    augLoadCount=inmemory_model.metrics.counts['AugLoad'],
                    augStoreCount=inmemory_model.metrics.counts['AugStore'],
                    awaitCount=inmemory_model.metrics.counts['Await'],
                    binOpCount=inmemory_model.metrics.counts['BinOp'],
                    bitAndCount=inmemory_model.metrics.counts['BitAnd'],
                    bitOrCount=inmemory_model.metrics.counts['BitOr'],
                    bitXorCount=inmemory_model.metrics.counts['BitXor'],
                    boolOpCount=inmemory_model.metrics.counts['BoolOp'],
                    breakCount=inmemory_model.metrics.counts['Break'],
                    bytesCount=inmemory_model.metrics.counts['Bytes'],
                    classDefCount=inmemory_model.metrics.counts['ClassDef'],
                    compareCount=inmemory_model.metrics.counts['Compare'],
                    comprehensionCount=inmemory_model.metrics.counts['Comprehension'],
                    constantCount=inmemory_model.metrics.counts['Constant'],
                    continueCount=inmemory_model.metrics.counts['Continue'],
                    delCount=inmemory_model.metrics.counts['Del'],
                    deleteCount=inmemory_model.metrics.counts['Delete'],
                    dictCompCount=inmemory_model.metrics.counts['DictComp'],
                    dictCount=inmemory_model.metrics.counts['Dict'],
                    divCount=inmemory_model.metrics.counts['Div'],
                    ellipsisCount=inmemory_model.metrics.counts['Ellipsis'],
                    eqCount=inmemory_model.metrics.counts['Eq'],
                    exceptHandlerCount=inmemory_model.metrics.counts['ExceptHandler'],
                    exprCount=inmemory_model.metrics.counts['Expr'],
                    expressionCount=inmemory_model.metrics.counts['Expression'],
                    floorDivCount=inmemory_model.metrics.counts['FloorDiv'],
                    forCount=inmemory_model.metrics.counts['For'],
                    formattedValueCount=inmemory_model.metrics.counts['FormattedValue'],
                    generatorExpCount=inmemory_model.metrics.counts['GeneratorExp'],
                    globalCount=inmemory_model.metrics.counts['Global'],
                    gtCount=inmemory_model.metrics.counts['Gt'],
                    gtECount=inmemory_model.metrics.counts['GtE'],
                    ifCount=inmemory_model.metrics.counts['If'],
                    ifExpCount=inmemory_model.metrics.counts['IfExp'],
                    inCount=inmemory_model.metrics.counts['In'],
                    indexCount=inmemory_model.metrics.counts['Index'],
                    invertCount=inmemory_model.metrics.counts['Invert'],
                    isCount=inmemory_model.metrics.counts['Is'],
                    isNotCount=inmemory_model.metrics.counts['IsNot'],
                    joinedStrCount=inmemory_model.metrics.counts['JoinedStr'],
                    keywordCount=inmemory_model.metrics.counts['Keyword'],
                    lShiftCount=inmemory_model.metrics.counts['LShift'],
                    lambdaCount=inmemory_model.metrics.counts['Lambda'],
                    listCompCount=inmemory_model.metrics.counts['ListComp'],
                    listCount=inmemory_model.metrics.counts['List'],
                    loadCount=inmemory_model.metrics.counts['Load'],
                    ltCount=inmemory_model.metrics.counts['Lt'],
                    ltECount=inmemory_model.metrics.counts['LtE'],
                    matMultCount=inmemory_model.metrics.counts['MatMult'],
                    modCount=inmemory_model.metrics.counts['Mod'],
                    multCount=inmemory_model.metrics.counts['Mult'],
                    nameConstantCount=inmemory_model.metrics.counts['NameConstant'],
                    nameCount=inmemory_model.metrics.counts['Name'],
                    nonlocalCount=inmemory_model.metrics.counts['Nonlocal'],
                    notCount=inmemory_model.metrics.counts['Not'],
                    notEqCount=inmemory_model.metrics.counts['NotEq'],
                    notInCount=inmemory_model.metrics.counts['NotIn'],
                    numCount=inmemory_model.metrics.counts['Num'],
                    orCount=inmemory_model.metrics.counts['Or'],
                    paramCount=inmemory_model.metrics.counts['Param'],
                    passCount=inmemory_model.metrics.counts['Pass'],
                    powCount=inmemory_model.metrics.counts['Pow'],
                    rShiftCount=inmemory_model.metrics.counts['RShift'],
                    raiseCount=inmemory_model.metrics.counts['Raise'],
                    returnCount=inmemory_model.metrics.counts['Return'],
                    setCompCount=inmemory_model.metrics.counts['SetComp'],
                    setCount=inmemory_model.metrics.counts['Set'],
                    sliceCount=inmemory_model.metrics.counts['Slice'],
                    starredCount=inmemory_model.metrics.counts['Starred'],
                    storeCount=inmemory_model.metrics.counts['Store'],
                    strCount=inmemory_model.metrics.counts['Str'],
                    subCount=inmemory_model.metrics.counts['Sub'],
                    subscriptCount=inmemory_model.metrics.counts['Subscript'],
                    suiteCount=inmemory_model.metrics.counts['Suite'],
                    tryCount=inmemory_model.metrics.counts['Try'],
                    tupleCount=inmemory_model.metrics.counts['Tuple'],
                    uAddCount=inmemory_model.metrics.counts['UAdd'],
                    uSubCount=inmemory_model.metrics.counts['USub'],
                    unaryOpCount=inmemory_model.metrics.counts['UnaryOp'],
                    whileCount=inmemory_model.metrics.counts['While'],
                    withCount=inmemory_model.metrics.counts['With'],
                    withitemCount=inmemory_model.metrics.counts['Withitem'],
                    yieldCount=inmemory_model.metrics.counts['Yield'],
                    yieldFromCount=inmemory_model.metrics.counts['YieldFrom']
                )
            )
            question.save()