# WatchEventListener

```TypeScript
export type WatchEventListener = (event: WatchEvent) => void
```

事件监听类，当监听的文件或目录发生变动事件时触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type WatchEventListener = (event: WatchEvent) => void--><!--Device-unnamed-export type WatchEventListener = (event: WatchEvent) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [WatchEvent](arkts-corefile-file-fs-watchevent-i.md) | Yes | 回调的事件类。 |

