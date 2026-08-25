# getConnectOwnerUid

## 导入模块

```TypeScript
import { connection } from '@kit.NetworkKit';
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

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为23。

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

**示例**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let protocol = connection.ProtocolType.PROTO_TYPE_TCP;
let local: connection.NetAddress = { address: '192.168.1.100', family: 1, port: 6666 };
let remote: connection.NetAddress = { address: '192.168.1.200', family: 1, port: 8888 };
connection.getConnectOwnerUid(protocol, local, remote).then((uid) => {
  console.info(`Succeeded to get uid: ${uid}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get ConnectOwnerUid. errorCode: ${error.code} message:${error.message}`);
});
```
