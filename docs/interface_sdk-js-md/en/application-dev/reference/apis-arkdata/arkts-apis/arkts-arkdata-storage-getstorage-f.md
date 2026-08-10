# getStorage

## getStorage

```TypeScript
function getStorage(path: string, callback: AsyncCallback<Storage>): void
```

读取指定文件，将数据加载到Storage实例，用于数据操作，使用callback方式返回结果，此方法为异步方法。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.preferences.preferences.getPreferences

<!--Device-storage-function getStorage(path: string, callback: AsyncCallback<Storage>): void--><!--Device-storage-function getStorage(path: string, callback: AsyncCallback<Storage>): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 应用程序内部数据存储路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Storage&gt; | Yes | 回调函数。 |


## getStorage

```TypeScript
function getStorage(path: string): Promise<Storage>
```

读取指定文件，将数据加载到Storage实例，用于数据操作，使用Promise方式返回结果，此方法为异步方法。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.preferences.preferences.getPreferences

<!--Device-storage-function getStorage(path: string): Promise<Storage>--><!--Device-storage-function getStorage(path: string): Promise<Storage>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 应用程序内部数据存储路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Storage&gt; | Promise实例，用于异步获取结果。 |

