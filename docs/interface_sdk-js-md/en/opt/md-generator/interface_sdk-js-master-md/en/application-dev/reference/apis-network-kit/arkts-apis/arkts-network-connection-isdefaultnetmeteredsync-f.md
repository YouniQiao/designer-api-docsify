# isDefaultNetMeteredSync

## Modules to Import

```TypeScript
```

## isDefaultNetMeteredSync

```TypeScript
function isDefaultNetMeteredSync(): boolean
```

Checks whether data traffic usage on the current network is metered.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function isDefaultNetMeteredSync(): boolean--><!--Device-connection-function isDefaultNetMeteredSync(): boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';

let isMetered = connection.isDefaultNetMeteredSync();
```
