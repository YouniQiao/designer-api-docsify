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

**Deprecated since:** 24

<!--Device-userStatus-function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void--><!--Device-userStatus-function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'userAgeGroupDetected' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserClassification&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) |
| [33900002](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900002-subscription-failed) |

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
