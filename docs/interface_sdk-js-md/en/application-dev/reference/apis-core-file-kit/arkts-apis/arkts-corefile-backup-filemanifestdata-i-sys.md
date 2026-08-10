# FileManifestData (System API)

增量数据中的清单文件信息，用于描述应用增量备份、恢复时对应文件的基础信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-backup-interface FileManifestData--><!--Device-backup-interface FileManifestData-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## manifestFd

```TypeScript
manifestFd: int
```

清单文件的文件描述符，通过备份服务获取。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-FileManifestData-manifestFd: int--><!--Device-FileManifestData-manifestFd: int-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

