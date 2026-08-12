# isDefaultNetMeteredSync

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## isDefaultNetMeteredSync

```TypeScript
function isDefaultNetMeteredSync(): boolean
```

Checks whether data traffic usage on the current network is metered.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function isDefaultNetMeteredSync(): boolean--><!--Device-connection-function isDefaultNetMeteredSync(): boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the current network is metered, else returns false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let isMetered = connection.isDefaultNetMeteredSync();
```

