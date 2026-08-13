# OnAVDownloadTaskStateHandle

```TypeScript
type OnAVDownloadTaskStateHandle = (taskId: string, state: AVDownloadTaskState) => void
```

Describes the callback invoked for the AVDownloader state change event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-media-type OnAVDownloadTaskStateHandle = (taskId: string, state: AVDownloadTaskState) => void--><!--Device-media-type OnAVDownloadTaskStateHandle = (taskId: string, state: AVDownloadTaskState) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| taskId | string | Yes | ID of the task whose status changes. |
| state | [AVDownloadTaskState](arkts-media-media-avdownloadtaskstate-t.md) | Yes |  |

