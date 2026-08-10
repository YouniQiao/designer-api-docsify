# getSystemInputMethodConfigAbility

## 导入模块

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## getSystemInputMethodConfigAbility

```TypeScript
function getSystemInputMethodConfigAbility(): ElementName
```

获取系统输入法设置界面Ability信息。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-inputMethod-function getSystemInputMethodConfigAbility(): ElementName--><!--Device-inputMethod-function getSystemInputMethodConfigAbility(): ElementName-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 系统输入法设置界面Ability的ElementName。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';

let inputMethodConfig: bundleManager.ElementName = inputMethod.getSystemInputMethodConfigAbility();
```

