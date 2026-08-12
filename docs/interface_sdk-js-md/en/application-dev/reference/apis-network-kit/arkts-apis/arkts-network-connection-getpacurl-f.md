# getPacUrl

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getPacUrl

```TypeScript
function getPacUrl(): string
```

Obtain the URL [pacUrl](pacUrl) of the current PAC script.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

<!--Device-connection-function getPacUrl(): string--><!--Device-connection-function getPacUrl(): string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the URL of the current PAC script or empty string if there is no PAC script. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let pacUrl = connection.getPacUrl();
```

