# getKeyboardDelegate

## getKeyboardDelegate

```TypeScript
function getKeyboardDelegate(): KeyboardDelegate
```

Obtains a [KeyboardDelegate]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance for the input method. The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and more.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate--><!--Device-inputMethodEngine-function getKeyboardDelegate(): KeyboardDelegate-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | **KeyboardDelegate** instance. |

**Example**

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
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the object of KeyboardDelegate. |

