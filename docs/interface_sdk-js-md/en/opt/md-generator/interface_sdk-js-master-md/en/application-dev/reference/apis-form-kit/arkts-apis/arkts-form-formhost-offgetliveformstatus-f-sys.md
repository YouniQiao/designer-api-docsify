# offGetLiveFormStatus (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## offGetLiveFormStatus

```TypeScript
function offGetLiveFormStatus(callback?: formInfo.GetLiveFormStatusCallback): void
```

Cancels Listening to the event of get live form status.

**Since:** 23

**Deprecated since:** -1

<!--Device-formHost-function offGetLiveFormStatus(callback?: formInfo.GetLiveFormStatusCallback): void--><!--Device-formHost-function offGetLiveFormStatus(callback?: formInfo.GetLiveFormStatusCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | formInfo.GetLiveFormStatusCallback | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
