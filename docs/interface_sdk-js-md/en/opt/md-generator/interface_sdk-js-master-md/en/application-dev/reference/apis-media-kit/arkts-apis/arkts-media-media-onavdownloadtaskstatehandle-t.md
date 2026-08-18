# OnAVDownloadTaskStateHandle

```TypeScript
type OnAVDownloadTaskStateHandle = (taskId: string, state: AVDownloadTaskState) => void
```

Describes the callback invoked for the AVDownloader state change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-media-type OnAVDownloadTaskStateHandle = (taskId: string, state: AVDownloadTaskState) => void--><!--Device-media-type OnAVDownloadTaskStateHandle = (taskId: string, state: AVDownloadTaskState) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| taskId | string | Yes |
| state | [AVDownloadTaskState](arkts-media-media-avdownloadtaskstate-t.md) | Yes |
