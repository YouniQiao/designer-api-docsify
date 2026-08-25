# getInputMethodEngine

## 导入模块

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## getInputMethodEngine

```TypeScript
function getInputMethodEngine(): InputMethodEngine
```

获取输入法应用客户端实例[InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md)（输入法引擎）。 <br> <br>输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件等。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md)()

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) |

**示例**

```TypeScript
// 获取输入法应用客户端实例（已废弃）
let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```
