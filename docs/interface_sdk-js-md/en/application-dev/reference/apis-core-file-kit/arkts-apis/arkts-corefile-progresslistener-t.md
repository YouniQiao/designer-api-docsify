# ProgressListener

```TypeScript
type ProgressListener = (progress: Progress) => void
```

Listener used to observe the copy progress.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| progress | [Progress](arkts-corefile-file-fs-progress-i.md) | Yes |

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
