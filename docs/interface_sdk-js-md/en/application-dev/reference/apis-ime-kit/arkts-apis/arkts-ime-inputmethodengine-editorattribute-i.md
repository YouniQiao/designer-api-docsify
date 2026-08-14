# EditorAttribute

In the following API examples, you must first use [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) to obtain a **KeyboardDelegate** instance, and then call the APIs using the obtained instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-inputMethodEngine-interface EditorAttribute--><!--Device-inputMethodEngine-interface EditorAttribute-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'inputMethodEngine';
```

## abilityName

```TypeScript
readonly abilityName?: string
```

Ability name set for the edit box.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly abilityName?: string--><!--Device-EditorAttribute-readonly abilityName?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## bundleName

```TypeScript
readonly bundleName?: string
```

Name of the application package to which the edit box belongs. The value may be **""**. Handle this scenario when using the attribute.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly bundleName?: string--><!--Device-EditorAttribute-readonly bundleName?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## capitalizeMode

```TypeScript
readonly capitalizeMode?: CapitalizeMode
```

Whether to capitalize the first letter in the edit box. If it is not set or is set to an invalid value, the first letter is not capitalized by default.

**Type:** CapitalizeMode

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly capitalizeMode?: CapitalizeMode--><!--Device-EditorAttribute-readonly capitalizeMode?: CapitalizeMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## consumeKeyEvents

```TypeScript
readonly consumeKeyEvents?: boolean
```

Whether the editor supports consuming key events.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditorAttribute-readonly consumeKeyEvents?: boolean--><!--Device-EditorAttribute-readonly consumeKeyEvents?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## displayId

```TypeScript
readonly displayId?: long
```

Screen ID of the window corresponding to the edit box. If window ID is not set, the screen ID of the focused window is used.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly displayId?: long--><!--Device-EditorAttribute-readonly displayId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## enterKeyType

```TypeScript
readonly enterKeyType: int
```

Function attributes of the edit box. For details, see [function key definitions in constants](arkts-inputmethodengine.md#Constants).

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly enterKeyType: int--><!--Device-EditorAttribute-readonly enterKeyType: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## extraConfig

```TypeScript
readonly extraConfig?: InputMethodExtraConfig
```

Extra information about the input method.

**Type:** [InputMethodExtraConfig](arkts-ime-inputmethod-extraconfig-inputmethodextraconfig-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly extraConfig?: InputMethodExtraConfig--><!--Device-EditorAttribute-readonly extraConfig?: InputMethodExtraConfig-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## gradientMode

```TypeScript
readonly gradientMode?: GradientMode
```

Gradient mode. If this attribute is not specified or is set to an invalid value, the gradient mode is not used by default.

**Type:** [GradientMode](arkts-ime-inputmethodengine-gradientmode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly gradientMode?: GradientMode--><!--Device-EditorAttribute-readonly gradientMode?: GradientMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## immersiveMode

```TypeScript
readonly immersiveMode?: ImmersiveMode
```

Immersive mode of the input method.

**Type:** ImmersiveMode

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly immersiveMode?: ImmersiveMode--><!--Device-EditorAttribute-readonly immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## inputPattern

```TypeScript
readonly inputPattern: int
```

Text attribute of the edit box. For details, see [edit box definitions in constants](arkts-inputmethodengine.md#Constants).

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly inputPattern: int--><!--Device-EditorAttribute-readonly inputPattern: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## isTextPreviewSupported

```TypeScript
isTextPreviewSupported: boolean
```

Whether text preview is supported. - **true**: Supported. - **false**: Unsupported.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-isTextPreviewSupported: boolean--><!--Device-EditorAttribute-isTextPreviewSupported: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## placeholder

```TypeScript
readonly placeholder?: string
```

Placeholder information set for the edit box.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly placeholder?: string--><!--Device-EditorAttribute-readonly placeholder?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## windowId

```TypeScript
readonly windowId?: int
```

ID of the window where the edit box is located.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-EditorAttribute-readonly windowId?: int--><!--Device-EditorAttribute-readonly windowId?: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

