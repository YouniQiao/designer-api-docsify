# EditorAttribute

编辑框属性值。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-inputMethodEngine-interface EditorAttribute--><!--Device-inputMethodEngine-interface EditorAttribute-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## abilityName

```TypeScript
readonly abilityName?: string
```

编辑框设置的ability名称。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly abilityName?: string--><!--Device-EditorAttribute-readonly abilityName?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## bundleName

```TypeScript
readonly bundleName?: string
```

编辑框所属应用包名；该值可能为""，使用该属性时需要考虑为""的场景。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly bundleName?: string--><!--Device-EditorAttribute-readonly bundleName?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## capitalizeMode

```TypeScript
readonly capitalizeMode?: CapitalizeMode
```

编辑框设置大小写模式。如果没有设置或设置非法值，默认不进行任何首字母大写处理。

**Type:** [CapitalizeMode](arkts-ime-inputmethod-capitalizemode-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly capitalizeMode?: CapitalizeMode--><!--Device-EditorAttribute-readonly capitalizeMode?: CapitalizeMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## consumeKeyEvents

```TypeScript
readonly consumeKeyEvents?: boolean
```

编辑框是否具有完整处理字母、字符、功能等按键的能力。

- 值为true，表示具备此能力。  
- 值为false，表示不具备此能力。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditorAttribute-readonly consumeKeyEvents?: boolean--><!--Device-EditorAttribute-readonly consumeKeyEvents?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## displayId

```TypeScript
readonly displayId?: long
```

编辑框设置窗口对应的屏幕ID。如果没有设置windowId，取当前焦点窗口屏幕ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly displayId?: long--><!--Device-EditorAttribute-readonly displayId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## enterKeyType

```TypeScript
readonly enterKeyType: int
```

编辑框的功能属性

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly enterKeyType: int--><!--Device-EditorAttribute-readonly enterKeyType: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## extraConfig

```TypeScript
readonly extraConfig?: InputMethodExtraConfig
```

输入法扩展信息。

**Type:** [InputMethodExtraConfig](arkts-ime-inputmethod-extraconfig-inputmethodextraconfig-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly extraConfig?: InputMethodExtraConfig--><!--Device-EditorAttribute-readonly extraConfig?: InputMethodExtraConfig-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## gradientMode

```TypeScript
readonly gradientMode?: GradientMode
```

渐变模式。如果没有设置或设置非法值，默认不使用渐变模式。

**Type:** [GradientMode](arkts-ime-inputmethodengine-gradientmode-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly gradientMode?: GradientMode--><!--Device-EditorAttribute-readonly gradientMode?: GradientMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## immersiveMode

```TypeScript
readonly immersiveMode?: ImmersiveMode
```

输入法沉浸模式。

**Type:** [ImmersiveMode](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-immersivemode-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly immersiveMode?: ImmersiveMode--><!--Device-EditorAttribute-readonly immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## inputPattern

```TypeScript
readonly inputPattern: int
```

编辑框的文本属性

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly inputPattern: int--><!--Device-EditorAttribute-readonly inputPattern: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## isTextPreviewSupported

```TypeScript
isTextPreviewSupported: boolean
```

编辑框是否支持预上屏。

- 值为true，表示支持。  
- 值为false，表示不支持。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-isTextPreviewSupported: boolean--><!--Device-EditorAttribute-isTextPreviewSupported: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## placeholder

```TypeScript
readonly placeholder?: string
```

编辑框设置的占位符信息。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly placeholder?: string--><!--Device-EditorAttribute-readonly placeholder?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## windowId

```TypeScript
readonly windowId?: int
```

编辑框设置所属窗口ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-EditorAttribute-readonly windowId?: int--><!--Device-EditorAttribute-readonly windowId?: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

