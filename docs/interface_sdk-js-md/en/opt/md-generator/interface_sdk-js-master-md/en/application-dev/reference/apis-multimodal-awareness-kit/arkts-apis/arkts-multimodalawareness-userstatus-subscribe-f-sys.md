# subscribe (System API)

## Modules to Import

```TypeScript
```

## subscribe

```TypeScript
function subscribe(featureId: UserStatusFeature, callback: Callback<UserStatusData>,
    deviceInfo?: DeviceInfo[]): number
```

Subscribes to user status monitoring.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-userStatus-function subscribe(featureId: UserStatusFeature, callback: Callback<UserStatusData>,    deviceInfo?: DeviceInfo[]): int--><!--Device-userStatus-function subscribe(featureId: UserStatusFeature, callback: Callback<UserStatusData>,    deviceInfo?: DeviceInfo[]): int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| featureId | [UserStatusFeature](arkts-multimodalawareness-userstatus-userstatusfeature-e-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md)&gt; | Yes |
| deviceInfo | [DeviceInfo[]](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-deviceinfo-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) |
| [33900002](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900002-subscription-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
