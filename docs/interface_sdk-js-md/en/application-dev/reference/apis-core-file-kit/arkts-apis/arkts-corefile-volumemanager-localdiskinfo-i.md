# LocalDiskInfo

```TypeScript
export interface LocalDiskInfo
```

Local disk hardware information.

**Since:** 26.1.0

<!--Device-volumeManager-export interface LocalDiskInfo--><!--Device-volumeManager-export interface LocalDiskInfo-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

## Modules to Import

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## description

```TypeScript
description: string
```

Disk description. The value is the same as that of **model**.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalDiskInfo-description: string--><!--Device-LocalDiskInfo-description: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

## mediaType

```TypeScript
mediaType: number
```

Disk media type. **1**: SSD (Solid State Drive). **2**: HDD (Hard Disk Drive). **255**: Unknown. The value should be an integer.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalDiskInfo-mediaType: int--><!--Device-LocalDiskInfo-mediaType: int-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

## model

```TypeScript
model: string
```

Disk model, which is defined by the vendor.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalDiskInfo-model: string--><!--Device-LocalDiskInfo-model: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

## size

```TypeScript
size: number
```

Total size of the disk. Unit: Byte.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalDiskInfo-size: long--><!--Device-LocalDiskInfo-size: long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

## state

```TypeScript
state: string
```

Disk running state. The value can be **live**, **connecting**, **resetting**, or **dead**.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalDiskInfo-state: string--><!--Device-LocalDiskInfo-state: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

## sysPath

```TypeScript
sysPath: string
```

Physical path of the disk device node, such as **\/sys/block/nvme0n1**.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalDiskInfo-sysPath: string--><!--Device-LocalDiskInfo-sysPath: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume
