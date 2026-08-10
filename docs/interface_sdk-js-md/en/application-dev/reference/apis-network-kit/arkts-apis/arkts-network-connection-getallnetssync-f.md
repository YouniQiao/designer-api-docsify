# getAllNetsSync

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getAllNetsSync

```TypeScript
function getAllNetsSync(): Array<NetHandle>
```

Obtains the list of data networks that are activated.To call this method, you must have the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function getAllNetsSync(): Array<NetHandle>--><!--Device-connection-function getAllNetsSync(): Array<NetHandle>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;NetHandle&gt; | Returns data networks that are activated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getAllNetsSync();
```

