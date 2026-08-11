# getInputMethodEngine

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## getInputMethodEngine

```TypeScript
function getInputMethodEngine(): InputMethodEngine
```

Obtains an [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) instance for the input method.

The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getinputmethodability)()

<!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine--><!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) | InputMethodAbility** instance. |

## Examples

```TypeScript
let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```

