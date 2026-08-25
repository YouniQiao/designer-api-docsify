# getAppNet

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getAppNet

```TypeScript
function getAppNet(callback: AsyncCallback<NetHandle>): void
```

获取App绑定的网络句柄。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NetHandle&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |


## getAppNet

```TypeScript
function getAppNet(): Promise<NetHandle>
```

获取App绑定的网络信息。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;NetHandle & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
