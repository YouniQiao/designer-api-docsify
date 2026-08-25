# getProxyMode (System API)

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getProxyMode

```TypeScript
function getProxyMode(): Promise<ProxyMode>
```

Obtains the current proxy mode. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ProxyMode](arkts-network-connection-proxymode-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
