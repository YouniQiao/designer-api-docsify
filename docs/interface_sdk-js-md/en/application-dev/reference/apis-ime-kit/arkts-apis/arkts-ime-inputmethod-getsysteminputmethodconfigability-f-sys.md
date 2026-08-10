# getSystemInputMethodConfigAbility (System API)

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## getSystemInputMethodConfigAbility

```TypeScript
function getSystemInputMethodConfigAbility(userId?: int): ElementName
```

获取指定用户的系统输入法设置界面Ability信息。用于启动系统输入法配置界面。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethod-function getSystemInputMethodConfigAbility(userId?: int): ElementName--><!--Device-inputMethod-function getSystemInputMethodConfigAbility(userId?: int): ElementName-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 用户ID。如果不提供： &lt;br&gt;- 如果调用者不是用户0的应用，该值默认为调用者的用户ID。 &lt;br&gt;- 如果调用者是用户0的应用，该值默认为主屏幕的前台用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 系统输入法设置界面Ability的ElementName。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800023 | the specified user does not exist. |
| 202 | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

