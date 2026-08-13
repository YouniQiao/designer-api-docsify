# sendNotice (System API)

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## sendNotice

```TypeScript
function sendNotice(noticeType: NoticeType, eventData: string): void
```

Sends a notification from the user authentication widget. When the unified authentication widget is used for user authentication, this API is used to receive notifications from the unified authentication widget and send the notifications to the user authentication framework.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SUPPORT_USER_AUTH

<!--Device-userAuth-function sendNotice(noticeType: NoticeType, eventData: string): void--><!--Device-userAuth-function sendNotice(noticeType: NoticeType, eventData: string): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| noticeType | [NoticeType](arkts-userauthentication-userauth-noticetype-e-sys.md) | Yes |
| eventData | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface  EventData {
  widgetContextId: number;
  event: string;
  version: string;
  payload: Payload;
}
interface Payload {
  type: string[];
}
try {
  const eventData : EventData = {
    widgetContextId: 123456,
    event: 'EVENT_AUTH_TYPE_READY',
    version: '1',
    payload: {
      type: ['pin']
    } as Payload,
  };
  const jsonEventData = JSON.stringify(eventData);
  let noticeType = userAuth.NoticeType.WIDGET_NOTICE;
  userAuth.sendNotice(noticeType, jsonEventData);
  console.info('sendNotice successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`sendNotice failed. Code is ${err?.code}, message is ${err?.message}`);
}
```
