# TcpNetPortStatesInfo

Defines TCP port states of system network.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-connection-export interface TcpNetPortStatesInfo--><!--Device-connection-export interface TcpNetPortStatesInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## tcpLocalIp

```TypeScript
tcpLocalIp: string
```

Local IP of the TCP network.

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TcpNetPortStatesInfo-tcpLocalIp: string--><!--Device-TcpNetPortStatesInfo-tcpLocalIp: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## tcpLocalPort

```TypeScript
tcpLocalPort: int
```

Local port of the TCP network.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TcpNetPortStatesInfo-tcpLocalPort: int--><!--Device-TcpNetPortStatesInfo-tcpLocalPort: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## tcpPid

```TypeScript
tcpPid: int
```

PID of the TCP network.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TcpNetPortStatesInfo-tcpPid: int--><!--Device-TcpNetPortStatesInfo-tcpPid: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## tcpRemoteIp

```TypeScript
tcpRemoteIp: string
```

Remote IP of the TCP network.

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TcpNetPortStatesInfo-tcpRemoteIp: string--><!--Device-TcpNetPortStatesInfo-tcpRemoteIp: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## tcpRemotePort

```TypeScript
tcpRemotePort: int
```

Remote port of the TCP network.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TcpNetPortStatesInfo-tcpRemotePort: int--><!--Device-TcpNetPortStatesInfo-tcpRemotePort: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## tcpState

```TypeScript
tcpState: TcpState
```

Port state of the TCP network.

**类型：** [TcpState](arkts-network-connection-tcpstate-e.md)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TcpNetPortStatesInfo-tcpState: TcpState--><!--Device-TcpNetPortStatesInfo-tcpState: TcpState-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## tcpUid

```TypeScript
tcpUid: int
```

UID of the TCP network.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TcpNetPortStatesInfo-tcpUid: int--><!--Device-TcpNetPortStatesInfo-tcpUid: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

