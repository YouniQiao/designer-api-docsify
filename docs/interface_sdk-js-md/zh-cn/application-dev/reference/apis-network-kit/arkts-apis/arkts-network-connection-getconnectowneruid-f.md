# getConnectOwnerUid

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getConnectOwnerUid

```TypeScript
function getConnectOwnerUid(protocol: ProtocolType, local: NetAddress, remote: NetAddress): Promise<number>
```

用于查询发起指定网络连接的应用UID。使用Promise异步回调。

> **说明：**&gt;
> - 该接口仅限在VPN应用中调用。&gt;
> - 调用接口时请设置local和remote参数的端口号。若未设置端口号或将端口号设置为0，接口会基于其他参数筛选出符合条件的UID的集合，并从中返回一个匹配的UID。&gt;
> - protocol参数为PROTO_TYPE_UDP时，若通过local，remote参数未筛选出符合条件的UID，则仅基于local参数筛选并返回匹配的UID。

**起始版本：** 23

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| protocol | [ProtocolType](arkts-network-connection-protocoltype-e.md) | 是 |
| local | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 |
| [remote](../../apis-driver-development-kit/arkts-apis/arkts-driverdevelopment-devicemanager-remotedevicedriver-i.md) | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100301](../errorcode-net-connection.md#2100301-调用方身份验证不通过非vpn应用) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
