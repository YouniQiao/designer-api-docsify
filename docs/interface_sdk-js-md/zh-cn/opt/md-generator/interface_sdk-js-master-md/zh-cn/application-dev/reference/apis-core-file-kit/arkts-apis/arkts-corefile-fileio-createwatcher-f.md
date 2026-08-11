# createWatcher

## createWatcher

```TypeScript
declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher
```

监听文件或者目录的变化，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [@ohos.file.fs:createWatcher](arkts-corefile-fileio-createwatcher-f.md#createwatcher)

<!--Device-unnamed-declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher--><!--Device-unnamed-declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filename | string | 是 |
| events | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Watcher](arkts-corefile-file-fs-watcher-i.md) |
