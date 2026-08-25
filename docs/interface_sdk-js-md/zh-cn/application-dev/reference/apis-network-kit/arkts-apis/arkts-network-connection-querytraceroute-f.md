# queryTraceRoute

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## queryTraceRoute

```TypeScript
function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>
```

查询网络路由跟踪信息，使用Promise方式作为异步方法。

> **说明：**&gt;
> 应用调用该接口需申请精确位置权限。<!--RP1-->根据[申请位置权限开发指导](../../../device/location/location-permission-guidelines.md)&lt;!--RP1End-
&gt; -&gt;，调用方需同时申请ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.INTERNET and ohos.permission.ACCESS_NET_TRACE_INFO and ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [destination](arkts-network-connection-routeinfo-i.md) | string | 是 |
| option | [TraceRouteOptions](arkts-network-connection-tracerouteoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[TraceRouteInfo](arkts-network-connection-tracerouteinfo-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
