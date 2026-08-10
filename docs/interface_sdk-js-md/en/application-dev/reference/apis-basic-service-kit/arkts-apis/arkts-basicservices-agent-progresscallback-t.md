# ProgressCallback

```TypeScript
export type ProgressCallback = (progress: Progress) => void
```

The callback function for the download progress event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-agent-export type ProgressCallback = (progress: Progress) => void--><!--Device-agent-export type ProgressCallback = (progress: Progress) => void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progress | [Progress](arkts-basicservices-agent-progress-i.md) | Yes | callback function with a `Progress` argument. |

