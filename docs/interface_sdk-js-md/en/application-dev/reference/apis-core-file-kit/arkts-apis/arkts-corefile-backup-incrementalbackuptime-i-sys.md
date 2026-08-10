# IncrementalBackupTime (System API)

记录最后一次增量备份时间，用于描述备份增量的时间点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-backup-interface IncrementalBackupTime--><!--Device-backup-interface IncrementalBackupTime-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## bundleName

```TypeScript
bundleName: string
```

应用名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-IncrementalBackupTime-bundleName: string--><!--Device-IncrementalBackupTime-bundleName: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## lastIncrementalTime

```TypeScript
lastIncrementalTime: long
```

最后一次增量备份时间。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-IncrementalBackupTime-lastIncrementalTime: long--><!--Device-IncrementalBackupTime-lastIncrementalTime: long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

