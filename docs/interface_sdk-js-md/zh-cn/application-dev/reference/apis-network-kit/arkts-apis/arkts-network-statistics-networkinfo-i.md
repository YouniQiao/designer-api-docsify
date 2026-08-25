# NetworkInfo

网络信息。

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## endTime

```TypeScript
endTime: int
```

结束时间戳（单位：秒）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetManager.Core

## simId

```TypeScript
simId?: int
```

SIM卡ID。默认值为uint32_t类型最大值。  
**注意：** 当type为蜂窝网络时，需指定本字段。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetManager.Core

## startTime

```TypeScript
startTime: int
```

开始时间戳（单位：秒）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetManager.Core

## type

```TypeScript
type: NetBearType
```

网络类型。  
**注意：** 当type为蜂窝网络时，需指定simId字段。

**类型：** NetBearType

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetManager.Core
