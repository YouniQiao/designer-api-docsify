# getDefaultNetSync

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## getDefaultNetSync

```TypeScript
function getDefaultNetSync(): NetHandle
```

Obtains the data network that is activated by default. To call this method, you must have the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-connection-function getDefaultNetSync(): NetHandle--><!--Device-connection-function getDefaultNetSync(): NetHandle-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| NetHandle | if the default network is not activated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getDefaultNetSync();
```

