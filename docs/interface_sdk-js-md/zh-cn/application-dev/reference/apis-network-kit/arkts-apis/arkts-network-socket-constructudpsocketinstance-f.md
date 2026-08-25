# constructUDPSocketInstance

## 导入模块

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## constructUDPSocketInstance

```TypeScript
function constructUDPSocketInstance(): UDPSocket
```

创建一个UDPSocket对象。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| [UDPSocket](arkts-network-socket-udpsocket-i.md) |

**示例**

```TypeScript
import { socket } from '@kit.NetworkKit';
let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
```
