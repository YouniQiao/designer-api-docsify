# NetIpMacInfo

The correspondence information between IP and MAC address.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

<!--Device-connection-export interface NetIpMacInfo--><!--Device-connection-export interface NetIpMacInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## iface

```TypeScript
iface: string
```

Interface name of the network.

**类型：** string

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

<!--Device-NetIpMacInfo-iface: string--><!--Device-NetIpMacInfo-iface: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## ipAddress

```TypeScript
ipAddress: NetAddress
```

Link address of the network.

**类型：** [NetAddress](arkts-network-connection-netaddress-i.md)

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

<!--Device-NetIpMacInfo-ipAddress: NetAddress--><!--Device-NetIpMacInfo-ipAddress: NetAddress-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## macAddress

```TypeScript
macAddress: string
```

Mac address of the network.

**类型：** string

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

<!--Device-NetIpMacInfo-macAddress: string--><!--Device-NetIpMacInfo-macAddress: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

