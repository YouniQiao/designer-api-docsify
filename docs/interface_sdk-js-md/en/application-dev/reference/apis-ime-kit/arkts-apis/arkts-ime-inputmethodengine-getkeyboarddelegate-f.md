# getKeyboardDelegate

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## getKeyboardDelegate

```TypeScript
function getKeyboardDelegate(): KeyboardDelegate
```

Obtains a [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) instance for the input method.

The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and more.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate--><!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) | KeyboardDelegate** instance. |

## Examples

```TypeScript
let KeyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.getKeyboardDelegate();
```


## getKeyboardDelegate

```TypeScript
function getKeyboardDelegate(): KeyboardDelegate | null
```

Get KeyboardDelegate object to subscribe key event or events about editor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate | null--><!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate | null-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) | the object of KeyboardDelegate. |

