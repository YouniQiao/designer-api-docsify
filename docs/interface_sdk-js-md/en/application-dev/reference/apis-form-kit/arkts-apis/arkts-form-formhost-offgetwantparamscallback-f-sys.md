# offGetWantParamsCallback (System API)

## Modules to Import

```TypeScript
import { formHost } from 'formHost';
```

## offGetWantParamsCallback

```TypeScript
function offGetWantParamsCallback(callback?: formInfo.GetWantParamsCallback): void
```

Unregister callback of getting the want parameters of the form.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function offGetWantParamsCallback(callback?: formInfo.GetWantParamsCallback): void--><!--Device-formHost-function offGetWantParamsCallback(callback?: formInfo.GetWantParamsCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | formInfo.GetWantParamsCallback | No | the callback for getting want parameters of the form. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [16500050](../errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

