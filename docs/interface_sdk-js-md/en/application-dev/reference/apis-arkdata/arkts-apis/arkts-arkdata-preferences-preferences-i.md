# Preferences

首选项实例，提供获取和修改存储数据的接口。

下列接口都需先使用[preferences.getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences)获取到Preferences实例，再通过此实例调用对应接口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-preferences-interface Preferences--><!--Device-preferences-interface Preferences-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## Modules to Import

```TypeScript
import { preferences } from 'kits/@kit.ArkData';
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

清除缓存的Preferences实例中的所有数据，可通过[flush](arkts-arkdata-preferences-preferences-i.md#flush)将Preferences实例持久化，使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-clear(callback: AsyncCallback<void>): void--><!--Device-Preferences-clear(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当清除成功，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Mandatory parameters are left unspecified. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.clear((err: BusinessError) =>{
  if (err) {
    console.error("Failed to clear. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in clearing.");
})
```

## clear

```TypeScript
clear(): Promise<void>
```

清除缓存的Preferences实例中的所有数据，可通过[flush](arkts-arkdata-preferences-preferences-i.md#flush)将Preferences实例持久化，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-clear(): Promise<void>--><!--Device-Preferences-clear(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.clear();
promise.then(() => {
  console.info("Succeeded in clearing.");
}).catch((err: BusinessError) => {
  console.error("Failed to clear. code =" + err.code + ", message =" + err.message);
})
```

## clearSync

```TypeScript
clearSync(): void
```

清除缓存的Preferences实例中的所有数据，可通过[flush](arkts-arkdata-preferences-preferences-i.md#flush)将Preferences实例持久化，此为同步接口。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-clearSync(): void--><!--Device-Preferences-clearSync(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## Examples

```TypeScript
dataPreferences.clearSync();
```

## delete

```TypeScript
delete(key: string, callback: AsyncCallback<void>): void
```

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](arkts-arkdata-preferences-preferences-i.md#flush)将Preferences实例持久化，使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-delete(key: string, callback: AsyncCallback<void>): void--><!--Device-Preferences-delete(key: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要删除的存储Key名称，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当删除成功，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.delete('startup', (err: BusinessError) => {
  if (err) {
    console.error("Failed to delete the key 'startup'. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in deleting the key 'startup'.");
})
```

## delete

```TypeScript
delete(key: string): Promise<void>
```

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](arkts-arkdata-preferences-preferences-i.md#flush)将Preferences实例持久化，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-delete(key: string): Promise<void>--><!--Device-Preferences-delete(key: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要删除的存储Key名称，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.delete('startup');
promise.then(() => {
  console.info("Succeeded in deleting the key 'startup'.");
}).catch((err: BusinessError) => {
  console.error("Failed to delete the key 'startup'. code =" + err.code +", message =" + err.message);
})
```

## deleteSync

```TypeScript
deleteSync(key: string): void
```

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](arkts-arkdata-preferences-preferences-i.md#flush)将Preferences实例持久化，此为同步接口。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-deleteSync(key: string): void--><!--Device-Preferences-deleteSync(key: string): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要删除的存储Key名称，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
dataPreferences.deleteSync('startup');
```

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

将缓存的Preferences实例中的数据异步存储到用户首选项的持久化文件中，使用callback异步回调。

> **说明：**
> 
> 当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。
> 
> 只在XML存储模式下使用，在GSKV存储模式下无需调用，因为当选择该模式时首选项对数据的操作会实时落盘。Preferences存储模式可见
> [存储模式说明](../../../database/data-persistence-by-preferences.md#存储模式说明)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-flush(callback: AsyncCallback<void>): void--><!--Device-Preferences-flush(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当保存成功，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Mandatory parameters are left unspecified. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in flushing.");
})
```

## flush

```TypeScript
flush(): Promise<void>
```

将缓存的Preferences实例中的数据异步存储到用户首选项的持久化文件中，使用Promise异步回调。

> **说明：**
> 
> 当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。
> 
> 只在XML存储模式下使用，在GSKV存储模式下无需调用，因为当选择该模式时首选项对数据的操作会实时落盘。Preferences存储模式可见
> [存储模式说明](../../../database/data-persistence-by-preferences.md#存储模式说明)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-flush(): Promise<void>--><!--Device-Preferences-flush(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.flush();
promise.then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error("Failed to flush. code =" + err.code + ", message =" + err.message);
})
```

## flushSync

```TypeScript
flushSync(): void
```

将缓存的Preferences实例中的数据存储到用户首选项的持久化文件中。

> **说明：**
> 
> 当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Preferences-flushSync(): void--><!--Device-Preferences-flushSync(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error. |

## Examples

```TypeScript
dataPreferences.flushSync();
```

## get

```TypeScript
get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void
```

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void--><!--Device-Preferences-get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要获取的存储Key名称，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |
| defValue | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 默认返回值。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ValueType&gt; | Yes | 回调函数。当获取成功时，err为undefined，data为键对应的值；否则err为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.get('startup', 'default', (err: BusinessError, val: preferences.ValueType) => {
  if (err) {
    console.error("Failed to get value of 'startup'. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in getting value of 'startup'. val: " + val);
})
```

## get

```TypeScript
get(key: string, defValue: ValueType): Promise<ValueType>
```

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-get(key: string, defValue: ValueType): Promise<ValueType>--><!--Device-Preferences-get(key: string, defValue: ValueType): Promise<ValueType>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要获取的存储Key名称，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |
| defValue | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 默认返回值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ValueType&gt; | Promise对象，返回键对应的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.get('startup', 'default');
promise.then((data: preferences.ValueType) => {
  console.info("Succeeded in getting value of 'startup'. Data: " + data);
}).catch((err: BusinessError) => {
  console.error("Failed to get value of 'startup'. code =" + err.code + ", message =" + err.message);
})
```

## getAll

```TypeScript
getAll(callback: AsyncCallback<Object>): void
```

获取缓存的Preferences实例中的所有键值数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getAll(callback: AsyncCallback<Object>): void--><!--Device-Preferences-getAll(callback: AsyncCallback<Object>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | Yes | 回调函数。当获取成功，err为undefined，value为所有键值数据；否则err为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Mandatory parameters are left unspecified. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// There is no Object.keys in ArkTS, and the for..in... syntax cannot be used.
// If an error is reported, extract this API to a .ts file and expose it. Then import the API to the .ets file when required.
function getObjKeys(obj: Object): string[] {
  let keys = Object.keys(obj);
  return keys;
}

dataPreferences.getAll((err: BusinessError, value: Object) => {
  if (err) {
    console.error("Failed to get all key-values. code =" + err.code + ", message =" + err.message);
    return;
  }
  let allKeys = getObjKeys(value);
  console.info("getAll keys = " + allKeys);
  console.info("getAll object = " + JSON.stringify(value));
})
```

## getAll

```TypeScript
getAll(): Promise<Object>
```

获取缓存的Preferences实例中的所有键值数据，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getAll(): Promise<Object>--><!--Device-Preferences-getAll(): Promise<Object>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Object&gt; | Promise对象，返回所有包含的键值数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// There is no Object.keys in ArkTS, and the for..in... syntax cannot be used.
// If an error is reported, extract this API to a .ts file and expose it. Then import the API to the .ets file when required.
function getObjKeys(obj: Object): string[] {
  let keys = Object.keys(obj);
  return keys;
}

let promise = dataPreferences.getAll();
promise.then((value: Object) => {
  let allKeys = getObjKeys(value);
  console.info('getAll keys = ' + allKeys);
  console.info("getAll object = " + JSON.stringify(value));
}).catch((err: BusinessError) => {
  console.error("Failed to get all key-values. code =" + err.code + ", message =" + err.message);
})
```

## getAllSync

```TypeScript
getAllSync(): Object
```

获取缓存的Preferences实例中的所有键值数据，此为同步接口。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getAllSync(): Object--><!--Device-Preferences-getAllSync(): Object-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| Type | Description |
| --- | --- |
| Object | 返回所有包含的键值数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
// There is no Object.keys in ArkTS, and the for..in... syntax cannot be used.
// If an error is reported, extract this API to a .ts file and expose it. Then import the API to the .ets file when required.
function getObjKeys(obj: Object): string[] {
  let keys = Object.keys(obj);
  return keys;
}

let value = dataPreferences.getAllSync();
let allKeys = getObjKeys(value);
console.info('getAll keys = ' + allKeys);
console.info("getAll object = " + JSON.stringify(value));
```

## getSync

```TypeScript
getSync(key: string, defValue: ValueType): ValueType
```

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，此为同步接口。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getSync(key: string, defValue: ValueType): ValueType--><!--Device-Preferences-getSync(key: string, defValue: ValueType): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要获取的存储Key名称，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |
| defValue | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 默认返回值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 返回键对应的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
let value: preferences.ValueType = dataPreferences.getSync('startup', 'default');
```

## has

```TypeScript
has(key: string, callback: AsyncCallback<boolean>): void
```

检查缓存的Preferences实例中是否包含指定Key的存储键值对，使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-has(key: string, callback: AsyncCallback<boolean>): void--><!--Device-Preferences-has(key: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要检查的存储Key名称，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。返回Preferences实例是否包含给定Key的存储键值对，true表示存在，false表示不存在。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.has('startup', (err: BusinessError, val: boolean) => {
  if (err) {
    console.error("Failed to check the key 'startup'. code =" + err.code + ", message =" + err.message);
    return;
  }
  if (val) {
    console.info("The key 'startup' is contained.");
  } else {
    console.info("The key 'startup' is not contained.");
  }
})
```

## has

```TypeScript
has(key: string): Promise<boolean>
```

检查缓存的Preferences实例中是否包含指定Key的存储键值对，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-has(key: string): Promise<boolean>--><!--Device-Preferences-has(key: string): Promise<boolean>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要检查的存储Key名称，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回Preferences实例是否包含给定Key的存储键值对，true表示存在，false表示不存在。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.has('startup');
promise.then((val: boolean) => {
  if (val) {
    console.info("The key 'startup' is contained.");
  } else {
    console.info("The key 'startup' does not contain.");
  }
}).catch((err: BusinessError) => {
  console.error("Failed to check the key 'startup'. code =" + err.code + ", message =" + err.message);
})
```

## hasSync

```TypeScript
hasSync(key: string): boolean
```

检查缓存的Preferences实例中是否包含指定Key的存储键值对，此为同步接口。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-hasSync(key: string): boolean--><!--Device-Preferences-hasSync(key: string): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要检查的存储Key名称，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回Preferences实例是否包含给定Key的存储键值对，true表示存在，false表示不存在。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
let isExist: boolean = dataPreferences.hasSync('startup');
if (isExist) {
  console.info("The key 'startup' is contained.");
} else {
  console.info("The key 'startup' does not contain.");
}
```

## off('change')

```TypeScript
off(type: 'change', callback?: Callback<string>): void
```

取消订阅数据变更。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-off(type: 'change', callback?: Callback<string>): void--><!--Device-Preferences-off(type: 'change', callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | 事件类型，固定值'change'，表示数据变更。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | 需要取消的回调函数，若不填写，表示取消所有已注册的回调函数；若填写，表示只取消指定的回调函数。<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
}
dataPreferences.on('change', observer);
dataPreferences.putSync('startup', 'auto');
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
dataPreferences.off('change', observer);
```

## off('multiProcessChange')

```TypeScript
off(type: 'multiProcessChange', callback?: Callback<string>): void
```

取消订阅进程间数据变更。

本接口提供给申请了[dataGroupId](arkts-arkdata-preferences-options-i.md)的应用进行使用，未申请的应用不推荐使用（监听不到数据变更），多进程操作可能会损坏持久化文件，导致数据丢失。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-off(type: 'multiProcessChange', callback?: Callback<string>): void--><!--Device-Preferences-off(type: 'multiProcessChange', callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'multiProcessChange' | Yes | 事件类型，固定值'multiProcessChange'，表示多进程间的数据变更。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | 需要取消的回调函数，若不填写，表示取消所有已注册的回调函数；若填写，表示只取消指定的回调函数。<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
}
dataPreferences.on('multiProcessChange', observer);
dataPreferences.putSync('startup', 'auto');
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
dataPreferences.off('multiProcessChange', observer);
```

## off('dataChange')

```TypeScript
off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void
```

取消精确订阅数据变更。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Preferences-off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void--><!--Device-Preferences-off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataChange' | Yes | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array&lt;string&gt; | Yes | 需要取消订阅的Key集合，当Keys为空数组时，表示取消订阅全部Key；当Keys为非空数组时，表示只取消订阅Key集合中的Key。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, ValueType&gt;&gt; | No | 需要取消的回调函数，若不填写，表示取消所有已注册的回调函数；若填写，表示只取消指定的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (data: Record<string, preferences.ValueType>) => {
  for (const keyValue of Object.entries(data)) {
    console.info(`observer : ${keyValue}`);
  }
  console.info("The observer called.");
}
let keys = ['name', 'age'];
dataPreferences.on('dataChange', keys, observer);
dataPreferences.putSync('name', 'xiaohong');
dataPreferences.putSync('weight', 125);
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
dataPreferences.off('dataChange', keys, observer);
```

## offChange

```TypeScript
offChange(callback?: Callback<string>): void
```

Unregisters an existing observer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Preferences-offChange(callback?: Callback<string>): void--><!--Device-Preferences-offChange(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | 需要取消的回调函数，若不填写，表示取消所有已注册的回调函数；若填写，表示只取消指定的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error. |

## offDataChange

```TypeScript
offDataChange(keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void
```

Unregisters an observer for changes to the {@ link Preferences} object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Preferences-offDataChange(keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void--><!--Device-Preferences-offDataChange(keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | Yes | 需要取消订阅的key集合，当keys为空数组时，表示取消订阅全部key；当keys为非空数组时，表示只取消订阅key集合中的key。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, ValueType&gt;&gt; | No | 需要取消的回调函数，若不填写，表示取消所有已注册的回调函数；若填写，表示只取消指定的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error. |

## offMultiProcessChange

```TypeScript
offMultiProcessChange(callback?: Callback<string>): void
```

Unregisters an existing observer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Preferences-offMultiProcessChange(callback?: Callback<string>): void--><!--Device-Preferences-offMultiProcessChange(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | 需要取消的回调函数，若不填写，表示取消所有已注册的回调函数；若填写，表示只取消指定的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error. |

## on('change')

```TypeScript
on(type: 'change', callback: Callback<string>): void
```

订阅数据变更，订阅的Key的值发生变更后，并且在执行[flush](arkts-arkdata-preferences-preferences-i.md#flush)方法后，触发callback回调。

> **不同订阅方法的对比：**
> 
> - on('change')：订阅所有Key变化，适合全局数据变化感知需求。
> 
> - on('dataChange')：精确订阅指定Key的变化，适合关注特定数据场景，可回调返回具体值。
> 
> - on('multiProcessChange')：订阅多进程数据变化，适合多进程共享同一首选项文件的场景。
> 
> **选取建议：** 单进程应用推荐使用on('change')或on('dataChange')；多进程数据同步时使用on('multiProcessChange')；需要精确知道特定Key变化并获取新值时使用on('
> dataChange')。
> > **说明：**
> 
> 当调用[removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache)或
> [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences)后，订阅的数据变更会主动取消订阅，在重新
> [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences)后需要重新订阅数据变更。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-on(type: 'change', callback: Callback<string>): void--><!--Device-Preferences-on(type: 'change', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | 事件类型，固定值'change'，表示数据变更。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | 回调函数，用于接收数据变更通知，回调参数为Key字符串，表示发生变更的键名称。<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
}
dataPreferences.on('change', observer);
dataPreferences.putSync('startup', 'manual');
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
```

## on('multiProcessChange')

```TypeScript
on(type: 'multiProcessChange', callback: Callback<string>): void
```

订阅进程间数据变更，多个进程持有同一个首选项文件时，在任意一个进程（包括本进程）执行  
[flush](arkts-arkdata-preferences-preferences-i.md#flush)方法，持久化文件发生变更后，触发callback回调。

本接口提供给申请了[dataGroupId](arkts-arkdata-preferences-options-i.md)的应用进行使用，未申请的应用不推荐使用（监听不到数据变更），多进程操作可能会损坏持久化文件，导致数据丢失。

> **说明：**
> 
> 同一持久化文件在当前进程对多进程数据变更订阅的最大数量为50次，超过最大限制后订阅会失败。建议在触发callback回调后及时取消订阅。
> 
> 当调用[removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache)或
> [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences)后，订阅的数据变更会主动取消订阅，在重新
> [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences)后需要重新订阅数据变更。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-on(type: 'multiProcessChange', callback: Callback<string>): void--><!--Device-Preferences-on(type: 'multiProcessChange', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'multiProcessChange' | Yes | 事件类型，固定值'multiProcessChange'，表示多进程间的数据变更。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | 多进程间数据变更时触发的回调函数，回调参数为发生变更的Key字符串。<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |
| 15500019 | Failed to obtain the subscription service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
}
dataPreferences.on('multiProcessChange', observer);
dataPreferences.putSync('startup', 'manual');
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
```

## on('dataChange')

```TypeScript
on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void
```

精确订阅数据变更，只有被订阅的Key值发生变更后，在执行[flush](arkts-arkdata-preferences-preferences-i.md#flush)方法后，触发callback回调。

> **说明：**
> 
> 当调用[removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache)或
> [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences)后，订阅的数据变更会主动取消订阅，在重新
> [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences)后需要重新订阅数据变更。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Preferences-on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void--><!--Device-Preferences-on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataChange' | Yes | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array&lt;string&gt; | Yes | 需要订阅的Key集合。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, ValueType&gt;&gt; | Yes | 回调函数。回调支持返回多个键值对，其中键为发生变更的订阅Key，类型为string；值为变更后的数据，类型为 [ValueType](arkts-arkdata-preferences-valuetype-t.md)。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 15500000 | Inner error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (data: Record<string, preferences.ValueType>) => {
  for (const keyValue of Object.entries(data)) {
    console.info(`observer : ${keyValue}`);
  }
  console.info("The observer called.");
}
let keys = ['name', 'age'];
dataPreferences.on('dataChange', keys, observer);
dataPreferences.putSync('name', 'xiaohong');
dataPreferences.putSync('weight', 125);
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
```

## onChange

```TypeScript
onChange(callback: Callback<string>): void
```

Registers an observer to listen for the change of a {@link Preferences} object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Preferences-onChange(callback: Callback<string>): void--><!--Device-Preferences-onChange(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | 回调函数，用于接收数据变更通知，回调参数为Key字符串，表示发生变更的键名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error. |

## onDataChange

```TypeScript
onDataChange(keys: Array<string>, callback: Callback<Record<string, ValueType>>): void
```

Registers an observer to listen for changes to the {@ link Preferences} object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Preferences-onDataChange(keys: Array<string>, callback: Callback<Record<string, ValueType>>): void--><!--Device-Preferences-onDataChange(keys: Array<string>, callback: Callback<Record<string, ValueType>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | Yes | 需要订阅的key集合。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, ValueType&gt;&gt; | Yes | 回调函数。回调支持返回多个键值对，其中键为发生变更的订阅key，类型为string；值为变更后的数据，类型为[ValueType](#valuetype)。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error. |

## onMultiProcessChange

```TypeScript
onMultiProcessChange(callback: Callback<string>): void
```

Registers an observer to listen for the change of a {@link Preferences} object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Preferences-onMultiProcessChange(callback: Callback<string>): void--><!--Device-Preferences-onMultiProcessChange(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | 多进程间数据变更时触发的回调函数，回调参数为发生变更的Key字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15500000 | Inner error. |
| 15500019 | Failed to obtain the subscription service. |

## put

```TypeScript
put(key: string, value: ValueType, callback: AsyncCallback<void>): void
```

将数据写入缓存的Preferences实例中，可通过[flush](arkts-arkdata-preferences-preferences-i.md#flush)将Preferences实例持久化，使用callback异步回调。

> **说明：**
> 
> 当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。
> 
> 当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-put(key: string, value: ValueType, callback: AsyncCallback<void>): void--><!--Device-Preferences-put(key: string, value: ValueType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要修改的存储的Key，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 存储的新值。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当数据写入成功，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.put('startup', 'auto', (err: BusinessError) => {
  if (err) {
    console.error("Failed to put value of 'startup'. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in putting value of 'startup'.");
})
```

## put

```TypeScript
put(key: string, value: ValueType): Promise<void>
```

将数据写入缓存的Preferences实例中，可通过[flush](arkts-arkdata-preferences-preferences-i.md#flush)将Preferences实例持久化，使用Promise异步回调。

> **说明：**
> 
> 当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。
> 
> 当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-put(key: string, value: ValueType): Promise<void>--><!--Device-Preferences-put(key: string, value: ValueType): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要修改的存储的Key，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 存储的新值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.put('startup', 'auto');
promise.then(() => {
  console.info("Succeeded in putting value of 'startup'.");
}).catch((err: BusinessError) => {
  console.error("Failed to put value of 'startup'. code =" + err.code + ", message =" + err.message);
})
```

## putSync

```TypeScript
putSync(key: string, value: ValueType): void
```

将数据写入缓存的Preferences实例中，可通过[flush](arkts-arkdata-preferences-preferences-i.md#flush)将Preferences实例持久化，此为同步接口。

> **说明：**
> 
> 当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。
> 
> 当对应的键已经存在时，putSync()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-putSync(key: string, value: ValueType): void--><!--Device-Preferences-putSync(key: string, value: ValueType): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要修改的存储的Key，不能为空，最大长度限制为 [MAX_KEY_LENGTH](../../../reference/apis-arkdata/js-apis-data-sendablePreferences.md#constants)。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 存储的新值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 15500000 | Inner error.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
dataPreferences.putSync('startup', 'auto');
```

