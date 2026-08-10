# NetworkInfo

Parameters for obtaining detailed information on specified network traffic usage.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-statistics-export interface NetworkInfo--><!--Device-statistics-export interface NetworkInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## endTime

```TypeScript
endTime: int
```

End time for querying traffic.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-NetworkInfo-endTime: int--><!--Device-NetworkInfo-endTime: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## simId

```TypeScript
simId?: int
```

SIM card id for querying traffic.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-NetworkInfo-simId?: int--><!--Device-NetworkInfo-simId?: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## startTime

```TypeScript
startTime: int
```

Start time for querying traffic.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-NetworkInfo-startTime: int--><!--Device-NetworkInfo-startTime: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## type

```TypeScript
type: NetBearType
```

Network type for querying traffic.

**类型：** [NetBearType](arkts-network-connection-netbeartype-e.md)

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-NetworkInfo-type: NetBearType--><!--Device-NetworkInfo-type: NetBearType-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

