# setPacUrl

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## setPacUrl

```TypeScript
function setPacUrl(pacUrl: string): void
```

Sets the URL of the system-level Proxy Auto Config (PAC) script.

> **NOTE：**&gt;
> Only the script address can be set. The proxy function cannot be parsed or enabled. To set the script and enable
> the proxy, call the [setPacFileUrl](arkts-network-connection-setpacfileurl-f.md) API.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**Required permissions:** ohos.permission.SET_PAC_URL

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pacUrl | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';

let pacUrl = "xxx";
connection.setPacUrl(pacUrl);
```
