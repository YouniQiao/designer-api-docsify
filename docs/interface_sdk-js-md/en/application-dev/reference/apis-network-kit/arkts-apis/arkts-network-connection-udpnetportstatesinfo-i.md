# UdpNetPortStatesInfo

Describes the UDP port state information.

**Since:** 24

<!--Device-connection-export interface UdpNetPortStatesInfo--><!--Device-connection-export interface UdpNetPortStatesInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## udpLocalIp

```TypeScript
udpLocalIp: string
```

Local IP address of the UDP network.

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UdpNetPortStatesInfo-udpLocalIp: string--><!--Device-UdpNetPortStatesInfo-udpLocalIp: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## udpLocalPort

```TypeScript
udpLocalPort: int
```

Local port of the UDP network. The value range is [0, 65535].

**Type:** int

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UdpNetPortStatesInfo-udpLocalPort: int--><!--Device-UdpNetPortStatesInfo-udpLocalPort: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## udpPid

```TypeScript
udpPid: int
```

PID of the process that listens for the UDP port.

**Type:** int

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UdpNetPortStatesInfo-udpPid: int--><!--Device-UdpNetPortStatesInfo-udpPid: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## udpUid

```TypeScript
udpUid: int
```

UID of the user who listens for the UDP port.

**Type:** int

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UdpNetPortStatesInfo-udpUid: int--><!--Device-UdpNetPortStatesInfo-udpUid: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

