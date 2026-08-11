# getDefaultNetSync

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getDefaultNetSync

```TypeScript
function getDefaultNetSync(): NetHandle
```

Obtains the data network that is activated by default.To call this method, you must have the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 11

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-connection-function getDefaultNetSync(): NetHandle--><!--Device-connection-function getDefaultNetSync(): NetHandle-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NetHandle](arkts-network-connection-nethandle-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getDefaultNetSync();
```
