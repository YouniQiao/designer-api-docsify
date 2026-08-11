# FileMeta (System API)

Corresponding to a file's metadata. FileMeta is useful when doing IPC with the backup service.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-backup-interface FileMeta--><!--Device-backup-interface FileMeta-End-->

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

Indicates the name of a bundle.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-FileMeta-bundleName: string--><!--Device-FileMeta-bundleName: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## uri

```TypeScript
uri: string
```

Indicates a uri to a file.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-FileMeta-uri: string--><!--Device-FileMeta-uri: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## uris

```TypeScript
uris?: Array<string>
```

Indicates uris to files.

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMeta-uris?: Array<string>--><!--Device-FileMeta-uris?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

