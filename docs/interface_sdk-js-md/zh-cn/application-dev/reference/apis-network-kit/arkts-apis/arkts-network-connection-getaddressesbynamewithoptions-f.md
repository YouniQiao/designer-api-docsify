# getAddressesByNameWithOptions

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getAddressesByNameWithOptions

```TypeScript
function getAddressesByNameWithOptions(host: string, option?: QueryOptions): Promise<Array<NetAddress>>
```

使用当前默认网络基于指定IP类型进行DNS解析。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | string | 是 |
| option | [QueryOptions](arkts-network-connection-queryoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;NetAddress & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
