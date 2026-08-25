# removeStorageFromCacheSync

## 导入模块

```TypeScript
```

## removeStorageFromCacheSync

```TypeScript
function removeStorageFromCacheSync(path: string): void
```

从内存中移除指定文件对应的Storage单实例。移除Storage单实例时，应用不允许再使用该实例进行数据操作，否则会出现数据一致性问题。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** removePreferencesFromCache

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**示例**

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
