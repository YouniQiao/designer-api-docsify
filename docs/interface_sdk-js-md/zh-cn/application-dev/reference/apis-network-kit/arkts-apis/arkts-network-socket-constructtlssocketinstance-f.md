# constructTLSSocketInstance

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## constructTLSSocketInstance

```TypeScript
function constructTLSSocketInstance(): TLSSocket
```

创建并返回一个TLSSocket对象。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| [TLSSocket](arkts-network-socket-tlssocket-i.md) |


## constructTLSSocketInstance

```TypeScript
function constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket
```

将TCPSocket升级为TLSSocket，创建并返回一个TLSSocket对象。

> **说明：**&gt;
> 需要确保TCPSocket已连接，并且当前已经没有传输数据，再调用constructTLSSocketInstance升级TLSSocket。当升级成功后，无需对TCPSocket对象调用close方法。

**起始版本：** 12

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tcpSocket | [TCPSocket](arkts-network-socket-tcpsocket-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TLSSocket](arkts-network-socket-tlssocket-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
| 2303601 |
| 2303602 |
