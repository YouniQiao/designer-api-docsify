# updateFormLockedState (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## updateFormLockedState

```TypeScript
function updateFormLockedState(formId: string, isLocked: boolean): Promise<void>
```

Notifies the update of the widget lock state. This API uses a promise to return the result.If an application is locked, its widget will also be locked and masked in a locked style. To use the widget, you need to enter the password set for the widget.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function updateFormLockedState(formId: string, isLocked: boolean): Promise<void>--><!--Device-formHost-function updateFormLockedState(formId: string, isLocked: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Widget ID. |
| isLocked | boolean | Yes | A Boolean value indicates whether a widget is in the locked state. The value **true** indicates that the widget is in the locked state, and the value **false** indicates the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | caller is not system app. |

