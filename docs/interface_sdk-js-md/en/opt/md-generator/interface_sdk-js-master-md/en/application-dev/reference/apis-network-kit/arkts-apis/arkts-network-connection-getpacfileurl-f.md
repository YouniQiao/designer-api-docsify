# getPacFileUrl

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getPacFileUrl

```TypeScript
function getPacFileUrl(): string
```

Obtain the URL {@link pacFileUrl} of the current PAC script.

**Since:** 20

<!--Device-connection-function getPacFileUrl(): string--><!--Device-connection-function getPacFileUrl(): string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let pacFileUrl = connection.getPacFileUrl();
console.info(pacFileUrl);
```
