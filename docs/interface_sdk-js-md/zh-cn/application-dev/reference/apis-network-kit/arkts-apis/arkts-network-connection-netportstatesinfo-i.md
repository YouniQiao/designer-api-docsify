# NetPortStatesInfo

Defines port states of system network.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-connection-export interface NetPortStatesInfo--><!--Device-connection-export interface NetPortStatesInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## tcpPortStatesInfo

```TypeScript
tcpPortStatesInfo?: Array<TcpNetPortStatesInfo>
```

Port information of the TCP network.

**类型：** Array&lt;TcpNetPortStatesInfo&gt;

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NetPortStatesInfo-tcpPortStatesInfo?: Array<TcpNetPortStatesInfo>--><!--Device-NetPortStatesInfo-tcpPortStatesInfo?: Array<TcpNetPortStatesInfo>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## udpPortStatesInfo

```TypeScript
udpPortStatesInfo?: Array<UdpNetPortStatesInfo>
```

Port information of the UDP network.

**类型：** Array&lt;UdpNetPortStatesInfo&gt;

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NetPortStatesInfo-udpPortStatesInfo?: Array<UdpNetPortStatesInfo>--><!--Device-NetPortStatesInfo-udpPortStatesInfo?: Array<UdpNetPortStatesInfo>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

