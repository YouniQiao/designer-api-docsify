# getStorage

## 导入模块

```TypeScript
```

## getStorage

```TypeScript
function getStorage(path: string, callback: AsyncCallback<Storage>): void
```

读取指定文件，将数据加载到Storage实例，用于数据操作，使用callback方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** getPreferences

<!--Device-storage-function getStorage(path: string, callback: AsyncCallback<Storage>): void--><!--Device-storage-function getStorage(path: string, callback: AsyncCallback<Storage>): void-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Storage&gt; | 是 |


## getStorage

```TypeScript
function getStorage(path: string): Promise<Storage>
```

读取指定文件，将数据加载到Storage实例，用于数据操作，使用Promise方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** getPreferences

<!--Device-storage-function getStorage(path: string): Promise<Storage>--><!--Device-storage-function getStorage(path: string): Promise<Storage>-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Storage & gt; |
