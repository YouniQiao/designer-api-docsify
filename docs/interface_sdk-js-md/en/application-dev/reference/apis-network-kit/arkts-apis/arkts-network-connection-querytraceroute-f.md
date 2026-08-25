# queryTraceRoute

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## queryTraceRoute

```TypeScript
function queryTraceRoute(destination: string, option?: TraceRouteOptions): Promise<TraceRouteInfo[]>
```

Queries the network route tracing information. This API uses a promise to return the result.

> **NOTE：**&gt;
> To call this API, the application needs to apply for the precise location permission. <!--RP1-->According to
> [Applying for Location Permissions (ArkTS)](../../../device/location/location-permission-guidelines.md)<!--RP1
> End-->, the caller needs to apply for both **ohos.permission.APPROXIMATELY_LOCATION** and
> **ohos.permission.LOCATION**.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.INTERNET and ohos.permission.ACCESS_NET_TRACE_INFO and ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
