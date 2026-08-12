# subscribe (System API)

## Modules to Import

```TypeScript
import { userStatus } from '@kit.MultimodalAwarenessKit';
```

## subscribe

```TypeScript
function subscribe(featureId: UserStatusFeature, callback: Callback<UserStatusData>,
    deviceInfo?: DeviceInfo[]): int
```

Subscribes to user status monitoring.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-userStatus-function subscribe(featureId: UserStatusFeature, callback: Callback<UserStatusData>,    deviceInfo?: DeviceInfo[]): int--><!--Device-userStatus-function subscribe(featureId: UserStatusFeature, callback: Callback<UserStatusData>,    deviceInfo?: DeviceInfo[]): int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| featureId | [UserStatusFeature](arkts-multimodalawareness-userstatus-userstatusfeature-e-sys.md) | Yes | Indicates the feature to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md)&gt; | Yes | Callback used to return user status data. |
| deviceInfo | DeviceInfo[] | No | List of devices to enable user status monitoring. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the registered callback ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited &lt;br&gt; device capabilities. |
| [33900001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) | Service exception. Possible causes: &lt;br&gt;1. System error, such as null pointer and container-related exception. &lt;br&gt;2. Node-API invocation exception, such as a invalid Node-API status. |
| [33900002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-userStatus.md#33900002-subscription-failed) | Subscription failed. Possible causes: &lt;br&gt;1. Callback registration failed. &lt;br&gt;2. Failed to bind the native object to the JS wrapper. &lt;br&gt;3. Node-API invocation exception, such as invalid Node-API status. &lt;br&gt;4. IPC request exception. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

