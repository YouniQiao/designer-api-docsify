# getSystemInputMethodConfigAbility（系统接口）

## 导入模块

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## getSystemInputMethodConfigAbility

```TypeScript
function getSystemInputMethodConfigAbility(userId?: int): ElementName
```

获取指定用户的系统输入法设置界面Ability信息。用于启动系统输入法配置界面。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethod-function getSystemInputMethodConfigAbility(userId?: int): ElementName--><!--Device-inputMethod-function getSystemInputMethodConfigAbility(userId?: int): ElementName-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 否 | 用户ID。如果不提供： &lt;br&gt;- 如果调用者不是用户0的应用，该值默认为调用者的用户ID。 &lt;br&gt;- 如果调用者是用户0的应用，该值默认为主屏幕的前台用户ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 系统输入法设置界面Ability的ElementName。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12800023 | the specified user does not exist. |
| 202 | not system application. |
| 12800025 | cross-user operation denied. Only user 0 applications are authorized for this operation. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800024 | the specified user is not in the foreground. |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';

try {
  let inputMethodConfig: bundleManager.ElementName = inputMethod.getSystemInputMethodConfigAbility(100);
  console.info('Succeeded in getting system input method config ability, bundleName: ' + inputMethodConfig.bundleName);
} catch (err) {
  console.error(`Failed to getSystemInputMethodConfigAbility. Code: ${err.code}, message: ${err.message}`);
}
```

