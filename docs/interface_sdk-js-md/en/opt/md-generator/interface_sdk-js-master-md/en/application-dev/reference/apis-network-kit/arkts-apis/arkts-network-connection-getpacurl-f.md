# getPacUrl

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getPacUrl

```TypeScript
function getPacUrl(): string
```

Obtain the URL {@link pacUrl} of the current PAC script.

**Since:** 15

<!--Device-connection-function getPacUrl(): string--><!--Device-connection-function getPacUrl(): string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let pacUrl = connection.getPacUrl();
```
