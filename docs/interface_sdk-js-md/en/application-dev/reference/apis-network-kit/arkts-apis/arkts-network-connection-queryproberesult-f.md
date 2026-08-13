# queryProbeResult

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## queryProbeResult

```TypeScript
function queryProbeResult(destination: string, duration: int): Promise<ProbeResultInfo>
```

Query a network probe result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function queryProbeResult(destination: string, duration: int): Promise<ProbeResultInfo>--><!--Device-connection-function queryProbeResult(destination: string, duration: int): Promise<ProbeResultInfo>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| destination | string | Yes | the distination domain or address. |
| duration | int | Yes | probe duration. Unit: second. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ProbeResultInfo](arkts-network-connection-proberesultinfo-i.md)&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

