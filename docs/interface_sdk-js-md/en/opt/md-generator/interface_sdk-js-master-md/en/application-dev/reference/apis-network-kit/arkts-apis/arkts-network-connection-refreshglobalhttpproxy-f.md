# refreshGlobalHttpProxy

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## refreshGlobalHttpProxy

```TypeScript
function refreshGlobalHttpProxy(): Promise<HttpProxy>
```

Notifies the system that global proxy re-authentication is required.Upon receiving the notification, the system will reproces the global proxy's authentication status.

**Since:** 26.0.0

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function refreshGlobalHttpProxy(): Promise<HttpProxy>--><!--Device-connection-function refreshGlobalHttpProxy(): Promise<HttpProxy>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;HttpProxy&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
