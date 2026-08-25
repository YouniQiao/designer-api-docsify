# setNetworkAccessPolicy（系统接口）

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## setNetworkAccessPolicy

```TypeScript
function setNetworkAccessPolicy(uid: number, policy: NetworkAccessPolicy, isReconfirmed?: boolean): Promise<void>
```

设置指定 uid 应用能否能访问网络的策略，使用 Promise 异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_NET_STRATEGY

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| [policy](arkts-net-policy.md) | [NetworkAccessPolicy](arkts-network-policy-networkaccesspolicy-i-sys.md) | 是 |
| isReconfirmed | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
