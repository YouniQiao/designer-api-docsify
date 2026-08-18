# queryTraceRoute

## Modules to Import

```TypeScript
```

## queryTraceRoute

```TypeScript
function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>
```

Query a network trace route.

**Since:** 26.0.0

**Required permissions:** ohos.permission.INTERNET and ohos.permission.ACCESS_NET_TRACE_INFO and ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>--><!--Device-connection-function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [destination](arkts-network-connection-routeinfo-i.md) | string | Yes |
| option | [TraceRouteOptions](arkts-network-connection-tracerouteoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[TraceRouteInfo](arkts-network-connection-tracerouteinfo-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dest: string = "www.example.com";
let options: connection.TraceRouteOptions = {
    maxJumpNumber: 30,
    packetsType: connection.PacketsType.NETCONN_PACKETS_ICMP
};

connection.queryTraceRoute(dest, options).then((data: connection.TraceRouteInfo[]) => {
    console.info(JSON.stringify(data));
}).catch((err: BusinessError) => {
    console.error(JSON.stringify(err));
});
```
