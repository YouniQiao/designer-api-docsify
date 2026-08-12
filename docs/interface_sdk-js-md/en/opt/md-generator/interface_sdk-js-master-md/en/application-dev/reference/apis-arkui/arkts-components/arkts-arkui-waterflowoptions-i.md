# WaterFlowOptions

Provides parameters of the **WaterFlow** component.

**Since:** 9

<!--Device-unnamed-declare interface WaterFlowOptions--><!--Device-unnamed-declare interface WaterFlowOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footer

```TypeScript
footer?: CustomBuilder
```

Footer component of the **WaterFlow** component, which is used to display custom content (such as loading prompts and bottom icons) at the end of the waterfall. If this parameter is not set, no footer component is displayed.

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md)

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WaterFlowOptions-footer?: CustomBuilder--><!--Device-WaterFlowOptions-footer?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footerContent

```TypeScript
footerContent?: ComponentContent
```

Footer of the **WaterFlow** component. This parameter has a higher priority than **footer**. If both  
**footer** and **footerContent** are set, the component set by **footerContent** will be used.

**Type:** ComponentContent

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-WaterFlowOptions-footerContent?: ComponentContent--><!--Device-WaterFlowOptions-footerContent?: ComponentContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutMode

```TypeScript
layoutMode?: WaterFlowLayoutMode
```

Layout mode of the &lt;em&gt;WaterFlow&lt;/em&gt; component.

**Type:** [WaterFlowLayoutMode](arkts-arkui-waterflowlayoutmode-e.md)

**Default:** ALWAYS_TOP_DOWN

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowOptions-layoutMode?: WaterFlowLayoutMode--><!--Device-WaterFlowOptions-layoutMode?: WaterFlowLayoutMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller?: Scroller
```

Controller of the scrollable component, bound to the scrollable component.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;The scroller cannot be bound to other scrollable components, such as ArcList, List, Grid, Scroll, or WaterFlow.&lt;/p&gt;

**Type:** [Scroller](arkts-arkui-scroller-c.md)

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WaterFlowOptions-scroller?: Scroller--><!--Device-WaterFlowOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sections

```TypeScript
sections?: WaterFlowSections
```

Water flow item sections, used to implement mixed layouts with different column counts for each section within the same **WaterFlow** component. This is applicable to scenarios where different numbers of columns are required in different areas. If this parameter is not set, the layout with the same number of columns is used.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;1. When &lt;em&gt;sections&lt;/em&gt; is used, the &lt;em&gt;columnsTemplate&lt;/em&gt; and &lt;em&gt;rowsTemplate&lt;/em&gt; attributes are ignored.&lt;br&gt;2. When &lt;em&gt;sections&lt;/em&gt; is used, the footer cannot be set separately.The last section can function as the footer.&lt;/p&gt;

**Type:** [WaterFlowSections](arkts-arkui-waterflowsections-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WaterFlowOptions-sections?: WaterFlowSections--><!--Device-WaterFlowOptions-sections?: WaterFlowSections-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
