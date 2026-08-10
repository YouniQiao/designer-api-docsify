# getKeyboardDelegate

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## getKeyboardDelegate

```TypeScript
function getKeyboardDelegate(): KeyboardDelegate
```

获取客户端编辑事件监听代理实例[KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md)（键盘代理对象）。

输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate--><!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) | 客户端编辑事件监听代理。 |

## Examples

```TypeScript
let KeyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.getKeyboardDelegate();
```


## getKeyboardDelegate

```TypeScript
function getKeyboardDelegate(): KeyboardDelegate | null
```

获取客户端编辑事件监听代理实例[KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md)（键盘代理对象）。输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate | null--><!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate | null-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) | 客户端编辑事件监听代理。 |

