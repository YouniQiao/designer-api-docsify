# WatchEventListener

```TypeScript
export type WatchEventListener = (event: WatchEvent) => void
```

Defines a watch event listener. When the monitored file or directory changes, a callback is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export type WatchEventListener = (event: WatchEvent) => void--><!--Device-unnamed-export type WatchEventListener = (event: WatchEvent) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [WatchEvent](arkts-filefs-watchevent-i.md) | Yes | Event for the callback to invoke. |

