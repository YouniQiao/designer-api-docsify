# startPassiveRanging

## Modules to Import

```TypeScript
import { ranging } from '@kit.ConnectivityKit';
```

## startPassiveRanging

```TypeScript
function startPassiveRanging(capabilityType: RangingTypes): Promise<number>
```

Starts passive ranging mode.

Upon successful startup, returns a handle identifier for the passive ranging session and begins broadcasting ranging packets.

The returned handle can be used to stop the passive ranging broadcast via stopPassiveRanging.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function startPassiveRanging(capabilityType: RangingTypes): Promise<int>--><!--Device-ranging-function startPassiveRanging(capabilityType: RangingTypes): Promise<int>-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [capabilityType](arkts-connectivity-ranging-rangingparams-i.md) | [RangingTypes](arkts-connectivity-ranging-rangingtypes-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 34900052 |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 34900053 |
| [34900099](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
