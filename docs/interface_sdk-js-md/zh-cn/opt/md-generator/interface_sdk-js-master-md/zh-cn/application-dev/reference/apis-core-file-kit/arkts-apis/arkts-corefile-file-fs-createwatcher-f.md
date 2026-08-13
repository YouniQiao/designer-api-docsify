# createWatcher

## createWatcher

```TypeScript
declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher
```

创建Watcher对象，监听文件或目录变动。

**起始版本：** 10

**废弃版本：** -1

<!--Device-unnamed-declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher--><!--Device-unnamed-declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| events | number | 是 | 监听变动的事件集，多个事件通过或(\|
| listener | [WatchEventListener](arkts-corefile-file-fs-watcheventlistener-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Watcher](arkts-corefile-file-fs-watcher-i.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900042 |
| 13900011 |
