# offRangingStateChange

## Modules to Import

```TypeScript
import { ranging } from '@kit.ConnectivityKit';
```

## offRangingStateChange

```TypeScript
function offRangingStateChange(callback?: Callback<RangingStateChangeInfo>): void
```

Unsubscribe from ranging state change events.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function offRangingStateChange(callback?: Callback<RangingStateChangeInfo>): void--><!--Device-ranging-function offRangingStateChange(callback?: Callback<RangingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RangingStateChangeInfo](arkts-connectivity-ranging-rangingstatechangeinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
