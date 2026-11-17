# MechInfo

```TypeScript
export interface MechInfo
```

机械设备信息@typedef MechInfo

**起始版本：** 20

<!--Device-mechanicManager-export interface MechInfo--><!--Device-mechanicManager-export interface MechInfo-End-->

**系统能力：** SystemCapability.Mechanic.Core

## 导入模块

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## mechDeviceType

```TypeScript
mechDeviceType: MechDeviceType
```

机械设备类型

**类型：** [MechDeviceType](arkts-mechanic-mechanicmanager-mechdevicetype-e.md)

**起始版本：** 20

<!--Device-MechInfo-mechDeviceType: MechDeviceType--><!--Device-MechInfo-mechDeviceType: MechDeviceType-End-->

**系统能力：** SystemCapability.Mechanic.Core

## mechId

```TypeScript
mechId: number
```

机械体设备ID，取值为大于等于0的整数。

**类型：** number

**起始版本：** 20

<!--Device-MechInfo-mechId: int--><!--Device-MechInfo-mechId: int-End-->

**系统能力：** SystemCapability.Mechanic.Core

## mechName

```TypeScript
mechName: string
```

机械体设备名称，长度不超过64字符。

**类型：** string

**起始版本：** 20

<!--Device-MechInfo-mechName: string--><!--Device-MechInfo-mechName: string-End-->

**系统能力：** SystemCapability.Mechanic.Core
