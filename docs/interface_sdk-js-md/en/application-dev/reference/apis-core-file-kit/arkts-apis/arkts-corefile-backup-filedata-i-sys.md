# FileData (System API)

文件数据，包含一个已经打开的文件描述符，在与备份服务进行IPC时使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-backup-interface FileData--><!--Device-backup-interface FileData-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## fd

```TypeScript
fd: int
```

已经打开的文件描述符，通过备份服务获取，可用于读取或写入备份、恢复文件内容。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-FileData-fd: int--><!--Device-FileData-fd: int-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

