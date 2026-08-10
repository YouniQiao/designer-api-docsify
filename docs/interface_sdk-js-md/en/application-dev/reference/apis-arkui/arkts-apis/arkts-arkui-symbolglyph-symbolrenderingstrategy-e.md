# SymbolRenderingStrategy

渲染模式的枚举值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum SymbolRenderingStrategy--><!--Device-unnamed-export declare enum SymbolRenderingStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SINGLE

```TypeScript
SINGLE = 0
```

单色渲染策略。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SymbolRenderingStrategy-SINGLE = 0--><!--Device-SymbolRenderingStrategy-SINGLE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MULTIPLE_COLOR

```TypeScript
MULTIPLE_COLOR = 1
```

多色渲染策略，最多可设置三种颜色，仅设置一种颜色时更新第一层颜色，其余保持默认值。仅支持颜色值，透明度设置不生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SymbolRenderingStrategy-MULTIPLE_COLOR = 1--><!--Device-SymbolRenderingStrategy-MULTIPLE_COLOR = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MULTIPLE_OPACITY

```TypeScript
MULTIPLE_OPACITY = 2
```

分层渲染策略，默认颜色为黑色，可设置一种或多种颜色，但仅应用第一种颜色。预定义透明度：第一层100%，第二层50%，第三层20%。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SymbolRenderingStrategy-MULTIPLE_OPACITY = 2--><!--Device-SymbolRenderingStrategy-MULTIPLE_OPACITY = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

