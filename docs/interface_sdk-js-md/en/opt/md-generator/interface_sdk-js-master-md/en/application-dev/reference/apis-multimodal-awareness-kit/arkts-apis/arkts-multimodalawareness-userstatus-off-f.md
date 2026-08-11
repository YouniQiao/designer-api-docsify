# off

## Modules to Import

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## off('userAgeGroupDetected')

```TypeScript
function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void
```

Disables the age group detection function.

> **NOTE：**
> 
> This API is supported only on some phones. Error code **33900003** is returned if it is called on unsupported
> phones.

**Since:** 20

**Deprecated since:** 24

<!--Device-userStatus-function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void--><!--Device-userStatus-function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'userAgeGroupDetected' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserClassification&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) |
| 33900003 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    userStatus.off('userAgeGroupDetected');
    console.info("off succeeded");
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed off and err code is " + error.code);
}
```
