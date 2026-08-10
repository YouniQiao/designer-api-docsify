# deleteStorageSync

## deleteStorageSync

```TypeScript
function deleteStorageSync(path: string): void
```

从内存中移除指定文件对应的Storage单实例，并删除指定文件及其备份文件、损坏文件。删除指定文件时，应用不允许再使用该实例进行数据操作，否则会出现数据一致性问题。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.preferences.preferences.deletePreferences

<!--Device-storage-function deleteStorageSync(path: string): void--><!--Device-storage-function deleteStorageSync(path: string): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 应用程序内部数据存储路径。 |

