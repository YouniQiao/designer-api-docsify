# DataSharePredicates (System API)

Provides APIs for setting different **DataSharePredicates** objects. This type is not multi-thread safe. If a **DataSharePredicates** instance is operated by multiple threads at the same time in an application, use a lock for it.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-dataSharePredicates-class DataSharePredicates--><!--Device-dataSharePredicates-class DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dataSharePredicates } from 'dataSharePredicates';
```

## and

```TypeScript
and(): DataSharePredicates
```

Creates a **DataSharePredicates** object to add the AND condition. Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-and(): DataSharePredicates--><!--Device-DataSharePredicates-and(): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| Type | Description |
| --- | --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) | DataSharePredicates** object with the AND operator. |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "lisi")
    .and()
    .equalTo("SALARY", 200.5);
```

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to search for the records in the specified column that are equal to the given value. Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-equalTo(field: string, value: ValueType): DataSharePredicates--><!--Device-DataSharePredicates-equalTo(field: string, value: ValueType): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table.If this parameter is set to **undefined** or **null**, the predicate used is invalid. |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | Yes | Value to match.If this parameter is set to **undefined** or **null**, the predicate used is invalid. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) | DataSharePredicates** object created. |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "Rose");
```

## in

```TypeScript
in(field: string, value: Array<ValueType>): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is within the specified range. Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-in(field: string, value: Array<ValueType>): DataSharePredicates--><!--Device-DataSharePredicates-in(field: string, value: Array<ValueType>): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table.If this parameter is set to **undefined** or **null**, the predicate used is invalid. |
| value | Array&lt;[ValueType](arkts-arkdata-valuetype-t.md)&gt; | Yes | Array of the values to match. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) | DataSharePredicates** object created. |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.in("AGE", [18, 20]);
```

## inValues

```TypeScript
inValues(field: string, value: Array<ValueType>): DataSharePredicates
```

Configure {@code DataSharePredicates} to match the specified field whose data type is ValueType array and values are within a given range. Currently only used for RDB and KVDB(schema).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-inValues(field: string, value: Array<ValueType>): DataSharePredicates--><!--Device-DataSharePredicates-inValues(field: string, value: Array<ValueType>): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Indicates the column name in the database table. |
| value | Array&lt;[ValueType](arkts-arkdata-valuetype-t.md)&gt; | Yes | Indicates the values to match with DataSharePredicates. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) | Returns DataSharePredicates that matches the specified field. |

## limit

```TypeScript
limit(total: int, offset: int): DataSharePredicates
```

Creates a **DataSharePredicates** object to specify the number of records in the result and the start position. Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-limit(total: int, offset: int): DataSharePredicates--><!--Device-DataSharePredicates-limit(total: int, offset: int): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| total | int | Yes | Maximum number of records.If the KV store is used and **total** is **undefined** or **null**, the maximum number of records is 0. For details about the value range, see the description of this parameter in [limit](arkts-arkdata-distributedkvstore-query-c.md#limit).If the RDB store is used and **total** is **undefined** or **null**, the maximum number of records is not limited. For details about the value range, see the description of this parameter in [limitAs](arkts-arkdata-distributedkvstore-query-c.md#limit). |
| offset | int | Yes | Start position of the query result.If this parameter is set to **undefined** or **null**, the start position is the beginning of the result set.For details about the value range in a KV store, see the description of this parameter in [limit](arkts-arkdata-distributedkvstore-query-c.md#limit).For details about the value range in an RDB store, see the description of the **rowOffset** parameter in [offsetAs](arkts-arkdata-relationalstore-rdbpredicates-c.md#offsetAs). |

**Return value:**

| Type | Description |
| --- | --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) | DataSharePredicates** object created. |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "Rose").limit(10, 3);
```

## notInValues

```TypeScript
notInValues(field: string, value: Array<ValueType>): DataSharePredicates
```

Configure {@code DataSharePredicates} to match the specified field whose data type is String array and values are out of a given range. Currently only used for RDB and KVDB(schema).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-notInValues(field: string, value: Array<ValueType>): DataSharePredicates--><!--Device-DataSharePredicates-notInValues(field: string, value: Array<ValueType>): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Indicates the column name in the database table. |
| value | Array&lt;[ValueType](arkts-arkdata-valuetype-t.md)&gt; | Yes | Indicates the values to match with DataSharePredicates. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) | Returns DataSharePredicates that matches the specified field. |

## orderByAsc

```TypeScript
orderByAsc(field: string): DataSharePredicates
```

Creates a **DataSharePredicates** object that sorts records in ascending order. Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-orderByAsc(field: string): DataSharePredicates--><!--Device-DataSharePredicates-orderByAsc(field: string): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table.If this parameter is set to **undefined** or **null**, the predicate used is invalid. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) | DataSharePredicates** object created. |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.orderByAsc("AGE");
```

## orderByDesc

```TypeScript
orderByDesc(field: string): DataSharePredicates
```

Creates a **DataSharePredicates** object that sorts data in descending order. Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-orderByDesc(field: string): DataSharePredicates--><!--Device-DataSharePredicates-orderByDesc(field: string): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table.If this parameter is set to **undefined** or **null**, the predicate used is invalid. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) | DataSharePredicates** object created. |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.orderByDesc("AGE");
```

