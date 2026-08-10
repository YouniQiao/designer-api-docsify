# NetIpMacInfo

The correspondence information between IP and MAC address.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

<!--Device-connection-export interface NetIpMacInfo--><!--Device-connection-export interface NetIpMacInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## iface

```TypeScript
iface: string
```

Interface name of the network.

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

<!--Device-NetIpMacInfo-iface: string--><!--Device-NetIpMacInfo-iface: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## ipAddress

```TypeScript
ipAddress: NetAddress
```

Link address of the network.

**Type:** [NetAddress](arkts-network-connection-netaddress-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

<!--Device-NetIpMacInfo-ipAddress: NetAddress--><!--Device-NetIpMacInfo-ipAddress: NetAddress-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## macAddress

```TypeScript
macAddress: string
```

Mac address of the network.

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

<!--Device-NetIpMacInfo-macAddress: string--><!--Device-NetIpMacInfo-macAddress: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

