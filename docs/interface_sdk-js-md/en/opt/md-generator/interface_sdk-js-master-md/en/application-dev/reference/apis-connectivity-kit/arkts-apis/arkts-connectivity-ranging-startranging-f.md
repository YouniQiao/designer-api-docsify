# startRanging

## Modules to Import

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## startRanging

```TypeScript
function startRanging(params: RangingParams, callback: Callback<RangingResult>): void
```

Initiates ranging with a specified device.If the link to the target device is already established, ranging starts directly.If not connected, this interface will: 1. Attempt to establish connection and perform pairing/encryption. 2. Query service to verify the device supports ranging. Initiate ranging upon confirmation.Ranging state updates are notified via onRangingStateChange callback.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function startRanging(params: RangingParams, callback: Callback<RangingResult>): void--><!--Device-ranging-function startRanging(params: RangingParams, callback: Callback<RangingResult>): void-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [RangingParams](arkts-connectivity-ranging-rangingparams-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RangingResult&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 34900052 |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 34900053 |
| 34900054 |
| 34900051 |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
