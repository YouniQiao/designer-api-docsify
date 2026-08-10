# getInputMethodEngine

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## getInputMethodEngine

```TypeScript
function getInputMethodEngine(): InputMethodEngine
```

获取输入法应用客户端实例[InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md)（输入法引擎）。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件等。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getinputmethodability)()

<!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine--><!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) | 输入法应用客户端。 |

## Examples

```TypeScript
let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```

