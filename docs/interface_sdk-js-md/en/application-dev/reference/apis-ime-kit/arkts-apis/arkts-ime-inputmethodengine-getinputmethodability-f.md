# getInputMethodAbility

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
```

## getInputMethodAbility

```TypeScript
function getInputMethodAbility(): InputMethodAbility
```

Obtains an [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md#inputmethodability) instance for the input method. This API can be called only by an input method. The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event, create/ destroy an input method panel, and the like.

**Since:** 9

<!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility--><!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) | InputMethodAbility** instance. |

**Examples**

```TypeScript
let InputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
```


## getInputMethodAbility

```TypeScript
function getInputMethodAbility(): InputMethodAbility | null
```

Get InputMethodAbility object to subscribe events about IME.

**Since:** 23

<!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility | null--><!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility | null-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) | the object of the InputMethodAbility. |

