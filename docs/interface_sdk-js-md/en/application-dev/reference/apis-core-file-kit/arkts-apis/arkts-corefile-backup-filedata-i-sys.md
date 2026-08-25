# FileData (System API)

Corresponding to a file's data. Filedata is useful when doing IPC with the backup service.@interface FileData

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from '@kit.CoreFileKit';
```

## fd

```TypeScript
fd: int
```

Indicates a native file descriptor typically retrieved from the backup service to hold the file's content.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.
