# getInputMethodEngine

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## getInputMethodEngine

```TypeScript
function getInputMethodEngine(): InputMethodEngine
```

Obtains an [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md#InputMethodEngine) instance for the input method.

The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getInputMethodAbility)()

<!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine--><!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) |

## Examples

```TypeScript
let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```
