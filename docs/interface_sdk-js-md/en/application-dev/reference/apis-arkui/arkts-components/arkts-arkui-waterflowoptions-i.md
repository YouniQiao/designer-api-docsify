# WaterFlowOptions

瀑布流组件参数对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare interface WaterFlowOptions--><!--Device-unnamed-declare interface WaterFlowOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footer

```TypeScript
footer?: CustomBuilder
```

设置WaterFlow尾部组件，用于在瀑布流末尾显示自定义内容（如加载提示、底部标识等）。不设置时不显示尾部组件。

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WaterFlowOptions-footer?: CustomBuilder--><!--Device-WaterFlowOptions-footer?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footerContent

```TypeScript
footerContent?: ComponentContent
```

设置WaterFlow尾部组件。该参数的优先级高于参数footer，即同时设置footer和footerContent时，以footerContent设置的组件为准。

**Type:** [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-WaterFlowOptions-footerContent?: ComponentContent--><!--Device-WaterFlowOptions-footerContent?: ComponentContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutMode

```TypeScript
layoutMode?: WaterFlowLayoutMode
```

设置WaterFlow的布局模式，根据使用场景选择更切合的模式。

**Type:** [WaterFlowLayoutMode](../arkts-apis/arkts-arkui-waterflow-waterflowlayoutmode-e.md)

**Default:** ALWAYS_TOP_DOWN

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowOptions-layoutMode?: WaterFlowLayoutMode--><!--Device-WaterFlowOptions-layoutMode?: WaterFlowLayoutMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller?: Scroller
```

可滚动组件的控制器，与可滚动组件绑定。

&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;&lt;br&gt;不允许和其他滚动类组件，如：ArcList、List、Grid、Scroll和WaterFlow绑定同一个滚动控制对象。&lt;/p&gt;

**Type:** [Scroller](../arkts-apis/arkts-arkui-scroll-scroller-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WaterFlowOptions-scroller?: Scroller--><!--Device-WaterFlowOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sections

```TypeScript
sections?: WaterFlowSections
```

设置FlowItem分组，实现同一个瀑布流组件内部各分组使用不同列数混合布局。适用于需要在不同区域使用不同列数布局的场景。不设置时使用统一列数布局。

&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;&lt;br&gt;1. 使用分组混合布局时会忽略columnsTemplate和rowsTemplate属性。&lt;br&gt;2. 使用分组混合布局时不支持单独设置footer，可以使用最后一个分组作为尾部组件。&lt;/p&gt;

**Type:** [WaterFlowSections](arkts-arkui-waterflowsections-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowOptions-sections?: WaterFlowSections--><!--Device-WaterFlowOptions-sections?: WaterFlowSections-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

