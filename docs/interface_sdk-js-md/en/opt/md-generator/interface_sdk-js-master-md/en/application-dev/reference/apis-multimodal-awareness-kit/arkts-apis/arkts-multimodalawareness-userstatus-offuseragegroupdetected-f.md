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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UserClassification](arkts-multimodalawareness-userstatus-userclassification-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) |
| 33900003 |
