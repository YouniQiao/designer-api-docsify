# getStorageSync

## getStorageSync

```TypeScript
function getStorageSync(path: string): Storage
```

读取指定文件，将数据加载到Storage实例，用于数据操作。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.preferences.preferences.getPreferences

<!--Device-storage-function getStorageSync(path: string): Storage--><!--Device-storage-function getStorageSync(path: string): Storage-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 应用程序内部数据存储路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Storage](arkts-arkdata-system-storage-storage-c.md) | 获取到要操作的Storage实例，用于进行数据存储操作。 |

