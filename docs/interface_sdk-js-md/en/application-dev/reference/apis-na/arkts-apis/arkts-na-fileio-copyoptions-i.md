# CopyOptions

Defines the callback for listening for the copy progress.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-interface CopyOptions--><!--Device-fileIo-interface CopyOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## copySignal

```TypeScript
copySignal?: TaskSignal
```

Signal used to cancel a copy task.

**Type:** [TaskSignal](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-tasksignal-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CopyOptions-copySignal?: TaskSignal--><!--Device-CopyOptions-copySignal?: TaskSignal-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## progressListener

```TypeScript
progressListener?: ProgressListener
```

Listener used to observe the copy progress.

**Type:** [ProgressListener](../../apis-core-file-kit/arkts-apis/arkts-corefile-progresslistener-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CopyOptions-progressListener?: ProgressListener--><!--Device-CopyOptions-progressListener?: ProgressListener-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

