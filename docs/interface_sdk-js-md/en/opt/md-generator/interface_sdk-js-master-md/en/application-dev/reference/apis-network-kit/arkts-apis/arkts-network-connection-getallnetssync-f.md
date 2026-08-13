# getAllNetsSync

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getAllNetsSync

```TypeScript
function getAllNetsSync(): Array<NetHandle>
```

Obtains the list of data networks that are activated. To call this method, you must have the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function getAllNetsSync(): Array<NetHandle>--><!--Device-connection-function getAllNetsSync(): Array<NetHandle>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;NetHandle & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getAllNetsSync();
```
