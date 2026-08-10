# FileSystemRequestConfig (System API)

配置系统执行碎片清理所需的参数。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-backup-interface FileSystemRequestConfig--><!--Device-backup-interface FileSystemRequestConfig-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## triggerType

```TypeScript
triggerType: int
```

指定碎片清理的触发类型，取值0表示执行存储器件碎片清理。

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

执行碎片清理的最大允许时间，单位为秒，取值范围为0至300。

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

碎片清理的目标大小，单位为MB，取值范围为0至2097152。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileSystemRequestConfig-writeSize: int--><!--Device-FileSystemRequestConfig-writeSize: int-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

