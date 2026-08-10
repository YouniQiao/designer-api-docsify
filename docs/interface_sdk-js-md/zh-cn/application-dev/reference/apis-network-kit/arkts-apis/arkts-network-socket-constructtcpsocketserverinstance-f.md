# constructTCPSocketServerInstance

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## constructTCPSocketServerInstance

```TypeScript
function constructTCPSocketServerInstance(): TCPSocketServer
```

Creates a TCPSocketServer object.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-socket-function constructTCPSocketServerInstance(): TCPSocketServer--><!--Device-socket-function constructTCPSocketServerInstance(): TCPSocketServer-End-->

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TCPSocketServer](arkts-network-socket-tcpsocketserver-i.md) | the TCPSocketServer of the constructTCPSocketServerInstance. |

## 示例

```TypeScript
import { socket } from '@kit.NetworkKit';
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
```

