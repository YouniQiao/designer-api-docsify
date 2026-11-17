# LocalDiskInfo

```TypeScript
export interface LocalDiskInfo
```

本地磁盘硬件信息。

**起始版本：** 26.1.0

<!--Device-volumeManager-export interface LocalDiskInfo--><!--Device-volumeManager-export interface LocalDiskInfo-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

## 导入模块

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## description

```TypeScript
description: string
```

磁盘描述信息，与model字段取值相同。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocalDiskInfo-description: string--><!--Device-LocalDiskInfo-description: string-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

## mediaType

```TypeScript
mediaType: number
```

磁盘介质类型。**1**：SSD（固态硬盘）。**2**：HDD（机械硬盘）。**255**：未知。该值应为整数。取值限定为整数。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocalDiskInfo-mediaType: int--><!--Device-LocalDiskInfo-mediaType: int-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

## model

```TypeScript
model: string
```

磁盘型号，由厂商定义。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocalDiskInfo-model: string--><!--Device-LocalDiskInfo-model: string-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

## size

```TypeScript
size: number
```

磁盘总空间大小。单位：Byte。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocalDiskInfo-size: long--><!--Device-LocalDiskInfo-size: long-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

## state

```TypeScript
state: string
```

磁盘运行状态，取值包括"live"、"connecting"、"resetting"、"dead"。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocalDiskInfo-state: string--><!--Device-LocalDiskInfo-state: string-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

## sysPath

```TypeScript
sysPath: string
```

磁盘设备节点的物理路径，如/sys/block/nvme0n1。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocalDiskInfo-sysPath: string--><!--Device-LocalDiskInfo-sysPath: string-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume
