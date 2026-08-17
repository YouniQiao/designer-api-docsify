# createKeyboardDelegate

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'inputMethodEngine';
```

## createKeyboardDelegate

```TypeScript
function createKeyboardDelegate(): KeyboardDelegate
```

Obtains a [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md#keyboarddelegate) instance for the input method. The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and more.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getkeyboarddelegate)()

<!--Device-inputMethodEngine-function createKeyboardDelegate(): KeyboardDelegate--><!--Device-inputMethodEngine-function createKeyboardDelegate(): KeyboardDelegate-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) | KeyboardDelegate** instance. |

**Examples**

```TypeScript
let keyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.createKeyboardDelegate();
```

