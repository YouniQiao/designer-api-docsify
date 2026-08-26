# removeStorageFromCacheSync

## Modules to Import

```TypeScript
```

## removeStorageFromCacheSync

```TypeScript
function removeStorageFromCacheSync(path: string): void
```

Removes the singleton **Storage** instance of a file from the cache. The removed instance cannot be used for data operations. Otherwise, data inconsistency will occur.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** removePreferencesFromCache

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Indicates the path of storage file. |

**Examples**

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';

let path;
let context = featureAbility.getContext();
context.getFilesDir().then((filePath) => {
    path = filePath;
    console.info("======================>getFilesDirPromise====================>");

    data_storage.removeStorageFromCacheSync(path + '/mystore');
});
```
