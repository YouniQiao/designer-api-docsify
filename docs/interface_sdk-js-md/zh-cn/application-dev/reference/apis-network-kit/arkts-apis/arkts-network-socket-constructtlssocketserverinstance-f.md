# constructTLSSocketServerInstance

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## constructTLSSocketServerInstance

```TypeScript
function constructTLSSocketServerInstance(): TLSSocketServer
```

Creates a TLSSocketServer object.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-socket-function constructTLSSocketServerInstance(): TLSSocketServer--><!--Device-socket-function constructTLSSocketServerInstance(): TLSSocketServer-End-->

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TLSSocketServer](arkts-network-socket-tlssocketserver-i.md) | the TLSSocketServer of the constructTLSSocketServerInstance. |

## 示例

```TypeScript
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
```

