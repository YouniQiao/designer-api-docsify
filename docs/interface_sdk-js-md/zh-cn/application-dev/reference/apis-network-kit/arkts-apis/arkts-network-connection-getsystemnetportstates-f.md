# getSystemNetPortStates

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getSystemNetPortStates

```TypeScript
function getSystemNetPortStates(): Promise<NetPortStatesInfo>
```

获取系统当前监听的所有TCP、UDP端口信息，以及监听端口进程的PID、UID，支持IPv4和IPv6。

> **说明：**&gt;
> 该接口获取系统当前监听的TCP、UDP端口信息，详细字段包括：&gt;
>   TCP端口字段：本地地址、本地端口、远端地址、远端端口、TCP连接状态、进程PID、进程UID&gt;
>   UDP端口字段：本地地址、本地端口、进程PID 、进程UID

**起始版本：** 24

**需要权限：** ohos.permission.GET_IP_MAC_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[NetPortStatesInfo](arkts-network-connection-netportstatesinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
