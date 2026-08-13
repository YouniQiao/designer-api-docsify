# queryTraceRoute

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## queryTraceRoute

```TypeScript
function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>
```

Query a network trace route.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET and ohos.permission.ACCESS_NET_TRACE_INFO and ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>--><!--Device-connection-function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| destination | string | Yes | the destination domain or address. |
| option | [TraceRouteOptions](arkts-network-connection-tracerouteoptions-i.md) | No | the trace route option. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[TraceRouteInfo](arkts-network-connection-tracerouteinfo-i.md)[]&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

