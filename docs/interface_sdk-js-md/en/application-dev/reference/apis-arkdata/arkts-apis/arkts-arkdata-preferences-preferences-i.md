# Preferences

Provides APIs for obtaining and modifying the stored data. Before calling any API of **Preferences**, you must obtain a **Preferences** instance by using [preferences.getPreferences](arkts-arkdata-preferences-getpreferences-f.md) .

**Since:** 23

<!--Device-preferences-interface Preferences--><!--Device-preferences-interface Preferences-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## Modules to Import

```TypeScript
import { preferences } from '@kit.ArkData';
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

Clears this **Preferences** instance. This API uses an asynchronous callback to return the result. You can use [flush](#flush) to persist the **Preferences** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-clear(callback: AsyncCallback<void>): void--><!--Device-Preferences-clear(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Mandatory parameters are left unspecified. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

Clears this **Preferences** instance. This API uses a promise to return the result. You can use [flush](#flush) to persist the **Preferences** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-clear(): Promise<void>--><!--Device-Preferences-clear(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

Clears this **Preferences** instance. This API returns the result synchronously. You can use [flush](#flush) to persist the **Preferences** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-clearSync(): void--><!--Device-Preferences-clearSync(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Examples**

```TypeScript
dataPreferences.clearSync();
```

## delete

```TypeScript
delete(key: string, callback: AsyncCallback<void>): void
```

Deletes a KV pair from this **Preferences** instance. This API uses an asynchronous callback to return the result. You can use [flush](#flush) to persist the **Preferences** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-delete(key: string, callback: AsyncCallback<void>): void--><!--Device-Preferences-delete(key: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be deleted. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

Deletes a KV pair from this **Preferences** instance. This API uses a promise to return the result. You can use [flush](#flush) to persist the **Preferences** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-delete(key: string): Promise<void>--><!--Device-Preferences-delete(key: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be deleted. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

Deletes a KV pair from this **Preferences** instance. This API returns the result synchronously. You can use [flush](#flush) to persist the **Preferences** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-deleteSync(key: string): void--><!--Device-Preferences-deleteSync(key: string): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be deleted. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

```TypeScript
dataPreferences.deleteSync('startup');
```

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

Flushes the data in this **Preferences** instance to the persistent file. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-flush(callback: AsyncCallback<void>): void--><!--Device-Preferences-flush(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Mandatory parameters are left unspecified. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-flush(): Promise<void>--><!--Device-Preferences-flush(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Preferences-flushSync(): void--><!--Device-Preferences-flushSync(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |

**Examples**

```TypeScript
dataPreferences.flushSync();
```

## get

```TypeScript
get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void
```

Obtains the value of a key from this **Preferences** instance. This API uses an asynchronous callback to return the result. If the value is null or is not of the default value type, **defValue** is returned.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void--><!--Device-Preferences-get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be obtained. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |
| defValue | ValueType | Yes | Default value to be returned. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;ValueType&gt; | Yes | Callback used to return the result. If the operation is successful , **err** is **undefined** and **data** is the value obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-get(key: string, defValue: ValueType): Promise<ValueType>--><!--Device-Preferences-get(key: string, defValue: ValueType): Promise<ValueType>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be obtained. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |
| defValue | ValueType | Yes | Default value to be returned. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ValueType&gt; | Promise used to return the value obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getAll(callback: AsyncCallback<Object>): void--><!--Device-Preferences-getAll(callback: AsyncCallback<Object>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Object&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **value** provides all KV pairs obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Mandatory parameters are left unspecified. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getAll(): Promise<Object>--><!--Device-Preferences-getAll(): Promise<Object>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Object&gt; | Promise used to return the KV pairs obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getAllSync(): Object--><!--Device-Preferences-getAllSync(): Object-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Return value:**

| Type | Description |
| --- | --- |
| Object | Returns all KV pairs obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-getSync(key: string, defValue: ValueType): ValueType--><!--Device-Preferences-getSync(key: string, defValue: ValueType): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be obtained. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |
| defValue | ValueType | Yes | Default value to be returned. |

**Return value:**

| Type | Description |
| --- | --- |
| ValueType | Returns the value obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

```TypeScript
let value: preferences.ValueType = dataPreferences.getSync('startup', 'default');
```

## has

```TypeScript
has(key: string, callback: AsyncCallback<boolean>): void
```

Checks whether this **Preferences** instance contains the KV pair of the given key. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-has(key: string, callback: AsyncCallback<boolean>): void--><!--Device-Preferences-has(key: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be checked. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the **Preferences** instance contains the KV pair, **true** will be returned. Otherwise, **false** will be returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-has(key: string): Promise<boolean>--><!--Device-Preferences-has(key: string): Promise<boolean>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be checked. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. If the **Preferences** instance contains the KV pair, **true** will be returned. Otherwise, **false** will be returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-hasSync(key: string): boolean--><!--Device-Preferences-hasSync(key: string): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be checked. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If the **Preferences** instance contains the KV pair, **true** will be returned. Otherwise, **false** will be returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

```TypeScript
let isExist: boolean = dataPreferences.hasSync('startup');
if (isExist) {
  console.info("The key 'startup' is contained.");
} else {
  console.info("The key 'startup' does not contain.");
}
```

## offChange

```TypeScript
offChange(callback?: Callback<string>): void
```

Unregisters an existing observer.

**Since:** 23

<!--Device-Preferences-offChange(callback?: Callback<string>): void--><!--Device-Preferences-offChange(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | No | Indicates the callback function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |

## offDataChange

```TypeScript
offDataChange(keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void
```

Unregisters an observer for changes to the {@ link Preferences} object.

**Since:** 23

<!--Device-Preferences-offDataChange(keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void--><!--Device-Preferences-offDataChange(keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | Yes | Indicates the data whose changes are not observed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Record&lt;string, ValueType&gt;&gt; | No | Indicates the callback to unregister. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |

## offMultiProcessChange

```TypeScript
offMultiProcessChange(callback?: Callback<string>): void
```

Unregisters an existing observer.

**Since:** 23

<!--Device-Preferences-offMultiProcessChange(callback?: Callback<string>): void--><!--Device-Preferences-offMultiProcessChange(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | No | Indicates the callback function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for data changes.<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataChange' | Yes | Event type. The value is **'dataChange'**, which indicates data changes. |
| keys | Array&lt;string&gt; | Yes | Array of keys to be unsubscribed from. If this parameter is left empty, all keys are unsubscribed from. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Record&lt;string, ValueType&gt;&gt; | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the changes of the specified data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |

**Examples**

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

## off('multiProcessChange')

```TypeScript
off(type: 'multiProcessChange', callback?: Callback<string>): void
```

Unsubscribes from inter-process data changes. This API is provided for applications that have applied for [dataGroupId](arkts-arkdata-preferences-options-i.md). Avoid using this API for the applications that have not applied for **dataGroupId** because calling it in multiple process may damage the persistent files and cause data loss.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-off(type: 'multiProcessChange', callback?: Callback<string>): void--><!--Device-Preferences-off(type: 'multiProcessChange', callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'multiProcessChange' | Yes | Event type. The value is **'multiProcessChange'**, which indicates inter- process data changes. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for data changes.<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

## onChange

```TypeScript
onChange(callback: Callback<string>): void
```

Registers an observer to listen for the change of a [Preferences](#preferences) object.

**Since:** 23

<!--Device-Preferences-onChange(callback: Callback<string>): void--><!--Device-Preferences-onChange(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | Yes | Indicates the callback function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |

## onDataChange

```TypeScript
onDataChange(keys: Array<string>, callback: Callback<Record<string, ValueType>>): void
```

Registers an observer to listen for changes to the {@ link Preferences} object.

**Since:** 23

<!--Device-Preferences-onDataChange(keys: Array<string>, callback: Callback<Record<string, ValueType>>): void--><!--Device-Preferences-onDataChange(keys: Array<string>, callback: Callback<Record<string, ValueType>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | Yes | Indicates one or more keys to listen for. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Record&lt;string, ValueType&gt;&gt; | Yes | Indicates the callback used to return the data change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |

## onMultiProcessChange

```TypeScript
onMultiProcessChange(callback: Callback<string>): void
```

Registers an observer to listen for the change of a [Preferences](#preferences) object.

**Since:** 23

<!--Device-Preferences-onMultiProcessChange(callback: Callback<string>): void--><!--Device-Preferences-onMultiProcessChange(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | Yes | Indicates the callback function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |
| [15500019](../errorcode-preferences.md#15500019-failed-to-obtain-the-subscription-service) | Failed to obtain the subscription service. |

## on('change')

```TypeScript
on(type: 'change', callback: Callback<string>): void
```

Subscribes to data changes. The registered callback will be invoked to return the new value if the data change is [flushed](#flush).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-on(type: 'change', callback: Callback<string>): void--><!--Device-Preferences-on(type: 'change', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | Yes | Callback used to return the data change.<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

## on('dataChange')

```TypeScript
on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void
```

Subscribes to changes of specific data. The registered callback will be invoked only after the values of the specified keys are changed and [flushed](#flush).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Preferences-on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void--><!--Device-Preferences-on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataChange' | Yes | Event type. The value is **'dataChange'**, which indicates data changes. |
| keys | Array&lt;string&gt; | Yes | Array of the keys to be observed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Record&lt;string, ValueType&gt;&gt; | Yes | Callback used to return the changed data, in an array of KV pairs. The keys identify the data changed, and the values are the new values. The values support the following data types: number, string, boolean, Array&lt;number&gt;, Array&lt;string&gt;, Array&lt; boolean&gt;, Uint8Array, and object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |

**Examples**

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

## on('multiProcessChange')

```TypeScript
on(type: 'multiProcessChange', callback: Callback<string>): void
```

Subscribes to data changes between processes. When multiple processes hold the same preference file, calling [flush](#flush) in any process (including the current process) will trigger the callback in this API. This API is provided for applications that have applied for [dataGroupId](arkts-arkdata-preferences-options-i.md). Avoid using this API for the applications that have not applied for **dataGroupId** because calling it in multiple process may damage the persistent files and cause data loss.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-on(type: 'multiProcessChange', callback: Callback<string>): void--><!--Device-Preferences-on(type: 'multiProcessChange', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'multiProcessChange' | Yes | Event type. The value is **'multiProcessChange'**, which indicates inter- process data changes. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | Yes | Callback used to return the data change.<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |
| [15500019](../errorcode-preferences.md#15500019-failed-to-obtain-the-subscription-service) | Failed to obtain the subscription service. |

**Examples**

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

## put

```TypeScript
put(key: string, value: ValueType, callback: AsyncCallback<void>): void
```

Writes data to this **Preferences** instance. This API uses an asynchronous callback to return the result. You can use [flush](#flush) to persist the **Preferences** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-put(key: string, value: ValueType, callback: AsyncCallback<void>): void--><!--Device-Preferences-put(key: string, value: ValueType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be modified. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |
| value | ValueType | Yes | Value to write. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

Writes data to this **Preferences** instance. This API uses a promise to return the result. You can use [flush](#flush) to persist the **Preferences** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-put(key: string, value: ValueType): Promise<void>--><!--Device-Preferences-put(key: string, value: ValueType): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be modified. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |
| value | ValueType | Yes | Value to write. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

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

Writes data to this **Preferences** instance. This API returns the result synchronously. You can use [flush](#flush) to persist the **Preferences** instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Preferences-putSync(key: string, value: ValueType): void--><!--Device-Preferences-putSync(key: string, value: ValueType): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be modified. The value cannot be empty. For details about its maximum length, see [MAX_KEY_LENGTH](arkts-data-preferences.md#constants). |
| value | ValueType | Yes | Value to write. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

**Examples**

```TypeScript
dataPreferences.putSync('startup', 'auto');
```

