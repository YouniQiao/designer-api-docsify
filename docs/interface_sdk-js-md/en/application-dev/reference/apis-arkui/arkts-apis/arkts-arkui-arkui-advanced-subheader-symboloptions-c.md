# SymbolOptions

Declare type SymbolOptions

**Since:** 12

<!--Device-unnamed-export declare class SymbolOptions--><!--Device-unnamed-export declare class SymbolOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OperationOption, OperationType, SelectOptions, SubHeader, SymbolOptions } from '@kit.ArkUI';
```

## effectStrategy

```TypeScript
effectStrategy?: SymbolEffectStrategy
```

Effect strategy of the symbol glyph.Default value: **SymbolEffectStrategy.NONE**.  
**NOTE：**For the resources referenced in **\$r('sys.symbol.ohos_*')**, only **ohos_wifi** supports the hierarchical effect.

**Type:** SymbolEffectStrategy

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymbolOptions-effectStrategy?: SymbolEffectStrategy--><!--Device-SymbolOptions-effectStrategy?: SymbolEffectStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: Array<ResourceColor>
```

Color of the symbol glyph.Default value: depending on the rendering strategy

**Type:** Array&lt;ResourceColor&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymbolOptions-fontColor?: Array<ResourceColor>--><!--Device-SymbolOptions-fontColor?: Array<ResourceColor>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: number | string | Resource
```

Size of the symbol glyph.For the number type, the value must be greater than or equal to 0.For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.Default value: system default value

**Type:** number \| string \| Resource

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymbolOptions-fontSize?: number | string | Resource--><!--Device-SymbolOptions-fontSize?: number | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight?: number | FontWeight | string
```

Weight of the symbol glyph.For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a heavier font weight. The default value is **400**.For the string type, only strings of the number type are supported, for example, **"400"**, **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**, which correspond to the enumerated values in **FontWeight**.Default value: **FontWeight.Normal**.

**Type:** number \| FontWeight \| string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymbolOptions-fontWeight?: number | FontWeight | string--><!--Device-SymbolOptions-fontWeight?: number | FontWeight | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## renderingStrategy

```TypeScript
renderingStrategy?: SymbolRenderingStrategy
```

Rendering strategy of the symbol glyph.Default value: **SymbolRenderingStrategy.SINGLE**.  
**NOTE：**For the resources referenced in **\$r('sys.symbol.ohos_*')**, only **ohos_trash_circle**, **ohos_folder_badge_plus**, and **ohos_lungs** support the **MULTIPLE_COLOR** modes.

**Type:** SymbolRenderingStrategy

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymbolOptions-renderingStrategy?: SymbolRenderingStrategy--><!--Device-SymbolOptions-renderingStrategy?: SymbolRenderingStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

