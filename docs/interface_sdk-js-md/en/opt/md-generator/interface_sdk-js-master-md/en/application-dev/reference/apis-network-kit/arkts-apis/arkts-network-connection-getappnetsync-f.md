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
| [2100002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100003-system-internal-error) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getAppNetSync();
```
