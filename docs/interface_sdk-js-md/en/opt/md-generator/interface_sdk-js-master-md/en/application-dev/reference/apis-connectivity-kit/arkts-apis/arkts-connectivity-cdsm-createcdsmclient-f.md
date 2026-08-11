# createCdsmClient

## Modules to Import

```TypeScript
import { cdsm } from 'kits/@kit.ConnectivityKit';
```

## createCdsmClient

```TypeScript
function createCdsmClient(address: string): CdsmClient
```

Creates a CDSM client instance.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-cdsm-function createCdsmClient(address: string): CdsmClient--><!--Device-cdsm-function createCdsmClient(address: string): CdsmClient-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| address | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CdsmClient](arkts-connectivity-cdsm-cdsmclient-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 36100050 |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100041 |
