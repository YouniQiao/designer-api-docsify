# constructLocalSocketServerInstance

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## constructLocalSocketServerInstance

```TypeScript
function constructLocalSocketServerInstance(): LocalSocketServer
```

Creates a LocalSocketServer object.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-socket-function constructLocalSocketServerInstance(): LocalSocketServer--><!--Device-socket-function constructLocalSocketServerInstance(): LocalSocketServer-End-->

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LocalSocketServer](arkts-network-socket-localsocketserver-i.md) | the LocalSocketServer of the constructLocalSocketServerInstance. |

## 示例

```TypeScript
import { socket } from '@kit.NetworkKit';
let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
```

