# setProxyMode (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## setProxyMode

```TypeScript
function setProxyMode(mode: ProxyMode): Promise<void>
```

Set the proxy mode [ProxyMode](arkts-network-connection-proxymode-e-sys.md#ProxyMode-(System-API)).

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-connection-function setProxyMode(mode: ProxyMode): Promise<void>--><!--Device-connection-function setProxyMode(mode: ProxyMode): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [ProxyMode](arkts-network-connection-proxymode-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.setProxyMode(connection.ProxyMode.PROXY_MODE_AUTO).then(() => {
    console.info("Proxy mode set successfully.");
}).catch((error: BusinessError) => {
    console.error("Error setting proxy mode:", error);
});
```
