# SymbolOptions

Declare type SymbolOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class SymbolOptions--><!--Device-unnamed-export declare class SymbolOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## effectStrategy

```TypeScript
public effectStrategy?: SymbolEffectStrategy
```

Effect strategy of the symbol glyph.Default value: **SymbolEffectStrategy.NONE**.  
**NOTE：**For the resources referenced in **\$r('sys.symbol.ohos_*')**, only **ohos_wifi** supports the hierarchical effect.

**Type:** SymbolEffectStrategy

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SymbolOptions-public effectStrategy?: SymbolEffectStrategy--><!--Device-SymbolOptions-public effectStrategy?: SymbolEffectStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
public fontColor?: Array<ResourceColor>
```

Color of the symbol glyph.Default value: depending on the rendering strategy

**Type:** Array&lt;ResourceColor&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SymbolOptions-public fontColor?: Array<ResourceColor>--><!--Device-SymbolOptions-public fontColor?: Array<ResourceColor>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
public fontSize?: double | string | Resource
```

Size of the symbol glyph.For the number type, the value must be greater than or equal to 0.For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.Default value: system default value

**Type:** double \| string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SymbolOptions-public fontSize?: double | string | Resource--><!--Device-SymbolOptions-public fontSize?: double | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
public fontWeight?: int | FontWeight | string
```

Weight of the symbol glyph.For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a heavier font weight. The default value is **400**.For the string type, only strings of the number type are supported, for example, **"400"**, **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**, which correspond to the enumerated values in **FontWeight**.Default value: **FontWeight.Normal**.

**Type:** int \| FontWeight \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SymbolOptions-public fontWeight?: int | FontWeight | string--><!--Device-SymbolOptions-public fontWeight?: int | FontWeight | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## renderingStrategy

```TypeScript
public renderingStrategy?: SymbolRenderingStrategy
```

Rendering strategy of the symbol glyph.Default value: **SymbolRenderingStrategy.SINGLE**.  
**NOTE：**For the resources referenced in **\$r('sys.symbol.ohos_*')**, only **ohos_trash_circle**, **ohos_folder_badge_plus**, and **ohos_lungs** support the **MULTIPLE_COLOR** modes.

**Type:** SymbolRenderingStrategy

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SymbolOptions-public renderingStrategy?: SymbolRenderingStrategy--><!--Device-SymbolOptions-public renderingStrategy?: SymbolRenderingStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

