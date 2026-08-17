# onGetLiveFormStatus (System API)

## Modules to Import

```TypeScript
import { formHost } from 'formHost';
```

## onGetLiveFormStatus

```TypeScript
function onGetLiveFormStatus(callback: formInfo.GetLiveFormStatusCallback): void
```

Listens to the event of get live form status.

**Since:** 23

<!--Device-formHost-function onGetLiveFormStatus(callback: formInfo.GetLiveFormStatusCallback): void--><!--Device-formHost-function onGetLiveFormStatus(callback: formInfo.GetLiveFormStatusCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | formInfo.GetLiveFormStatusCallback | Yes | The callback of get live form status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

