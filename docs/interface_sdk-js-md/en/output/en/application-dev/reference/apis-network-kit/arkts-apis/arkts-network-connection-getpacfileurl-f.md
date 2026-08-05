# getPacFileUrl

## getPacFileUrl

```TypeScript
function getPacFileUrl(): string
```

Obtain the URL \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ of the current PAC script.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-connection-function getPacFileUrl(): string--><!--Device-connection-function getPacFileUrl(): string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the URL of the current PAC script or empty string if there is no PAC script. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |

**Example**

```TypeScript
import { connection } from '@kit.NetworkKit';

let pacFileUrl = connection.getPacFileUrl();
console.info(pacFileUrl);
```

