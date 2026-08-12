# Query

Provides methods to create a **Query** object, which defines different data query criteria. A **Query** object supports a maximum of 256 predicates.

**Since:** 9

<!--Device-distributedKVStore-class Query--><!--Device-distributedKVStore-class Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## and

```TypeScript
and(): Query
```

Creates a **Query** object with the AND condition.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-and(): Query--><!--Device-Query-and(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo('field', 'value1');
      query.and();
      query.notEqualTo('field', 'value2');
      console.info('query is ' + query.getSqlLike());
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## beginGroup

```TypeScript
beginGroup(): Query
```

Creates a **Query** object for a query condition group with a left parenthesis.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-beginGroup(): Query--><!--Device-Query-beginGroup(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.beginGroup();
      query.isNotNull('field');
      query.endGroup();
      console.info('query is ' + query.getSqlLike());
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## constructor

```TypeScript
constructor()
```

Defines a constructor used to create a **Query** instance.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-constructor()--><!--Device-Query-constructor()-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## deviceId

```TypeScript
deviceId(deviceId: string): Query
```

Creates a **Query** object with the device ID as the key prefix.

> **NOTE：**
> 
> **deviceId** can be obtained by
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getAvailableDeviceListSync)
> .
> > For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributedkvstore-syncmode-e.md#SyncMode).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-deviceId(deviceId: string): Query--><!--Device-Query-deviceId(deviceId: string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.deviceId('deviceId');
      console.info(`query is ${query.getSqlLike()}`);
    }
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## endGroup

```TypeScript
endGroup(): Query
```

Creates a **Query** object for a query condition group with a right parenthesis.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-endGroup(): Query--><!--Device-Query-endGroup(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.beginGroup();
      query.isNotNull('field');
      query.endGroup();
      console.info('query is ' + query.getSqlLike());
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## equalTo

```TypeScript
equalTo(field: string, value: number | number | string | boolean): Query
```

Creates a **Query** object to match the specified field whose value is equal to the given value.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-equalTo(field: string, value: long | double | string | boolean): Query--><!--Device-Query-equalTo(field: string, value: long | double | string | boolean): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getSqlLike

```TypeScript
getSqlLike(): string
```

Obtains the query statement of the **Query** object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-getSqlLike(): string--><!--Device-Query-getSqlLike(): string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      let sql1 = query.getSqlLike();
      console.info(`GetSqlLike sql= ${sql1}`);
    }
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## greaterThan

```TypeScript
greaterThan(field: string, value: number | number | string | boolean): Query
```

Creates a **Query** object to match the specified field whose value is greater than the specified value.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-greaterThan(field: string, value: long | double | string | boolean): Query--><!--Device-Query-greaterThan(field: string, value: long | double | string | boolean): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: number | number | string): Query
```

Creates a **Query** object to match the specified field whose value is greater than or equal to the specified value.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-greaterThanOrEqualTo(field: string, value: long | double | string): Query--><!--Device-Query-greaterThanOrEqualTo(field: string, value: long | double | string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## inNumber

```TypeScript
inNumber(field: string, valueList: number[] | number[]): Query
```

Creates a **Query** object to match the specified field whose value is within the specified list of numbers.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-inNumber(field: string, valueList: long[] | double[]): Query--><!--Device-Query-inNumber(field: string, valueList: long[] | double[]): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## inString

```TypeScript
inString(field: string, valueList: string[]): Query
```

Creates a **Query** object to match the specified field whose value is within the specified list of strings.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-inString(field: string, valueList: string[]): Query--><!--Device-Query-inString(field: string, valueList: string[]): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.inString('field', ['test1', 'test2']);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## isNotNull

```TypeScript
isNotNull(field: string): Query
```

Creates a **Query** object to match the specified field whose value is not **null**.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-isNotNull(field: string): Query--><!--Device-Query-isNotNull(field: string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.isNotNull('field');
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## isNull

```TypeScript
isNull(field: string): Query
```

Creates a **Query** object to match the specified field whose value is **null**.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-isNull(field: string): Query--><!--Device-Query-isNull(field: string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.isNull('field');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## lessThan

```TypeScript
lessThan(field: string, value: number | number | string): Query
```

Creates a **Query** object to match the specified field whose value is less than the specified value.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-lessThan(field: string, value: long | double | string): Query--><!--Device-Query-lessThan(field: string, value: long | double | string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: number | number | string): Query
```

Creates a **Query** object to match the specified field whose value is less than or equal to the specified value.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-lessThanOrEqualTo(field: string, value: long | double | string): Query--><!--Device-Query-lessThanOrEqualTo(field: string, value: long | double | string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## like

```TypeScript
like(field: string, value: string): Query
```

Creates a **Query** object to match the specified field whose value is similar to the specified string.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-like(field: string, value: string): Query--><!--Device-Query-like(field: string, value: string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.like('field', 'value');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## limit

```TypeScript
limit(total: number, offset: number): Query
```

Creates a **Query** object to specify the number of records of the query result and where to start. This API must  be called after the invocation of the **orderByAsc()**, **orderByDesc()**, and the query APIs of the **Query**object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-limit(total: int, offset: int): Query--><!--Device-Query-limit(total: int, offset: int): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let total = 10;
let offset = 1;
try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.notEqualTo('field', 'value');
    query.limit(total, offset);
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notEqualTo

```TypeScript
notEqualTo(field: string, value: number | number | string | boolean): Query
```

Creates a **Query** object to match the specified field whose value is not equal to the specified value.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-notEqualTo(field: string, value: long | double | string | boolean): Query--><!--Device-Query-notEqualTo(field: string, value: long | double | string | boolean): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## notInNumber

```TypeScript
notInNumber(field: string, valueList: number[] | number[]): Query
```

Creates a **Query** object to match the specified field whose value is not within the specified list of numbers.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-notInNumber(field: string, valueList: long[] | double[]): Query--><!--Device-Query-notInNumber(field: string, valueList: long[] | double[]): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## notInString

```TypeScript
notInString(field: string, valueList: string[]): Query
```

Creates a **Query** object to match the specified field whose value is not within the specified list of strings.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-notInString(field: string, valueList: string[]): Query--><!--Device-Query-notInString(field: string, valueList: string[]): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notInString('field', ['test1', 'test2']);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## or

```TypeScript
or(): Query
```

Creates a **Query** object with the OR condition.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-or(): Query--><!--Device-Query-or(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo('field', 'value1');
      query.or();
      query.notEqualTo('field', 'value2');
      console.info('query is ' + query.getSqlLike());
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## orderByAsc

```TypeScript
orderByAsc(field: string): Query
```

Creates a **Query** object to sort the query results in ascending order.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-orderByAsc(field: string): Query--><!--Device-Query-orderByAsc(field: string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo('field', 'value');
      query.orderByAsc('field');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## orderByDesc

```TypeScript
orderByDesc(field: string): Query
```

Creates a **Query** object to sort the query results in descending order.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-orderByDesc(field: string): Query--><!--Device-Query-orderByDesc(field: string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo('field', 'value');
      query.orderByDesc('field');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## prefixKey

```TypeScript
prefixKey(prefix: string): Query
```

Creates a **Query** object with a specified key prefix.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-prefixKey(prefix: string): Query--><!--Device-Query-prefixKey(prefix: string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.prefixKey('$.name');
      query.prefixKey('0');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## reset

```TypeScript
reset(): Query
```

Resets the **Query** object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-reset(): Query--><!--Device-Query-reset(): Query-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.equalTo('key', 'value');
    console.info('query is ' + query.getSqlLike());
    query.reset();
    console.info('query is ' + query.getSqlLike());
  }
  query = null;
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## setSuggestIndex

```TypeScript
setSuggestIndex(index: string): Query
```

Creates a **Query** object with an index preferentially used for query.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-setSuggestIndex(index: string): Query--><!--Device-Query-setSuggestIndex(index: string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.setSuggestIndex('$.name');
      query.setSuggestIndex('0');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## unlike

```TypeScript
unlike(field: string, value: string): Query
```

Creates a **Query** object to match the specified field whose value is not similar to the specified string.

> **NOTE：**
> 
> This API should be used together with [Schema](arkts-arkdata-distributedkvstore-schema-c.md#Schema).
> 
> For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
> store using the **getKVStore()** method in
> [Persisting KV Store Data](../../../database/data-persistence-by-kv-store.md#how-to-develop).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-Query-unlike(field: string, value: string): Query--><!--Device-Query-unlike(field: string, value: string): Query-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.unlike('field', 'value');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```
