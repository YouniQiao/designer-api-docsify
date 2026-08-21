# EditorAttribute

@brief Represents the attributes of the edit box.

**Since:** 23

<!--Device-inputMethodEngine-interface EditorAttribute--><!--Device-inputMethodEngine-interface EditorAttribute-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## abilityName

```TypeScript
readonly abilityName?: string
```

@brief Ability name set for the edit box.

**Type:** string

**Since:** 23

<!--Device-EditorAttribute-readonly abilityName?: string--><!--Device-EditorAttribute-readonly abilityName?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## bundleName

```TypeScript
readonly bundleName?: string
```

@brief Name of the application package to which the edit box belongs. The value may be **""**. Handle this scenario when using the attribute.

**Type:** string

**Since:** 23

<!--Device-EditorAttribute-readonly bundleName?: string--><!--Device-EditorAttribute-readonly bundleName?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## capitalizeMode

```TypeScript
readonly capitalizeMode?: CapitalizeMode
```

@brief Whether to capitalize the first letter in the edit box. If it is not set or is set to an invalid value, the first letter is not capitalized by default.

**Type:** CapitalizeMode

**Since:** 23

<!--Device-EditorAttribute-readonly capitalizeMode?: CapitalizeMode--><!--Device-EditorAttribute-readonly capitalizeMode?: CapitalizeMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## consumeKeyEvents

```TypeScript
readonly consumeKeyEvents?: boolean
```

@brief Whether the editor supports consuming key events.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditorAttribute-readonly consumeKeyEvents?: boolean--><!--Device-EditorAttribute-readonly consumeKeyEvents?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## displayId

```TypeScript
readonly displayId?: long
```

@brief Screen ID of the window corresponding to the edit box. If window ID is not set, the screen ID of the focused window is used.

**Type:** long

**Since:** 23

<!--Device-EditorAttribute-readonly displayId?: long--><!--Device-EditorAttribute-readonly displayId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## enterKeyType

```TypeScript
readonly enterKeyType: int
```

@brief Function attributes of the edit box. For details, see function key definitions in constants.

**Type:** int

**Since:** 23

<!--Device-EditorAttribute-readonly enterKeyType: int--><!--Device-EditorAttribute-readonly enterKeyType: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## extraConfig

```TypeScript
readonly extraConfig?: InputMethodExtraConfig
```

@brief Extra information about the input method.

**Type:** [InputMethodExtraConfig](arkts-ime-inputmethod-extraconfig-inputmethodextraconfig-i.md)

**Since:** 23

<!--Device-EditorAttribute-readonly extraConfig?: InputMethodExtraConfig--><!--Device-EditorAttribute-readonly extraConfig?: InputMethodExtraConfig-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## gradientMode

```TypeScript
readonly gradientMode?: GradientMode
```

@brief Gradient mode.

**Type:** [GradientMode](arkts-ime-inputmethodengine-gradientmode-e.md)

**Since:** 23

<!--Device-EditorAttribute-readonly gradientMode?: GradientMode--><!--Device-EditorAttribute-readonly gradientMode?: GradientMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## immersiveMode

```TypeScript
readonly immersiveMode?: ImmersiveMode
```

@brief Immersive mode of the input method.

**Type:** ImmersiveMode

**Since:** 23

<!--Device-EditorAttribute-readonly immersiveMode?: ImmersiveMode--><!--Device-EditorAttribute-readonly immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## inputPattern

```TypeScript
readonly inputPattern: int
```

@brief Text attribute of the edit box. For details, see edit box definitions in constants.

**Type:** int

**Since:** 23

<!--Device-EditorAttribute-readonly inputPattern: int--><!--Device-EditorAttribute-readonly inputPattern: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## isTextPreviewSupported

```TypeScript
isTextPreviewSupported: boolean
```

@brief Whether text preview is supported. <br> <br>- **true**: Supported. <br>- **false**: Unsupported.

**Type:** boolean

**Since:** 23

<!--Device-EditorAttribute-isTextPreviewSupported: boolean--><!--Device-EditorAttribute-isTextPreviewSupported: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## placeholder

```TypeScript
readonly placeholder?: string
```

@brief Placeholder information set for the edit box.

**Type:** string

**Since:** 23

<!--Device-EditorAttribute-readonly placeholder?: string--><!--Device-EditorAttribute-readonly placeholder?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## windowId

```TypeScript
readonly windowId?: int
```

@brief ID of the window where the edit box is located.

**Type:** int

**Since:** 23

<!--Device-EditorAttribute-readonly windowId?: int--><!--Device-EditorAttribute-readonly windowId?: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

