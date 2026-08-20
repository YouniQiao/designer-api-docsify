# getInputMethodAbility

## 导入模块

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## getInputMethodAbility

```TypeScript
function getInputMethodAbility(): InputMethodAbility
```

**起始版本：** 9

<!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility--><!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) | 输入法能力对象。 |

**示例**

```TypeScript
// 获取输入法应用客户端实例
let InputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
```


## getInputMethodAbility

```TypeScript
function getInputMethodAbility(): InputMethodAbility | null
```

**起始版本：** 23

<!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility | null--><!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility | null-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) \| null | 输入法能力对象。 |

