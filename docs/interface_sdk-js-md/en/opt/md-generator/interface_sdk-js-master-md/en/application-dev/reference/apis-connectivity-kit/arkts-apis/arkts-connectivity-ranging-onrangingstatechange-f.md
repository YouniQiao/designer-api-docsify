# onRangingStateChange

## Modules to Import

```TypeScript
import { ranging } from '@kit.ConnectivityKit';
```

## onRangingStateChange

```TypeScript
function onRangingStateChange(callback: Callback<RangingStateChangeInfo>): void
```

Registers a callback to receive ranging state change notifications.

Notifies state changes for both active ranging and passive ranging operations.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function onRangingStateChange(callback: Callback<RangingStateChangeInfo>): void--><!--Device-ranging-function onRangingStateChange(callback: Callback<RangingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RangingStateChangeInfo](arkts-connectivity-ranging-rangingstatechangeinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [34900099](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
