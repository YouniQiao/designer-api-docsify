# getDefaultHttpProxy

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getDefaultHttpProxy

```TypeScript
function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void
```

获取网络的默认代理配置信息。使用callback异步回调。

> **说明：**&gt;
> - 如果设置了全局代理，则返回全局代理配置信息。&gt;
> - 如果进程使用[setAppNet](arkts-network-connection-setappnet-f.md)绑定到指定[NetHandle](arkts-network-connection-nethandle-i.md)对应的网络，则返回
> [NetHandle](arkts-network-connection-nethandle-i.md)对应网络的代理配置信息。在其它情况下，将返回默认网络的代理配置信息。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpProxy&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |


## getDefaultHttpProxy

```TypeScript
function getDefaultHttpProxy(): Promise<HttpProxy>
```

获取网络默认的代理配置信息。使用Promise异步回调。

> **说明：**&gt;
> - 如果设置了全局代理，则返回全局代理配置信息。&gt;
> - 如果进程使用[setAppNet](arkts-network-connection-setappnet-f.md)绑定到指定[NetHandle](arkts-network-connection-nethandle-i.md)对应的网络，则返回
> [NetHandle](arkts-network-connection-nethandle-i.md)对应网络的代理配置信息。在其它情况下，将返回默认网络的代理配置信息。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;HttpProxy & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
