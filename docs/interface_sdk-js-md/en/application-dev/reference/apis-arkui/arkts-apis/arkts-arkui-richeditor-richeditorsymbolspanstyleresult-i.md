# RichEditorSymbolSpanStyleResult

后端返回的SymbolSpan样式信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RichEditorSymbolSpanStyleResult--><!--Device-unnamed-export declare interface RichEditorSymbolSpanStyleResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## effectStrategy

```TypeScript
effectStrategy: SymbolEffectStrategy
```

SymbolSpan组件动效策略。

默认值：SymbolEffectStrategy.NONE。

**Type:** [SymbolEffectStrategy](../arkts-components/arkts-arkui-symboleffectstrategy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorSymbolSpanStyleResult-effectStrategy: SymbolEffectStrategy--><!--Device-RichEditorSymbolSpanStyleResult-effectStrategy: SymbolEffectStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor: Array<ResourceColor>
```

SymbolSpan组件颜色。

默认值：不同渲染策略下默认值不同。

**Type:** Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorSymbolSpanStyleResult-fontColor: Array<ResourceColor>--><!--Device-RichEditorSymbolSpanStyleResult-fontColor: Array<ResourceColor>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize: double | string | Resource
```

SymbolSpan组件大小，默认单位为fp。

默认值：跟随主题。

**Type:** double \| string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorSymbolSpanStyleResult-fontSize: double | string | Resource--><!--Device-RichEditorSymbolSpanStyleResult-fontSize: double | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight: int | FontWeight | string
```

SymbolSpan组件粗细。

number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。

string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。

默认值：FontWeight.Normal。

**Type:** int \| FontWeight \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorSymbolSpanStyleResult-fontWeight: int | FontWeight | string--><!--Device-RichEditorSymbolSpanStyleResult-fontWeight: int | FontWeight | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## renderingStrategy

```TypeScript
renderingStrategy: SymbolRenderingStrategy
```

SymbolSpan组件渲染策略。

默认值：SymbolRenderingStrategy.SINGLE。

**Type:** [SymbolRenderingStrategy](../arkts-components/arkts-arkui-symbolrenderingstrategy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorSymbolSpanStyleResult-renderingStrategy: SymbolRenderingStrategy--><!--Device-RichEditorSymbolSpanStyleResult-renderingStrategy: SymbolRenderingStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

