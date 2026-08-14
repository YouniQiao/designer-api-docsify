# disableEthernetInterface (System API)

## Modules to Import

```TypeScript
import { ethernet } from 'ethernet';
```

## disableEthernetInterface

```TypeScript
function disableEthernetInterface(): Promise<void>
```

Disable the ethernet interface.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-ethernet-function disableEthernetInterface(): Promise<void>--><!--Device-ethernet-function disableEthernetInterface(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned when the ethernet interface is disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) | System internal error. |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) | Failed to connect to the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

