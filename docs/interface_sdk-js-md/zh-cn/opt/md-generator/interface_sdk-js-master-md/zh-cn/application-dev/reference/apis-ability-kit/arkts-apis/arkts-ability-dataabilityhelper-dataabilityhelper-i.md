# DataAbilityHelper

可以通过[acquireDataAbilityHelper](arkts-ability-featureability-acquiredataabilityhelper-f.md#acquiredataabilityhelper)接口获取DataAbilityHelper对象。

**起始版本：** 7

<!--Device-unnamed-export interface DataAbilityHelper--><!--Device-unnamed-export interface DataAbilityHelper-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

## batchInsert

```TypeScript
batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>, callback: AsyncCallback<number>): void
```

将多个数据记录插入数据库。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>, callback: AsyncCallback<number>): void--><!--Device-DataAbilityHelper-batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| valuesBuckets | Array&lt;rdb.ValuesBucket&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## batchInsert

```TypeScript
batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>): Promise<number>
```

将多个数据记录插入数据库。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>): Promise<number>--><!--Device-DataAbilityHelper-batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>): Promise<number>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| valuesBuckets | Array&lt;rdb.ValuesBucket&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

## call

```TypeScript
call(uri: string, method: string, arg: string, extras: PacMap, callback: AsyncCallback<PacMap>): void
```

调用DataAbility的扩展接口。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-call(uri: string, method: string, arg: string, extras: PacMap, callback: AsyncCallback<PacMap>): void--><!--Device-DataAbilityHelper-call(uri: string, method: string, arg: string, extras: PacMap, callback: AsyncCallback<PacMap>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| method | string | 是 |
| arg | string | 是 |
| extras | [PacMap](arkts-ability-dataabilityhelper-pacmap-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PacMap&gt; | 是 |

## call

```TypeScript
call(uri: string, method: string, arg: string, extras: PacMap): Promise<PacMap>
```

调用DataAbility的扩展接口。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-call(uri: string, method: string, arg: string, extras: PacMap): Promise<PacMap>--><!--Device-DataAbilityHelper-call(uri: string, method: string, arg: string, extras: PacMap): Promise<PacMap>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| method | string | 是 |
| arg | string | 是 |
| extras | [PacMap](arkts-ability-dataabilityhelper-pacmap-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;PacMap&gt; |

## delete

```TypeScript
delete(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void
```

从数据库中删除一个或多个数据记录。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-delete(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void--><!--Device-DataAbilityHelper-delete(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataAbility.DataAbilityPredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## delete

```TypeScript
delete(uri: string, predicates?: dataAbility.DataAbilityPredicates): Promise<number>
```

从数据库中删除一个或多个数据记录。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-delete(uri: string, predicates?: dataAbility.DataAbilityPredicates): Promise<number>--><!--Device-DataAbilityHelper-delete(uri: string, predicates?: dataAbility.DataAbilityPredicates): Promise<number>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataAbility.DataAbilityPredicates | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

## delete

```TypeScript
delete(uri: string, callback: AsyncCallback<number>): void
```

predicates筛选条件为空，自定义数据库删除数据记录的处理逻辑。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-delete(uri: string, callback: AsyncCallback<number>): void--><!--Device-DataAbilityHelper-delete(uri: string, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## denormalizeUri

```TypeScript
denormalizeUri(uri: string, callback: AsyncCallback<string>): void
```

将由normalizeUri（uri）生成的给定规范化uri转换为非规范化uri。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-denormalizeUri(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataAbilityHelper-denormalizeUri(uri: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## denormalizeUri

```TypeScript
denormalizeUri(uri: string): Promise<string>
```

将由normalizeUri（uri）生成的给定规范化uri转换为非规范化uri。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-denormalizeUri(uri: string): Promise<string>--><!--Device-DataAbilityHelper-denormalizeUri(uri: string): Promise<string>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

## executeBatch

```TypeScript
executeBatch(
    uri: string,
    operations: Array<DataAbilityOperation>,
    callback: AsyncCallback<Array<DataAbilityResult>>
  ): void
```

批量操作数据库中的数据。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-executeBatch(    uri: string,    operations: Array<DataAbilityOperation>,    callback: AsyncCallback<Array<DataAbilityResult>>  ): void--><!--Device-DataAbilityHelper-executeBatch(    uri: string,    operations: Array<DataAbilityOperation>,    callback: AsyncCallback<Array<DataAbilityResult>>  ): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| operations | Array&lt;[DataAbilityOperation](arkts-ability-dataabilityoperation-dataabilityoperation-i.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[DataAbilityResult](arkts-ability-dataabilityresult-dataabilityresult-i.md)&gt;&gt; | 是 |

## executeBatch

```TypeScript
executeBatch(uri: string, operations: Array<DataAbilityOperation>): Promise<Array<DataAbilityResult>>
```

批量操作数据库中的数据。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-executeBatch(uri: string, operations: Array<DataAbilityOperation>): Promise<Array<DataAbilityResult>>--><!--Device-DataAbilityHelper-executeBatch(uri: string, operations: Array<DataAbilityOperation>): Promise<Array<DataAbilityResult>>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| operations | Array&lt;[DataAbilityOperation](arkts-ability-dataabilityoperation-dataabilityoperation-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[DataAbilityResult](arkts-ability-dataabilityresult-dataabilityresult-i.md)&gt;&gt; |

## getFileTypes

```TypeScript
getFileTypes(uri: string, mimeTypeFilter: string, callback: AsyncCallback<Array<string>>): void
```

获取支持的文件媒体资源类型。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-getFileTypes(uri: string, mimeTypeFilter: string, callback: AsyncCallback<Array<string>>): void--><!--Device-DataAbilityHelper-getFileTypes(uri: string, mimeTypeFilter: string, callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| mimeTypeFilter | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## getFileTypes

```TypeScript
getFileTypes(uri: string, mimeTypeFilter: string): Promise<Array<string>>
```

获取支持的文件媒体资源类型。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-getFileTypes(uri: string, mimeTypeFilter: string): Promise<Array<string>>--><!--Device-DataAbilityHelper-getFileTypes(uri: string, mimeTypeFilter: string): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| mimeTypeFilter | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

## getType

```TypeScript
getType(uri: string, callback: AsyncCallback<string>): void
```

获取给定uri指向数据的媒体资源类型。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-getType(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataAbilityHelper-getType(uri: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getType

```TypeScript
getType(uri: string): Promise<string>
```

获取给定uri指向数据的媒体资源类型。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-getType(uri: string): Promise<string>--><!--Device-DataAbilityHelper-getType(uri: string): Promise<string>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

## insert

```TypeScript
insert(uri: string, valuesBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void
```

将单个数据记录插入数据库。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-insert(uri: string, valuesBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void--><!--Device-DataAbilityHelper-insert(uri: string, valuesBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| valuesBucket | rdb.ValuesBucket | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## insert

```TypeScript
insert(uri: string, valuesBucket: rdb.ValuesBucket): Promise<number>
```

将单个数据记录插入数据库。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-insert(uri: string, valuesBucket: rdb.ValuesBucket): Promise<number>--><!--Device-DataAbilityHelper-insert(uri: string, valuesBucket: rdb.ValuesBucket): Promise<number>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| valuesBucket | rdb.ValuesBucket | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

## normalizeUri

```TypeScript
normalizeUri(uri: string, callback: AsyncCallback<string>): void
```

将引用数据功能的给定uri转换为规范化uri。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-normalizeUri(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataAbilityHelper-normalizeUri(uri: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## normalizeUri

```TypeScript
normalizeUri(uri: string): Promise<string>
```

将引用数据功能的给定uri转换为规范化uri。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-normalizeUri(uri: string): Promise<string>--><!--Device-DataAbilityHelper-normalizeUri(uri: string): Promise<string>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

## notifyChange

```TypeScript
notifyChange(uri: string, callback: AsyncCallback<void>): void
```

通知注册的观察者，uri指定数据的数据变化。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-notifyChange(uri: string, callback: AsyncCallback<void>): void--><!--Device-DataAbilityHelper-notifyChange(uri: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## notifyChange

```TypeScript
notifyChange(uri: string): Promise<void>
```

通知注册的观察者，uri指定数据的数据变化。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-notifyChange(uri: string): Promise<void>--><!--Device-DataAbilityHelper-notifyChange(uri: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## off('dataChange')

```TypeScript
off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void
```

注销观察者以停止监听uri指定数据的数据变化通知。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void--><!--Device-DataAbilityHelper-off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataChange' | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

## on('dataChange')

```TypeScript
on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void
```

注册观察者以监听uri指定数据的数据变化通知。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void--><!--Device-DataAbilityHelper-on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataChange' | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## openFile

```TypeScript
openFile(uri: string, mode: string, callback: AsyncCallback<number>): void
```

打开指定uri对应的文件，返回文件描述符。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-openFile(uri: string, mode: string, callback: AsyncCallback<number>): void--><!--Device-DataAbilityHelper-openFile(uri: string, mode: string, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| mode | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## openFile

```TypeScript
openFile(uri: string, mode: string): Promise<number>
```

打开指定uri对应的文件，返回文件描述符。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-openFile(uri: string, mode: string): Promise<number>--><!--Device-DataAbilityHelper-openFile(uri: string, mode: string): Promise<number>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

## query

```TypeScript
query(
    uri: string,
    columns: Array<string>,
    predicates: dataAbility.DataAbilityPredicates,
    callback: AsyncCallback<ResultSet>
  ): void
```

查询数据库中的数据。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-query(    uri: string,    columns: Array<string>,    predicates: dataAbility.DataAbilityPredicates,    callback: AsyncCallback<ResultSet>  ): void--><!--Device-DataAbilityHelper-query(    uri: string,    columns: Array<string>,    predicates: dataAbility.DataAbilityPredicates,    callback: AsyncCallback<ResultSet>  ): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| columns | Array&lt;string&gt; | 是 |
| predicates | dataAbility.DataAbilityPredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

## query

```TypeScript
query(uri: string, callback: AsyncCallback<ResultSet>): void
```

查询数据库中的数据。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-query(uri: string, callback: AsyncCallback<ResultSet>): void--><!--Device-DataAbilityHelper-query(uri: string, callback: AsyncCallback<ResultSet>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

## query

```TypeScript
query(uri: string, columns: Array<string>, callback: AsyncCallback<ResultSet>): void
```

查询数据库中的数据。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-query(uri: string, columns: Array<string>, callback: AsyncCallback<ResultSet>): void--><!--Device-DataAbilityHelper-query(uri: string, columns: Array<string>, callback: AsyncCallback<ResultSet>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| columns | Array&lt;string&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

## query

```TypeScript
query(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<ResultSet>): void
```

查询数据库中的数据。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-query(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<ResultSet>): void--><!--Device-DataAbilityHelper-query(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<ResultSet>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataAbility.DataAbilityPredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

## query

```TypeScript
query(uri: string, columns?: Array<string>, predicates?: dataAbility.DataAbilityPredicates): Promise<ResultSet>
```

查询数据库中的数据。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-query(uri: string, columns?: Array<string>, predicates?: dataAbility.DataAbilityPredicates): Promise<ResultSet>--><!--Device-DataAbilityHelper-query(uri: string, columns?: Array<string>, predicates?: dataAbility.DataAbilityPredicates): Promise<ResultSet>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| columns | Array&lt;string&gt; | 否 |
| predicates | dataAbility.DataAbilityPredicates | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;ResultSet&gt; |

## update

```TypeScript
update(
    uri: string,
    valuesBucket: rdb.ValuesBucket,
    predicates: dataAbility.DataAbilityPredicates,
    callback: AsyncCallback<number>
  ): void
```

更新数据库中的数据记录。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-update(    uri: string,    valuesBucket: rdb.ValuesBucket,    predicates: dataAbility.DataAbilityPredicates,    callback: AsyncCallback<number>  ): void--><!--Device-DataAbilityHelper-update(    uri: string,    valuesBucket: rdb.ValuesBucket,    predicates: dataAbility.DataAbilityPredicates,    callback: AsyncCallback<number>  ): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| valuesBucket | rdb.ValuesBucket | 是 |
| predicates | dataAbility.DataAbilityPredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## update

```TypeScript
update(uri: string, valuesBucket: rdb.ValuesBucket, predicates?: dataAbility.DataAbilityPredicates): Promise<number>
```

更新数据库中的数据记录。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-update(uri: string, valuesBucket: rdb.ValuesBucket, predicates?: dataAbility.DataAbilityPredicates): Promise<number>--><!--Device-DataAbilityHelper-update(uri: string, valuesBucket: rdb.ValuesBucket, predicates?: dataAbility.DataAbilityPredicates): Promise<number>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| valuesBucket | rdb.ValuesBucket | 是 |
| predicates | dataAbility.DataAbilityPredicates | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

## update

```TypeScript
update(uri: string, valuesBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void
```

predicates筛选条件为空，自定义更新数据库的处理逻辑。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DataAbilityHelper-update(uri: string, valuesBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void--><!--Device-DataAbilityHelper-update(uri: string, valuesBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| valuesBucket | rdb.ValuesBucket | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |
