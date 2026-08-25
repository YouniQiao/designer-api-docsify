# WatchEventListener

```TypeScript
export type WatchEventListener = (event: WatchEvent) => void
```

事件监听类，当监听的文件或目录发生变动事件时触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [WatchEvent](arkts-corefile-file-fs-watchevent-i.md) | 是 |
