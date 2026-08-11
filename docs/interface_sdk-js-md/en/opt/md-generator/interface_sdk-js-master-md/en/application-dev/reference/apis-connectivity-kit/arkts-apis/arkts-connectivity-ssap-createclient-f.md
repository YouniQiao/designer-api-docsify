# createClient

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## createClient

```TypeScript
function createClient(address: string): Client
```

Creates a SSAP client instance.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ssap-function createClient(address: string): Client--><!--Device-ssap-function createClient(address: string): Client-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| address | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Client](arkts-connectivity-ssap-client-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100041 |
