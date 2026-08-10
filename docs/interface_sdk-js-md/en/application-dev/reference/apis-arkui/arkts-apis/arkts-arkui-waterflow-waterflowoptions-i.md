# WaterFlowOptions

提供瀑布流组件的参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface WaterFlowOptions--><!--Device-unnamed-export declare interface WaterFlowOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footer

```TypeScript
footer?: CustomBuilder
```

瀑布流组件的尾部组件。

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowOptions-footer?: CustomBuilder--><!--Device-WaterFlowOptions-footer?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footerContent

```TypeScript
footerContent?: ComponentContentBase
```

瀑布流组件的尾部组件。

**Type:** [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowOptions-footerContent?: ComponentContentBase--><!--Device-WaterFlowOptions-footerContent?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutMode

```TypeScript
layoutMode?: WaterFlowLayoutMode
```

瀑布流组件的布局模式。

**Type:** [WaterFlowLayoutMode](arkts-arkui-waterflow-waterflowlayoutmode-e.md)

**Default:** ALWAYS_TOP_DOWN

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowOptions-layoutMode?: WaterFlowLayoutMode--><!--Device-WaterFlowOptions-layoutMode?: WaterFlowLayoutMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller?: Scroller
```

可滚动组件的控制器，与可滚动组件绑定。&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;。&lt;br&gt;不允许和其他滚动类组件，如ArcList、List、Grid、Scroll绑定同一个滚动控制对象。&lt;/p&gt;

**Type:** [Scroller](../arkts-components/arkts-arkui-scroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowOptions-scroller?: Scroller--><!--Device-WaterFlowOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sections

```TypeScript
sections?: WaterFlowSections
```

瀑布流项分组，不同分组可以设置不同的列数。&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;。&lt;br&gt;1. 使用分组时，columnsTemplate和rowsTemplate属性将被忽略。&lt;br&gt;2. 使用分组时不支持单独设置footer，可以使用最后一个分组作为尾部组件。&lt;/p&gt;

**Type:** [WaterFlowSections](../arkts-components/arkts-arkui-waterflowsections-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowOptions-sections?: WaterFlowSections--><!--Device-WaterFlowOptions-sections?: WaterFlowSections-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

