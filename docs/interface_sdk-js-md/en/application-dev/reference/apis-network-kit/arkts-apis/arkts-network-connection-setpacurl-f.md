# setPacUrl

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## setPacUrl

```TypeScript
function setPacUrl(pacUrl: string): void
```

Set the URL pacUrl of the current PAC script. To invoke this method, you must have the {@code ohos.permission.SET_PAC_URL} permission.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_PAC_URL

<!--Device-connection-function setPacUrl(pacUrl: string): void--><!--Device-connection-function setPacUrl(pacUrl: string): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pacUrl | string | Yes | Indicates the URL of the current PAC script. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let pacUrl = "xxx";
connection.setPacUrl(pacUrl);
```

