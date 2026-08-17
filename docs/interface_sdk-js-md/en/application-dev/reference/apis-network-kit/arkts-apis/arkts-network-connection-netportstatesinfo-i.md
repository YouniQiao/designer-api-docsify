# NetPortStatesInfo

Defines port states of system network.

**Since:** 26.0.0

<!--Device-connection-export interface NetPortStatesInfo--><!--Device-connection-export interface NetPortStatesInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## tcpPortStatesInfo

```TypeScript
tcpPortStatesInfo?: Array<TcpNetPortStatesInfo>
```

Port information of the TCP network.

**Type:** Array&lt;[TcpNetPortStatesInfo](arkts-network-connection-tcpnetportstatesinfo-i.md)&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-NetPortStatesInfo-tcpPortStatesInfo?: Array<TcpNetPortStatesInfo>--><!--Device-NetPortStatesInfo-tcpPortStatesInfo?: Array<TcpNetPortStatesInfo>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## udpPortStatesInfo

```TypeScript
udpPortStatesInfo?: Array<UdpNetPortStatesInfo>
```

Port information of the UDP network.

**Type:** Array&lt;[UdpNetPortStatesInfo](arkts-network-connection-udpnetportstatesinfo-i.md)&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-NetPortStatesInfo-udpPortStatesInfo?: Array<UdpNetPortStatesInfo>--><!--Device-NetPortStatesInfo-udpPortStatesInfo?: Array<UdpNetPortStatesInfo>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

