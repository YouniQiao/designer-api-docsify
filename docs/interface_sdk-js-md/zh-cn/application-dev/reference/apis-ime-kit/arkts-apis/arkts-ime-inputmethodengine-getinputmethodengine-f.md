# getInputMethodEngine

## 导入模块

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## getInputMethodEngine

```TypeScript
function getInputMethodEngine(): InputMethodEngine
```

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md)()

<!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine--><!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) | 输入法应用客户端。 |

**示例**

```TypeScript
// 获取输入法应用客户端实例（已废弃）
let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```

