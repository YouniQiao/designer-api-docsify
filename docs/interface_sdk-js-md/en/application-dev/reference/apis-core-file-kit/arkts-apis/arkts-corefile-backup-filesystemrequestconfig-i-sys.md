# FileSystemRequestConfig (System API)

Parameters required to perform garbage collection (GC).

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-backup-interface FileSystemRequestConfig--><!--Device-backup-interface FileSystemRequestConfig-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from '@kit.CoreFileKit';
```

## triggerType

```TypeScript
triggerType: int
```

Specifies the trigger type for garbage collection (0-default Device GC).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileSystemRequestConfig-triggerType: int--><!--Device-FileSystemRequestConfig-triggerType: int-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## waitTime

```TypeScript
waitTime: int
```

Sets the maximum wait time (in seconds) for GC operation.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileSystemRequestConfig-waitTime: int--><!--Device-FileSystemRequestConfig-waitTime: int-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## writeSize

```TypeScript
writeSize: int
```

Defines the target size (in MBytes) for garbage collection.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileSystemRequestConfig-writeSize: int--><!--Device-FileSystemRequestConfig-writeSize: int-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

