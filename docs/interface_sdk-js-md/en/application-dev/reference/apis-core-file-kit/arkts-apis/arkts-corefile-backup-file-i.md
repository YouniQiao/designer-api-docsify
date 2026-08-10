# File (System API)

文件对象，包含文件元数据、文件数据和清单文件信息。用于客户端与备份服务进行IPC。

**Inheritance/Implementation:** File extends [FileMeta](arkts-corefile-backup-filemeta-i-sys.md), [FileData](arkts-corefile-backup-filedata-i-sys.md), [FileManifestData](arkts-corefile-backup-filemanifestdata-i-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-backup-interface File extends FileMeta, FileData, FileManifestData--><!--Device-backup-interface File extends FileMeta, FileData, FileManifestData-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

