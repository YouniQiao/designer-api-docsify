# Storage

Provides APIs for obtaining and modifying storage data.Before calling the following APIs, use [data_storage.getStorage](arkts-arkdata-storage-getstoragesync-f.md) or [data_storage.getStorageSync](arkts-arkdata-storage-getstoragesync-f.md) to obtain the **Storage** instance.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** preferences

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## Modules to Import

```TypeScript
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

Clears this **Storage** object. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** clear

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

```TypeScript
storage.clear(function (err) {
    if (err) {
        console.info("Failed to clear the storage with err: " + err);
        return;
    }
    console.info("Succeeded in clearing the storage.");
})
```

```TypeScript
let promiseclear = storage.clear();
promiseclear.then(() => {
    console.info("Succeeded in clearing the storage.");
}).catch((err) => {
    console.info("Failed to clear the storage with err: " + err);
})
```

## clear

```TypeScript
clear(): Promise<void>
```

Clears this **Storage** object. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** clear

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

See [clear](#clear)

## clearSync

```TypeScript
clearSync(): void
```

Clears this **Storage** object.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** clear

**Examples**

```TypeScript
storage.clearSync();
```

## delete

```TypeScript
delete(key: string, callback: AsyncCallback<void>): void
```

Deletes data with the specified key from this storage object. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** delete

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

```TypeScript
storage.delete('startup', function (err) {
    if (err) {
        console.info("Failed to delete startup key failed err: " + err);
        return;
    }
    console.info("Succeeded in deleting startup key.");
})
```

```TypeScript
let promisedel = storage.delete('startup')
promisedel.then(() => {
    console.info("Succeeded in deleting startup key.");
}).catch((err) => {
    console.info("Failed to delete startup key failed err: " + err);
})
```

## delete

```TypeScript
delete(key: string): Promise<void>
```

Deletes data with the specified key from this storage object. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** delete

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

See [delete](#delete)

## deleteSync

```TypeScript
deleteSync(key: string): void
```

Deletes data with the specified key from this storage object.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** delete

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Examples**

```TypeScript
storage.deleteSync('startup');
```

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

Saves the modification of this object to the **Storage** instance and synchronizes the modification to the file. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** flush

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

```TypeScript
storage.flush(function (err) {
    if (err) {
        console.info("Failed to flush to file with err: " + err);
        return;
    }
    console.info("Succeeded in flushing to file.");
})
```

```TypeScript
let promiseflush = storage.flush();
promiseflush.then(() => {
    console.info("Succeeded in flushing to file.");
}).catch((err) => {
    console.info("Failed to flush to file with err: " + err);
})
```

## flush

```TypeScript
flush(): Promise<void>
```

Saves the modification of this object to the **Storage** instance and synchronizes the modification to the file. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** flush

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

See [flush](#flush)

## flushSync

```TypeScript
flushSync(): void
```

Saves the modification of this object to the **Storage** instance and synchronizes the modification to the file.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** flush

**Examples**

```TypeScript
storage.flushSync();
```

## get

```TypeScript
get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void
```

Obtains the value corresponding to a key. If the value is null or not of the default value type, **defValue** is returned. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** get

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| defValue | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ValueType&gt; | Yes |

**Examples**

```TypeScript
storage.get('startup', 'default', function(err, value) {
    if (err) {
        console.info("Failed to get the value of startup with err: " + err);
        return;
      }
    console.info("The value of startup is " + value);
})
```

```TypeScript
let promiseget = storage.get('startup', 'default');
promiseget.then((value) => {
    console.info("The value of startup is " + value)
}).catch((err) => {
    console.info("Failed to get the value of startup with err: " + err);
})
```

## get

```TypeScript
get(key: string, defValue: ValueType): Promise<ValueType>
```

Obtains the value corresponding to a key. If the value is null or not of the default value type, **defValue** is returned. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** get

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| defValue | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ValueType & gt; |

**Examples**

See [get](#get)

## getSync

```TypeScript
getSync(key: string, defValue: ValueType): ValueType
```

Obtains the value corresponding to a key. If the value is null or not of the default value type, **defValue** is returned.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** get

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| defValue | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**Examples**

```TypeScript
let value = storage.getSync('startup', 'default');
console.info("The value of startup is " + value);
```

## has

```TypeScript
has(key: string, callback: AsyncCallback<boolean>): boolean
```

Checks whether the storage object contains data with a given key. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** has

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
storage.has('startup', function (err, isExist) {
    if (err) {
        console.info("Failed to check the key of startup with err: " + err);
        return;
    }
    if (isExist) {
        console.info("The key of startup is contained.");
    }
})
```

```TypeScript
let promisehas = storage.has('startup')
promisehas.then((isExist) => {
    if (isExist) {
        console.info("The key of startup is contained.");
    }
}).catch((err) => {
    console.info("Failed to check the key of startup with err: " + err);
})
```

## has

```TypeScript
has(key: string): Promise<boolean>
```

Checks whether the storage object contains data with a given key. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** has

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Examples**

See [has](#has)

## hasSync

```TypeScript
hasSync(key: string): boolean
```

Checks whether the storage object contains data with a given key.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** has

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
let isExist = storage.hasSync('startup');
if (isExist) {
    console.info("The key of startup is contained.");
}
```

## off('change')

```TypeScript
off(type: 'change', callback: Callback<StorageObserver>): void
```

Unsubscribes from data changes.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** off

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[StorageObserver](arkts-arkdata-storage-storageobserver-i.md)&gt; | Yes |

**Examples**

```TypeScript
let observer = function (key) {
    console.info("The key of " + key + " changed.");
}
storage.off('change', observer);
```

## on('change')

```TypeScript
on(type: 'change', callback: Callback<StorageObserver>): void
```

Subscribes to data changes. The **StorageObserver** needs to be implemented. When the value of the key subscribed to is changed, a callback will be invoked after **flush()** or **flushSync()** is executed.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** on

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[StorageObserver](arkts-arkdata-storage-storageobserver-i.md)&gt; | Yes |

**Examples**

```TypeScript
let observer = function (key) {
    console.info("The key of " + key + " changed.");
}
storage.on('change', observer);
storage.putSync('startup', 'auto');
storage.flushSync();  // observer will be called.
```

## put

```TypeScript
put(key: string, value: ValueType, callback: AsyncCallback<void>): void
```

Obtains the **Storage** instance corresponding to the specified file, writes data to the **Storage** instance using a **Storage** API, and saves the modification using **flush()** or **flushSync()**. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** put

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

```TypeScript
storage.put('startup', 'auto', function (err) {
    if (err) {
        console.info("Failed to put the value of startup with err: " + err);
        return;
    }
    console.info("Succeeded in putting the value of startup.");
})
```

```TypeScript
let promiseput = storage.put('startup', 'auto');
promiseput.then(() => {
    console.info("Succeeded in putting the value of startup.");
}).catch((err) => {
    console.info("Failed to put the value of startup with err: " + err);
})
```

## put

```TypeScript
put(key: string, value: ValueType): Promise<void>
```

Obtains the **Storage** instance corresponding to the specified file, writes data to the **Storage** instance using a **Storage** API, and saves the modification using **flush()** or **flushSync()**. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** put

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

See [put](#put)

## putSync

```TypeScript
putSync(key: string, value: ValueType): void
```

Obtains the **Storage** instance corresponding to the specified file, writes data to the **Storage** instance using a **Storage** API, and saves the modification using **flush()** or **flushSync()**.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** put

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Examples**

```TypeScript
storage.putSync('startup', 'auto');
```
