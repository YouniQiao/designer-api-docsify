# getNetAccessPolicy

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## getNetAccessPolicy

```TypeScript
function getNetAccessPolicy(): Promise<NetAccessPolicy>
```

Queries the network access policy of an application (whether cellular or Wi-Fi network access is allowed). You can check the policy by choosing **Settings**   
> **Mobile network**
> **Manage data usage**
> **Network access**. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[NetAccessPolicy](arkts-network-policy-netaccesspolicy-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
