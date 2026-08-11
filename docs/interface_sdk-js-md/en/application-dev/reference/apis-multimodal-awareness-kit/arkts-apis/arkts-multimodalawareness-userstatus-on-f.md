# on

## Modules to Import

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## on('userAgeGroupDetected')

```TypeScript
function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void
```

Enables the age group detection function.

When the function is enabled, the application can recommend content based on the age group detection result.

> **NOTE：**
> 
> This API is supported only on some phones. Error code **801** is returned if it is called on unsupported phones.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** 24

<!--Device-userStatus-function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void--><!--Device-userStatus-function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'userAgeGroupDetected' | Yes | Event type. The value **userAgeGroupDetected** indicates the event of enabling age group detection. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserClassification&gt; | Yes | Callback used to return the detection result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) | Service exception. Possible causes: &lt;br&gt;1. System error, such as a null pointer and container-related exception. &lt;br&gt;2. Node-API invocation exception, such as invalid Node-API status. |
| [33900002](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900002-subscription-failed) | Subscription failed. Possible causes: &lt;br&gt;1. Callback registration failed. &lt;br&gt;2. Failed to bind the native object to the JS wrapper. &lt;br&gt;3. Node-API invocation exception, such as invalid Node-API status. &lt;br&gt;4. IPC request exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    userStatus.on('userAgeGroupDetected', (data: userStatus.UserClassification) => {
        console.info('callback succeeded, ageGroup:' + data.ageGroup + ", confidence:" + data.confidence);
    });
    console.info("on succeeded");
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed on and err code is " + error.code);
}
```

