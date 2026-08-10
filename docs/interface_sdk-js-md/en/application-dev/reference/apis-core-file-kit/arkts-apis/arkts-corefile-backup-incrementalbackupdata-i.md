# IncrementalBackupData (System API)

一次增量备份对象，包含最后一次增量备份时间和增量清单。

**Inheritance/Implementation:** IncrementalBackupData extends [IncrementalBackupTime](arkts-corefile-backup-incrementalbackuptime-i-sys.md), [FileManifestData](arkts-corefile-backup-filemanifestdata-i-sys.md), [BackupParams](arkts-corefile-backup-backupparams-i-sys.md), [BackupPriority](arkts-corefile-backup-backuppriority-i-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-backup-interface IncrementalBackupData extends IncrementalBackupTime, FileManifestData, BackupParams, BackupPriority--><!--Device-backup-interface IncrementalBackupData extends IncrementalBackupTime, FileManifestData, BackupParams, BackupPriority-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

