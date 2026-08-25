# FileManifestData (System API)

Manifest file information in incremental data. FileManifestData is useful when doing IPC with the backup service.@interface FileManifestData

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from '@kit.CoreFileKit';
```

## manifestFd

```TypeScript
manifestFd: int
```

A file descriptor for the manifest file that holds the data

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.
