# getProxyMode (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getProxyMode

```TypeScript
function getProxyMode(): Promise<ProxyMode>
```

Obtain the proxy mode [ProxyMode](arkts-network-connection-proxymode-e-sys.md#ProxyMode-(System-API)).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-connection-function getProxyMode(): Promise<ProxyMode>--><!--Device-connection-function getProxyMode(): Promise<ProxyMode>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ProxyMode](arkts-network-connection-proxymode-e-sys.md)&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getProxyMode().then(mode => {
    console.info("Current proxy mode:", mode);
}).catch((error: BusinessError) => {
    console.error("Error getting proxy mode:", error);
});
```

