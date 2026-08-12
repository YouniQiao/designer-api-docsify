# setPacUrl

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## setPacUrl

```TypeScript
function setPacUrl(pacUrl: string): void
```

Set the URL [pacUrl](pacUrl) of the current PAC script.To invoke this method, you must have the {@code ohos.permission.SET_PAC_URL} permission.

**Since:** 15

**Required permissions:** ohos.permission.SET_PAC_URL

<!--Device-connection-function setPacUrl(pacUrl: string): void--><!--Device-connection-function setPacUrl(pacUrl: string): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pacUrl | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [2100002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let pacUrl = "xxx";
connection.setPacUrl(pacUrl);
```
