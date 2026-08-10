# Query

使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query

<!--Device-distributedData-class Query--><!--Device-distributedData-class Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## and

```TypeScript
and(): Query
```

构造一个带有与条件的查询对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#and

<!--Device-Query-and(): Query--><!--Device-Query-and(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回查询对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value1");
    query.and();
    query.notEqualTo("field", "value2");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## beginGroup

```TypeScript
beginGroup(): Query
```

创建一个带有左括号的查询条件组。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#beginGroup

<!--Device-Query-beginGroup(): Query--><!--Device-Query-beginGroup(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.beginGroup();
    query.isNotNull("field");
    query.endGroup();
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## constructor

```TypeScript
constructor()
```

用于创建Query实例的构造函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#constructor

<!--Device-Query-constructor()--><!--Device-Query-constructor()-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## deviceId

```TypeScript
deviceId(deviceId: string): Query
```

添加设备ID作为key的前缀。

> **说明：**
> 
> 其中deviceId通过调用&lt;!--RP1--&gt;
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync)
> 方法得到。&lt;!--RP1End--&gt;deviceManager模块的接口均为系统接口，仅系统应用可用。
> > deviceId具体获取方式请参考[sync接口示例](arkts-arkdata-distributeddata-singlekvstore-i.md#sync)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#deviceId

<!--Device-Query-deviceId(deviceId: string): Query--><!--Device-Query-deviceId(deviceId: string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 指示查询的设备ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.deviceId("deviceId");
    console.log("query is " + query.getSqlLike());
} catch (e) {
    console.log("should be ok on Method Chaining : " + e);
}
```

## endGroup

```TypeScript
endGroup(): Query
```

创建一个带有右括号的查询条件组。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#endGroup

<!--Device-Query-endGroup(): Query--><!--Device-Query-endGroup(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.beginGroup();
    query.isNotNull("field");
    query.endGroup();
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## equalTo

```TypeScript
equalTo(field: string, value: number | string | boolean): Query
```

构造一个Query对象来查询具有指定字段的条目，其值等于指定的值。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#equalTo

<!--Device-Query-equalTo(field: string, value: number | string | boolean): Query--><!--Device-Query-equalTo(field: string, value: number | string | boolean): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| value | number \| string \| boolean | Yes | 表示指定的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.equalTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## getSqlLike

```TypeScript
getSqlLike(): string
```

获取Query对象的查询语句。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#getSqlLike

<!--Device-Query-getSqlLike(): string--><!--Device-Query-getSqlLike(): string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回一个字段列中包含对应子串的结果。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    let sql1 = query.getSqlLike();
    console.log("GetSqlLike sql=" + sql1);
} catch (e) {
    console.log("duplicated calls should be ok : " + e);
}
```

## greaterThan

```TypeScript
greaterThan(field: string, value: number | string | boolean): Query
```

构造一个Query对象以查询具有大于指定值的指定字段的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#greaterThan

<!--Device-Query-greaterThan(field: string, value: number | string | boolean): Query--><!--Device-Query-greaterThan(field: string, value: number | string | boolean): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| value | number \| string \| boolean | Yes | 表示指定的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.greaterThan("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: number | string): Query
```

构造一个Query对象以查询具有指定字段且值大于或等于指定值的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#greaterThanOrEqualTo

<!--Device-Query-greaterThanOrEqualTo(field: string, value: number | string): Query--><!--Device-Query-greaterThanOrEqualTo(field: string, value: number | string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| value | number \| string | Yes | 表示指定的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.greaterThanOrEqualTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## inNumber

```TypeScript
inNumber(field: string, valueList: number[]): Query
```

构造一个Query对象以查询具有指定字段的条目，其值在指定的值列表中。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#inNumber

<!--Device-Query-inNumber(field: string, valueList: number[]): Query--><!--Device-Query-inNumber(field: string, valueList: number[]): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| valueList | number[] | Yes | 表示指定的值列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.inNumber("field", [0, 1]);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## inString

```TypeScript
inString(field: string, valueList: string[]): Query
```

构造一个Query对象以查询具有指定字段的条目，其值在指定的字符串值列表中。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#inString

<!--Device-Query-inString(field: string, valueList: string[]): Query--><!--Device-Query-inString(field: string, valueList: string[]): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| valueList | string[] | Yes | 表示指定的字符串值列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.inString("field", ['test1', 'test2']);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## isNotNull

```TypeScript
isNotNull(field: string): Query
```

构造一个Query对象以查询具有值不为null的指定字段的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#isNotNull

<!--Device-Query-isNotNull(field: string): Query--><!--Device-Query-isNotNull(field: string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.isNotNull("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## isNull

```TypeScript
isNull(field: string): Query
```

构造一个Query对象以查询具有值为null的指定字段的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#isNull

<!--Device-Query-isNull(field: string): Query--><!--Device-Query-isNull(field: string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.isNull("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## lessThan

```TypeScript
lessThan(field: string, value: number | string): Query
```

构造一个Query对象以查询具有小于指定值的指定字段的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#lessThan

<!--Device-Query-lessThan(field: string, value: number | string): Query--><!--Device-Query-lessThan(field: string, value: number | string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| value | number \| string | Yes | 表示指定的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.lessThan("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: number | string): Query
```

构造一个Query对象以查询具有指定字段且值小于或等于指定值的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#lessThanOrEqualTo

<!--Device-Query-lessThanOrEqualTo(field: string, value: number | string): Query--><!--Device-Query-lessThanOrEqualTo(field: string, value: number | string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| value | number \| string | Yes | 表示指定的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.lessThanOrEqualTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## like

```TypeScript
like(field: string, value: string): Query
```

构造一个Query对象以查询具有与指定字符串值相似的指定字段的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#like

<!--Device-Query-like(field: string, value: string): Query--><!--Device-Query-like(field: string, value: string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| value | string | Yes | 表示指定的字符串值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.like("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## limit

```TypeScript
limit(total: number, offset: number): Query
```

构造一个Query对象来指定结果的数量和开始位置。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#limit

<!--Device-Query-limit(total: number, offset: number): Query--><!--Device-Query-limit(total: number, offset: number): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| total | number | Yes | 表示指定的结果数。 |
| offset | number | Yes | 表示起始位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
let total = 10;
let offset = 1;
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.limit(total, offset);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## notEqualTo

```TypeScript
notEqualTo(field: string, value: number | string | boolean): Query
```

构造一个Query对象以查询具有指定字段且值不等于指定值的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#notEqualTo

<!--Device-Query-notEqualTo(field: string, value: number | string | boolean): Query--><!--Device-Query-notEqualTo(field: string, value: number | string | boolean): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| value | number \| string \| boolean | Yes | 表示指定的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## notInNumber

```TypeScript
notInNumber(field: string, valueList: number[]): Query
```

构造一个Query对象以查询具有指定字段的条目，该字段的值不在指定的值列表中。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#notInNumber

<!--Device-Query-notInNumber(field: string, valueList: number[]): Query--><!--Device-Query-notInNumber(field: string, valueList: number[]): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| valueList | number[] | Yes | 表示指定的值列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.notInNumber("field", [0, 1]);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## notInString

```TypeScript
notInString(field: string, valueList: string[]): Query
```

构造一个Query对象以查询具有指定字段且值不在指定字符串值列表中的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#notInString

<!--Device-Query-notInString(field: string, valueList: string[]): Query--><!--Device-Query-notInString(field: string, valueList: string[]): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| valueList | string[] | Yes | 表示指定的字符串值列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.notInString("field", ['test1', 'test2']);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## or

```TypeScript
or(): Query
```

构造一个带有或条件的Query对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#or

<!--Device-Query-or(): Query--><!--Device-Query-or(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回查询对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value1");
    query.or();
    query.notEqualTo("field", "value2");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## orderByAsc

```TypeScript
orderByAsc(field: string): Query
```

构造一个Query对象，将查询结果按升序排序。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#orderByAsc

<!--Device-Query-orderByAsc(field: string): Query--><!--Device-Query-orderByAsc(field: string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.orderByAsc("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## orderByDesc

```TypeScript
orderByDesc(field: string): Query
```

构造一个Query对象，将查询结果按降序排序。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#orderByDesc

<!--Device-Query-orderByDesc(field: string): Query--><!--Device-Query-orderByDesc(field: string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.orderByDesc("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## prefixKey

```TypeScript
prefixKey(prefix: string): Query
```

创建具有指定键前缀的查询条件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#prefixKey

<!--Device-Query-prefixKey(prefix: string): Query--><!--Device-Query-prefixKey(prefix: string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| prefix | string | Yes | 表示指定的键前缀。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.prefixKey("$.name");
    query.prefixKey("0");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

## reset

```TypeScript
reset(): Query
```

重置Query对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#reset

<!--Device-Query-reset(): Query--><!--Device-Query-reset(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回重置的Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.equalTo("key", "value");
    console.log("query is " + query.getSqlLike());
    query.reset();
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("simply calls should be ok :" + e);
}
```

## setSuggestIndex

```TypeScript
setSuggestIndex(index: string): Query
```

设置一个指定的索引，将优先用于查询。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#setSuggestIndex

<!--Device-Query-setSuggestIndex(index: string): Query--><!--Device-Query-setSuggestIndex(index: string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | string | Yes | 指示要设置的索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.setSuggestIndex("$.name");
    query.setSuggestIndex("0");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
   console.log("duplicated calls should be ok :" + e);
}
```

## unlike

```TypeScript
unlike(field: string, value: string): Query
```

构造一个Query对象以查询具有与指定字符串值不相似的指定字段的条目。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Query#unlike

<!--Device-Query-unlike(field: string, value: string): Query--><!--Device-Query-unlike(field: string, value: string): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 表示指定字段，不能包含' ^ '。 |
| value | string | Yes | 表示指定的字符串值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) | 返回Query对象。 |

## Examples

```TypeScript
try {
    let query = new distributedData.Query();
    query.unlike("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

