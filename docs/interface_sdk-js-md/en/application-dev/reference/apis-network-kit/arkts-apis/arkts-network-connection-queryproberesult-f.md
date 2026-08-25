# queryProbeResult

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## queryProbeResult

```TypeScript
function queryProbeResult(destination: string, duration: number): Promise<ProbeResultInfo>
```

Queries network probe results. If an exception (for example, network disconnection) occurs and the request fails to be sent, the API immediately returns the result without performing subsequent probe. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is used to perform network probe on a target host for a period of time to obtain the packet loss rate
> and RTT information.

**Since:** 26.0.0

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [destination](arkts-network-connection-routeinfo-i.md) | string | Yes |
| duration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ProbeResultInfo](arkts-network-connection-proberesultinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
