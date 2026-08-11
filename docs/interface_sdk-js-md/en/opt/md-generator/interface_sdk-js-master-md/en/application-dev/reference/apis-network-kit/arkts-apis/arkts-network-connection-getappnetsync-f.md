# getAppNetSync

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getAppNetSync

```TypeScript
function getAppNetSync(): NetHandle
```

Obtains the {@link NetHandle} bound to a process using {@link setAppNet}.

**Since:** 10

<!--Device-connection-function getAppNetSync(): NetHandle--><!--Device-connection-function getAppNetSync(): NetHandle-End-->

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

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getAppNetSync();
```
