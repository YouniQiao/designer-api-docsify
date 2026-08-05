# getInputMethodEngine

## getInputMethodEngine

```TypeScript
function getInputMethodEngine(): InputMethodEngine
```

Obtains an [InputMethodEngine]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance for the input method. The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getinputmethodability)()

<!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine--><!--Device-inputMethodEngine-function getInputMethodEngine(): InputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | **InputMethodAbility** instance. |

**Example**

```TypeScript
let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```

