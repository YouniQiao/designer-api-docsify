# ProgressListener

```TypeScript
type ProgressListener = (progress: Progress) => void
```

Listener used to observe the copy progress.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-type ProgressListener = (progress: Progress) => void--><!--Device-fileIo-type ProgressListener = (progress: Progress) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progress | [Progress](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-progress-i.md) | Yes | indicates the progress data of copyFile |

