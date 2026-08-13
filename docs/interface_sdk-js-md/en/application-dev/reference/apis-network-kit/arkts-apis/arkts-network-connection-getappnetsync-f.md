# getAppNetSync

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getAppNetSync

```TypeScript
function getAppNetSync(): NetHandle
```

Obtains the [NetHandle](arkts-network-connection-nethandle-i.md#NetHandle) bound to a process using [setAppNet](arkts-network-connection-setappnet-f.md#setAppNet).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-connection-function getAppNetSync(): NetHandle--><!--Device-connection-function getAppNetSync(): NetHandle-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| NetHandle | Returns the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getAppNetSync();
```

