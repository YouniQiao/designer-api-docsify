# getConnectionState

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## getConnectionState

```TypeScript
function getConnectionState(params: ConnectionStateParams): ConnectionState
```

Obtains the connection status for data transfer.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function getConnectionState(params: ConnectionStateParams): ConnectionState--><!--Device-dataTransfer-function getConnectionState(params: ConnectionStateParams): ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [ConnectionStateParams](arkts-connectivity-datatransfer-connectionstateparams-i.md) | Yes | Parameters used to obtain the connection status. |

**Return value:**

| Type | Description |
| --- | --- |
| ConnectionState | Returns the connection status for data transfer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 36100044 | NearLink standard UUID not allowed. |
| 36100043 | Invalid UUID in connection parameters. |
| 36100041 | Invalid address. |

