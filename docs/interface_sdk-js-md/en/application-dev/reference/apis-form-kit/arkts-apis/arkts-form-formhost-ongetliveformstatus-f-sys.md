# onGetLiveFormStatus (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## onGetLiveFormStatus

```TypeScript
function onGetLiveFormStatus(callback: formInfo.GetLiveFormStatusCallback): void
```

Listens to the event of get live form status.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
| 202 | The application is not a system application. |

