# setNetExtAttribute

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## setNetExtAttribute

```TypeScript
function setNetExtAttribute(netHandle: NetHandle, netExtAttribute: string): Promise<void>
```

为netHandle对应的网络设置扩展属性，标识网络的安全级别。使用Promise异步回调。

> **说明：**&gt;
> 该接口所需的权限目前仅支持PC设备。

**起始版本：** 20

**需要权限：** ohos.permission.SET_NET_EXT_ATTRIBUTE

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| netHandle | [NetHandle](arkts-network-connection-nethandle-i.md) | 是 |
| netExtAttribute | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
