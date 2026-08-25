# getInputMethodAbility

## 导入模块

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## getInputMethodAbility

```TypeScript
function getInputMethodAbility(): InputMethodAbility
```

获取输入法能力对象实例[InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md)，仅支持输入法应用调用。 <br> <br>输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件、创建/销毁输入法面板等。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) |

**示例**

```TypeScript
// 获取输入法应用客户端实例
let InputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
```


## getInputMethodAbility

```TypeScript
function getInputMethodAbility(): InputMethodAbility | null
```

获取输入法能力对象实例[InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md)，仅支持输入法应用调用。 <br> <br>输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件、创建/销毁输入法面板等。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) \| null |

**示例**

参见 [getInputMethodAbility](#getinputmethodability)
