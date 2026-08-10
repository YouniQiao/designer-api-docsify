# NetBlockStatusInfo

Get network status information.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-connection-export interface NetBlockStatusInfo--><!--Device-connection-export interface NetBlockStatusInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## blocked

```TypeScript
blocked: boolean
```

Check whether the current state is blocked.

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-NetBlockStatusInfo-blocked: boolean--><!--Device-NetBlockStatusInfo-blocked: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## netHandle

```TypeScript
netHandle: NetHandle
```

Defines the handle of the data network.

**类型：** [NetHandle](arkts-network-connection-nethandle-i.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-NetBlockStatusInfo-netHandle: NetHandle--><!--Device-NetBlockStatusInfo-netHandle: NetHandle-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

