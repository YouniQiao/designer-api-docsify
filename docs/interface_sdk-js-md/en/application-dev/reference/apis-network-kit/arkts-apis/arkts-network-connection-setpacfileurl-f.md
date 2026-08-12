# setPacFileUrl

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## setPacFileUrl

```TypeScript
function setPacFileUrl(pacFileUrl: string): void
```

Set the URL [pacFileUrl](pacFileUrl) of the current PAC script.Proxy information can be obtained through parsing the script address.To invoke this method, you must have the {@code ohos.permission.SET_PAC_URL} permission.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.SET_PAC_URL

<!--Device-connection-function setPacFileUrl(pacFileUrl: string): void--><!--Device-connection-function setPacFileUrl(pacFileUrl: string): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pacFileUrl | string | Yes | Indicates the URL of the current PAC script. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let pacFileUrl = "http://example.com/proxy.pac";
connection.setPacFileUrl(pacFileUrl);
```

