# stopRanging

## Modules to Import

```TypeScript
import { ranging } from '@kit.ConnectivityKit';
```

## stopRanging

```TypeScript
function stopRanging(callback: Callback<RangingResult>, params?: RangingParams): void
```

Stops ongoing ranging operations.If no target device is specified, stops ranging for all devices associated with the callback.If a target device is specified, only stops ranging for that specific device.This method also releases all occupied resources. For proper resource management,stopRanging must be called after startRanging to avoid resource leaks.State changes are notified via the onRangingStateChange callback.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function stopRanging(callback: Callback<RangingResult>, params?: RangingParams): void--><!--Device-ranging-function stopRanging(callback: Callback<RangingResult>, params?: RangingParams): void-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RangingResult](arkts-connectivity-ranging-rangingresult-i.md)&gt; | Yes |
| params | [RangingParams](arkts-connectivity-ranging-rangingparams-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| 34900052 |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 34900054 |
| 34900050 |
| [34900099](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
