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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-formHost-function offGetLiveFormStatus(callback?: formInfo.GetLiveFormStatusCallback): void--><!--Device-formHost-function offGetLiveFormStatus(callback?: formInfo.GetLiveFormStatusCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | formInfo.GetLiveFormStatusCallback | No | The callback of get live form status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

