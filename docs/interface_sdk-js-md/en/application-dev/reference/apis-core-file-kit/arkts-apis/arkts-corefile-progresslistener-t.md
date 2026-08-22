# ProgressListener

```TypeScript
type ProgressListener = (progress: Progress) => void
```

Listener used to observe the copy progress.

**Since:** 11

<!--Device-unnamed-type ProgressListener = (progress: Progress) => void--><!--Device-unnamed-type ProgressListener = (progress: Progress) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progress | [Progress](arkts-corefile-file-fs-progress-i.md) | Yes | indicates the progress data of copyFile |

**Examples**

```TypeScript
import { TaskSignal } from '@kit.CoreFileKit';
let copySignal: fs.TaskSignal = new TaskSignal();
let progressListener: fs.ProgressListener = (progress: fs.Progress) => {
  console.info(`processedSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
};
let copyOption: fs.CopyOptions = {
  "progressListener" : progressListener,
  "copySignal" : copySignal,
}
```

