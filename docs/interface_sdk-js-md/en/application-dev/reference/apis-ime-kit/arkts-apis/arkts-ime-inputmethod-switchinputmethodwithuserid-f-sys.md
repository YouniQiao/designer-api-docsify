# switchInputMethodWithUserId (System API)

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## switchInputMethodWithUserId

```TypeScript
function switchInputMethodWithUserId(bundleName: string, subtypeId?: string, userId?: int): Promise<void>
```

切换输入法，使用promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethod-function switchInputMethodWithUserId(bundleName: string, subtypeId?: string, userId?: int): Promise<void>--><!--Device-inputMethod-function switchInputMethodWithUserId(bundleName: string, subtypeId?: string, userId?: int): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 目标输入法的包名。 |
| subtypeId | string | No | 输入法子类型的ID。如果不设置该参数，则切换到使用默认子类型的目标输入法。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 用户ID。如果不提供： &lt;br&gt;- 如果调用者不是用户0的应用，该值默认为调用者的用户ID。 &lt;br&gt;- 如果调用者是用户0的应用，该值默认为主屏幕的前台用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800023 | the specified user does not exist. |
| 12800005 | configuration persistence error. |
| 201 | permissions check fails. |
| 202 | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

