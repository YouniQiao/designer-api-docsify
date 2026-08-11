# Preferences

Provides APIs for obtaining and modifying the stored data.Before calling any API of **Preferences**, you must obtain a **Preferences** instance by using   
[preferences.getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences).

**Since:** 9

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

Clears this **Preferences** instance. This API uses an asynchronous callback to return the result. You can use   
[flush](arkts-arkdata-preferences-preferences-i.md#flush) to persist the **Preferences** instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-clear(callback: AsyncCallback<void>): void--><!--Device-Preferences-clear(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Clears this **Preferences** instance. This API uses a promise to return the result. You can use   
[flush](arkts-arkdata-preferences-preferences-i.md#flush) to persist the **Preferences** instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-clear(): Promise<void>--><!--Device-Preferences-clear(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Clears this **Preferences** instance. This API returns the result synchronously. You can use   
[flush](arkts-arkdata-preferences-preferences-i.md#flush) to persist the **Preferences** instance.

**Since:** 10

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

Deletes a KV pair from this **Preferences** instance. This API uses an asynchronous callback to return the result. You can use [flush](arkts-arkdata-preferences-preferences-i.md#flush) to persist the   
**Preferences** instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-delete(key: string, callback: AsyncCallback<void>): void--><!--Device-Preferences-delete(key: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Deletes a KV pair from this **Preferences** instance. This API uses a promise to return the result. You can use   
[flush](arkts-arkdata-preferences-preferences-i.md#flush) to persist the **Preferences** instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-delete(key: string): Promise<void>--><!--Device-Preferences-delete(key: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Deletes a KV pair from this **Preferences** instance. This API returns the result synchronously. You can use   
[flush](arkts-arkdata-preferences-preferences-i.md#flush) to persist the **Preferences** instance.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-deleteSync(key: string): void--><!--Device-Preferences-deleteSync(key: string): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

## Examples

```TypeScript
dataPreferences.deleteSync('startup');
```

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

Flushes the data in this **Preferences** instance to the persistent file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-flush(callback: AsyncCallback<void>): void--><!--Device-Preferences-flush(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Flushes the data in this **Preferences** instance to the persistent file. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-flush(): Promise<void>--><!--Device-Preferences-flush(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Flushes the data in the cached **Preferences** instance to the persistent file.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Preferences-flushSync(): void--><!--Device-Preferences-flushSync(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Error codes:**

| Error Code ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

## Examples

```TypeScript
dataPreferences.flushSync();
```

## get

```TypeScript
get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void
```

Obtains the value of a key from this **Preferences** instance. This API uses an asynchronous callback to return the result. If the value is null or is not of the default value type, **defValue** is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void--><!--Device-Preferences-get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| defValue | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ValueType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Obtains the value of a key from this **Preferences** instance. This API uses a promise to return the result. If the value is null or is not of the default value type, **defValue** is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-get(key: string, defValue: ValueType): Promise<ValueType>--><!--Device-Preferences-get(key: string, defValue: ValueType): Promise<ValueType>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| defValue | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ValueType&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Obtains all KV pairs from a **Preferences** instance. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getAll(callback: AsyncCallback<Object>): void--><!--Device-Preferences-getAll(callback: AsyncCallback<Object>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Obtains all KV pairs from this **Preferences** instance. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getAll(): Promise<Object>--><!--Device-Preferences-getAll(): Promise<Object>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Object&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Obtains all KV pairs from this **Preferences** instance. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getAllSync(): Object--><!--Device-Preferences-getAllSync(): Object-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Object |

**Error codes:**

| Error Code ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Obtains the value of a key from this **Preferences** instance. This API returns the result synchronously. If the value is null or is not of the default value type, **defValue** is returned.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getSync(key: string, defValue: ValueType): ValueType--><!--Device-Preferences-getSync(key: string, defValue: ValueType): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| defValue | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

## Examples

```TypeScript
let value: preferences.ValueType = dataPreferences.getSync('startup', 'default');
```

## has

```TypeScript
has(key: string, callback: AsyncCallback<boolean>): void
```

Checks whether this **Preferences** instance contains the KV pair of the given key. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-has(key: string, callback: AsyncCallback<boolean>): void--><!--Device-Preferences-has(key: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Checks whether this **Preferences** instance contains the KV pair of the given key. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-has(key: string): Promise<boolean>--><!--Device-Preferences-has(key: string): Promise<boolean>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Checks whether this **Preferences** instance contains the KV pair of the given key. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-hasSync(key: string): boolean--><!--Device-Preferences-hasSync(key: string): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Unsubscribes from data changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-off(type: 'change', callback?: Callback<string>): void--><!--Device-Preferences-off(type: 'change', callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Unsubscribes from inter-process data changes.This API is provided for applications that have applied for [dataGroupId](arkts-arkdata-preferences-options-i.md). Avoid using this API for the applications that have not applied for **dataGroupId** because calling it in multiple process may damage the persistent files and cause data loss.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-off(type: 'multiProcessChange', callback?: Callback<string>): void--><!--Device-Preferences-off(type: 'multiProcessChange', callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'multiProcessChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Unsubscribes from changes of specific data.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Preferences-off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void--><!--Device-Preferences-off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataChange' | Yes |
| keys | Array&lt;string&gt; | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, ValueType&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

## on('change')

```TypeScript
on(type: 'change', callback: Callback<string>): void
```

Subscribes to data changes. The registered callback will be invoked to return the new value if the data change is  
[flushed](arkts-arkdata-preferences-preferences-i.md#flush).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-on(type: 'change', callback: Callback<string>): void--><!--Device-Preferences-on(type: 'change', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Subscribes to data changes between processes. When multiple processes hold the same preference file, calling   
[flush](arkts-arkdata-preferences-preferences-i.md#flush) in any process (including the current process) will trigger the callback in this API.This API is provided for applications that have applied for [dataGroupId](arkts-arkdata-preferences-options-i.md). Avoid using this API for the applications that have not applied for **dataGroupId** because calling it in multiple process may damage the persistent files and cause data loss.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-on(type: 'multiProcessChange', callback: Callback<string>): void--><!--Device-Preferences-on(type: 'multiProcessChange', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'multiProcessChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |
| [15500019](../errorcode-preferences.md#15500019-failed-to-obtain-the-subscription-service) |

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

Subscribes to changes of specific data. The registered callback will be invoked only after the values of the specified keys are changed and [flushed](arkts-arkdata-preferences-preferences-i.md#flush).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Preferences-on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void--><!--Device-Preferences-on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataChange' | Yes |
| keys | Array&lt;string&gt; | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, ValueType&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

## put

```TypeScript
put(key: string, value: ValueType, callback: AsyncCallback<void>): void
```

Writes data to this **Preferences** instance. This API uses an asynchronous callback to return the result. You can use [flush](arkts-arkdata-preferences-preferences-i.md#flush) to persist the   
**Preferences** instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-put(key: string, value: ValueType, callback: AsyncCallback<void>): void--><!--Device-Preferences-put(key: string, value: ValueType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Writes data to this **Preferences** instance. This API uses a promise to return the result. You can use   
[flush](arkts-arkdata-preferences-preferences-i.md#flush) to persist the **Preferences** instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-put(key: string, value: ValueType): Promise<void>--><!--Device-Preferences-put(key: string, value: ValueType): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

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

Writes data to this **Preferences** instance. This API returns the result synchronously. You can use   
[flush](arkts-arkdata-preferences-preferences-i.md#flush) to persist the **Preferences** instance.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-putSync(key: string, value: ValueType): void--><!--Device-Preferences-putSync(key: string, value: ValueType): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |

## Examples

```TypeScript
dataPreferences.putSync('startup', 'auto');
```
