# RichEditorSymbolSpanStyleResult

后端返回的SymbolSpan样式信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface RichEditorSymbolSpanStyleResult--><!--Device-unnamed-declare interface RichEditorSymbolSpanStyleResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## effectStrategy

```TypeScript
effectStrategy: SymbolEffectStrategy
```

SymbolSpan组件动效策略。

默认值：SymbolEffectStrategy.NONE。

**Type:** [SymbolEffectStrategy](arkts-arkui-symboleffectstrategy-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorSymbolSpanStyleResult-effectStrategy: SymbolEffectStrategy--><!--Device-RichEditorSymbolSpanStyleResult-effectStrategy: SymbolEffectStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor: Array<ResourceColor>
```

SymbolSpan组件颜色。

默认值：不同渲染策略下默认值不同。

**Type:** Array&lt;ResourceColor&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorSymbolSpanStyleResult-fontColor: Array<ResourceColor>--><!--Device-RichEditorSymbolSpanStyleResult-fontColor: Array<ResourceColor>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize: number | string | Resource
```

SymbolSpan组件大小，默认单位为fp。

默认值：跟随主题。

**Type:** number \| string \| Resource

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorSymbolSpanStyleResult-fontSize: number | string | Resource--><!--Device-RichEditorSymbolSpanStyleResult-fontSize: number | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight: number | FontWeight | string
```

SymbolSpan组件粗细。

number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。

string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。

默认值：FontWeight.Normal。

**Type:** number \| FontWeight \| string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorSymbolSpanStyleResult-fontWeight: number | FontWeight | string--><!--Device-RichEditorSymbolSpanStyleResult-fontWeight: number | FontWeight | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## renderingStrategy

```TypeScript
renderingStrategy: SymbolRenderingStrategy
```

SymbolSpan组件渲染策略。

默认值：SymbolRenderingStrategy.SINGLE。

**Type:** [SymbolRenderingStrategy](arkts-arkui-symbolrenderingstrategy-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorSymbolSpanStyleResult-renderingStrategy: SymbolRenderingStrategy--><!--Device-RichEditorSymbolSpanStyleResult-renderingStrategy: SymbolRenderingStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

