# IncrementalBackupTime (System API)

Save the time information of the incremental backup. IncrementalBackupTime is useful when doing IPC with the backup service.@interface IncrementalBackupTime

**Since:** 23

<!--Device-backup-interface IncrementalBackupTime--><!--Device-backup-interface IncrementalBackupTime-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from '@kit.CoreFileKit';
```

## bundleName

```TypeScript
bundleName: string
```

Indicates the name of a bundle.

**Type:** string

**Since:** 23

<!--Device-IncrementalBackupTime-bundleName: string--><!--Device-IncrementalBackupTime-bundleName: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## lastIncrementalTime

```TypeScript
lastIncrementalTime: long
```

Time of the last incremental backup

**Type:** long

**Since:** 23

<!--Device-IncrementalBackupTime-lastIncrementalTime: long--><!--Device-IncrementalBackupTime-lastIncrementalTime: long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

