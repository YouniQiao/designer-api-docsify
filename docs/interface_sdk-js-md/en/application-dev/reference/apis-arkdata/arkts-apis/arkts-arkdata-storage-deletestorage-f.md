# deleteStorage

## Modules to Import

```TypeScript
```

## deleteStorage

```TypeScript
function deleteStorage(path: string, callback: AsyncCallback<void>): void
```

Deletes the singleton **Storage** instance of a file from the memory, and deletes the specified file, its backup file, and damaged files. After the specified files are deleted, the **Storage** instance cannot be used for data operations. Otherwise, data inconsistency will occur. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** deletePreferences

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path of the target file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';

let path;
let context = featureAbility.getContext();
context.getFilesDir().then((filePath) => {
  path = filePath;
  console.info("======================>getFilesDirPromise====================>");

  data_storage.deleteStorage(path + '/mystore', function (err) {
    if (err) {
      console.info("Failed to delete the storage with err: " + err);
      return;
    }
    console.info("Succeeded in deleting the storage.");
  })
});
```


## deleteStorage

```TypeScript
function deleteStorage(path: string): Promise<void>
```

Deletes the singleton **Storage** instance of a file from the memory, and deletes the specified file, its backup file, and damaged files. After the specified files are deleted, the **Storage** instance cannot be used for data operations. Otherwise, data inconsistency will occur. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** deletePreferences

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path of the target file. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;void & gt; | Promise used to return the result. |

**Examples**

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';

let path;
let context = featureAbility.getContext();
context.getFilesDir().then((filePath) => {
  path = filePath;
  console.info("======================>getFilesDirPromise====================>");

  let promisedelSt = data_storage.deleteStorage(path + '/mystore');
  promisedelSt.then(() => {
    console.info("Succeeded in deleting the storage.");
  }).catch((err) => {
    console.info("Failed to delete the storage with err: " + err);
  })
});
```
