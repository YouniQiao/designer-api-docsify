# onUserAgeGroupDetected

## Modules to Import

```TypeScript
import { userStatus } from '@kit.MultimodalAwarenessKit';
import { userStatus } from '@kit.MultimodalAwarenessKit';
```

## onUserAgeGroupDetected

```TypeScript
function onUserAgeGroupDetected(callback: Callback<UserClassification>): void
```

Subscribe to age group detection feature.

**Since:** 23

**Deprecated since:** 24

<!--Device-userStatus-function onUserAgeGroupDetected(callback: Callback<UserClassification>): void--><!--Device-userStatus-function onUserAgeGroupDetected(callback: Callback<UserClassification>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UserClassification](arkts-multimodalawareness-userstatus-userclassification-i.md)&gt; | Yes | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function can not work correctly due to limited <br> device capabilities. |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) | Service exception. Possible causes: <br>1. System error, such as a null pointer and container-related exception. <br>2. Node-API invocation exception, such as invalid Node-API status. |
| [33900002](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900002-subscription-failed) | Subscription failed. Possible causes: <br>1. Callback registration failed. <br>2. Failed to bind the native object to the JS wrapper. <br>3. Node-API invocation exception, such as invalid Node-API status. <br>4. IPC request exception. |

