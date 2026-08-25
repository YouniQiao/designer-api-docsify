# Query

Provides methods to create a **Query** object, which defines different data query criteria. A **Query** object supports a maximum of 256 predicates.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## and

```TypeScript
and(): Query
```

Creates a **Query** object with the AND condition.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## beginGroup

```TypeScript
beginGroup(): Query
```

Creates a **Query** object for a query condition group with a left parenthesis.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## constructor

```TypeScript
constructor()
```

Defines a constructor used to create a **Query** instance.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## deviceId

```TypeScript
deviceId(deviceId: string): Query
```

Creates a **Query** object with the device ID as the key prefix.

> **NOTE：**&gt;
> **deviceId** can be obtained by
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> .
> 
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributedkvstore-syncmode-e.md).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [deviceId](#deviceid) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## endGroup

```TypeScript
endGroup(): Query
```

Creates a **Query** object for a query condition group with a right parenthesis.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: number | number | string | boolean): Query
```

Creates a **Query** object to match the specified field whose value is equal to the given value.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | number \| number \| string \| boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getSqlLike

```TypeScript
getSqlLike(): string
```

Obtains the query statement of the **Query** object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## greaterThan

```TypeScript
greaterThan(field: string, value: number | number | string | boolean): Query
```

Creates a **Query** object to match the specified field whose value is greater than the specified value.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | number \| number \| string \| boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: number | number | string): Query
```

Creates a **Query** object to match the specified field whose value is greater than or equal to the specified value.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | number \| number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## inNumber

```TypeScript
inNumber(field: string, valueList: number[] | number[]): Query
```

Creates a **Query** object to match the specified field whose value is within the specified list of numbers.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| valueList | number[] \| number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## inString

```TypeScript
inString(field: string, valueList: string[]): Query
```

Creates a **Query** object to match the specified field whose value is within the specified list of strings.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| valueList | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## isNotNull

```TypeScript
isNotNull(field: string): Query
```

Creates a **Query** object to match the specified field whose value is not **null**.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## isNull

```TypeScript
isNull(field: string): Query
```

Creates a **Query** object to match the specified field whose value is **null**.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## lessThan

```TypeScript
lessThan(field: string, value: number | number | string): Query
```

Creates a **Query** object to match the specified field whose value is less than the specified value.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | number \| number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: number | number | string): Query
```

Creates a **Query** object to match the specified field whose value is less than or equal to the specified value.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | number \| number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## like

```TypeScript
like(field: string, value: string): Query
```

Creates a **Query** object to match the specified field whose value is similar to the specified string.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## limit

```TypeScript
limit(total: number, offset: number): Query
```

Creates a **Query** object to specify the number of records of the query result and where to start. This API must be called after the invocation of the **orderByAsc()**, **orderByDesc()**, and the query APIs of the **Query** object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| total | number | Yes |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: number | number | string | boolean): Query
```

Creates a **Query** object to match the specified field whose value is not equal to the specified value.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | number \| number \| string \| boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## notInNumber

```TypeScript
notInNumber(field: string, valueList: number[] | number[]): Query
```

Creates a **Query** object to match the specified field whose value is not within the specified list of numbers.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| valueList | number[] \| number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## notInString

```TypeScript
notInString(field: string, valueList: string[]): Query
```

Creates a **Query** object to match the specified field whose value is not within the specified list of strings.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| valueList | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## or

```TypeScript
or(): Query
```

Creates a **Query** object with the OR condition.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## orderByAsc

```TypeScript
orderByAsc(field: string): Query
```

Creates a **Query** object to sort the query results in ascending order.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## orderByDesc

```TypeScript
orderByDesc(field: string): Query
```

Creates a **Query** object to sort the query results in descending order.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## prefixKey

```TypeScript
prefixKey(prefix: string): Query
```

Creates a **Query** object with a specified key prefix.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| prefix | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## reset

```TypeScript
reset(): Query
```

Resets the **Query** object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## setSuggestIndex

```TypeScript
setSuggestIndex(index: string): Query
```

Creates a **Query** object with an index preferentially used for query.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## unlike

```TypeScript
unlike(field: string, value: string): Query
```

Creates a **Query** object to match the specified field whose value is not similar to the specified string.

> **NOTE：**&gt;
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md).&gt;
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
