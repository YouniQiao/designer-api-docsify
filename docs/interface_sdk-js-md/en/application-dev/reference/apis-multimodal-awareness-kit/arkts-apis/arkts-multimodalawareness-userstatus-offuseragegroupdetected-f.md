# offUserAgeGroupDetected

## Modules to Import

```TypeScript
import { userStatus } from '@kit.MultimodalAwarenessKit';
```

## offUserAgeGroupDetected

```TypeScript
function offUserAgeGroupDetected(callback?: Callback<UserClassification>): void
```

Unsubscribe to age group detection feature.

**Since:** 23

**Deprecated since:** 24

<!--Device-userStatus-function offUserAgeGroupDetected(callback?: Callback<UserClassification>): void--><!--Device-userStatus-function offUserAgeGroupDetected(callback?: Callback<UserClassification>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[UserClassification](arkts-multimodalawareness-userstatus-userclassification-i.md)&gt; | No | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function can not work correctly due to limited <br> device capabilities. |
| [33900001](../errorcode-userStatus.md#33900001-service-exception) | Service exception. Possible causes: <br>1. System error, such as a null pointer and container-related exception. <br>2. Node-API invocation exception, such as invalid Node-API status. |
| 33900003 | Unsubscription failed. Possible causes: <br>1. Callback failure. <br>2. Node-API invocation exception, such as invalid Node-API status. <br>3. IPC request exception. |

