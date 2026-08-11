# WaterFlowOptions

Provides parameters of the &lt;em&gt;WaterFlow&lt;/em&gt; component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface WaterFlowOptions--><!--Device-unnamed-export declare interface WaterFlowOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footer

```TypeScript
footer?: CustomBuilder
```

Footer of the WaterFlow component.

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

Footer of the WaterFlow component.

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

Layout mode of the &lt;em&gt;WaterFlow&lt;/em&gt; component.

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

Controller of the scrollable component, bound to the scrollable component.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;.&lt;br&gt;The scroller cannot be bound to other scrollable components, such as ArcList, List, Grid, or Scroll.&lt;/p&gt;

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

Water flow item sections. Different sections can have different numbers of columns.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;.&lt;br&gt;1. When &lt;em&gt;sections&lt;/em&gt; is used, the &lt;em&gt;columnsTemplate&lt;/em&gt;and &lt;em&gt;rowsTemplate&lt;/em&gt; attributes are ignored.&lt;br&gt;2. When &lt;em&gt;sections&lt;/em&gt; is used, the footer cannot be set separately.The last section can function as the footer.&lt;/p&gt;

**Type:** [WaterFlowSections](../arkts-components/arkts-arkui-waterflowsections-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WaterFlowOptions-sections?: WaterFlowSections--><!--Device-WaterFlowOptions-sections?: WaterFlowSections-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

