# getStorageSync

## Modules to Import

```TypeScript
```

## getStorageSync

```TypeScript
function getStorageSync(path: string): Storage
```

Reads the specified file and loads its data to the **Storage** instance for data operations.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** getPreferences

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path of the target file. |

**Return value:**

| Type | Description |
| --- | --- |
| Storage | Storage** instance used for data storage operations. |

**Examples**

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';

let path;
let context = featureAbility.getContext();
context.getFilesDir().then((filePath) => {
  path = filePath;
  console.info("======================>getFilesDirPromise====================>");

  let storage = data_storage.getStorageSync(path + '/mystore');
  storage.putSync('startup', 'auto');
  storage.flushSync();
});
```
