# getConnectionState

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## getConnectionState

```TypeScript
function getConnectionState(params: ConnectionStateParams): ConnectionState
```

Obtains the connection status for data transfer.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function getConnectionState(params: ConnectionStateParams): ConnectionState--><!--Device-dataTransfer-function getConnectionState(params: ConnectionStateParams): ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [ConnectionStateParams](arkts-connectivity-datatransfer-connectionstateparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ConnectionState](arkts-connectivity-ssap-connectionstate-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 36100003 |
| 36100099 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| 36100044 |
| 36100043 |
| 36100041 |
