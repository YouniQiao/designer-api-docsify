# ProgressListener

```TypeScript
type ProgressListener = (progress: ProgressInfo) => void
```

Defines a listener for progress data changes. If the default progress indicator is not used, you can set this API to obtain the paste progress.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-pasteboard-type ProgressListener = (progress: ProgressInfo) => void--><!--Device-pasteboard-type ProgressListener = (progress: ProgressInfo) => void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progress | ProgressInfo | Yes | Defines the progress information. This information is reported only when [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md#progressindicator) is set to **NONE**. |

