# FileConflictOptions

Enumerates options for file copy conflicts.

**Since:** 23

<!--Device-pasteboard-enum FileConflictOptions--><!--Device-pasteboard-enum FileConflictOptions-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## OVERWRITE

```TypeScript
OVERWRITE = 0
```

Overwrites the file with the same name in the destination path.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FileConflictOptions-OVERWRITE = 0--><!--Device-FileConflictOptions-OVERWRITE = 0-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## SKIP

```TypeScript
SKIP = 1
```

Skips the file with the same name in the destination path. If **SKIP** is set, the copied data of the skipped file is not pasted to the application.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FileConflictOptions-SKIP = 1--><!--Device-FileConflictOptions-SKIP = 1-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

