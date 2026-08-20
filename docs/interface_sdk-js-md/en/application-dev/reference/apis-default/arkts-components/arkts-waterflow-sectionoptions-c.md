# SectionOptions

Describes the configuration of the water flow item section.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class SectionOptions--><!--Device-unnamed-export declare class SectionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnsGap

```TypeScript
columnsGap?: Dimension
```

Gap between columns. If this parameter is not set, the value of columnsGap for the water flow is used. If this parameter is set to an invalid value, 0 vp is used.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-columnsGap?: Dimension--><!--Device-SectionOptions-columnsGap?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## crossCount

```TypeScript
crossCount?: int
```

The columns of this section in vertical layout, or rows in horizontal layout. The value should be an integer.

**Type:** int

**Default:** 1 one column in vertical layout, or one row in horizontal layout

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-crossCount?: int--><!--Device-SectionOptions-crossCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemsCount

```TypeScript
itemsCount: int
```

The number of FlowItems in this section. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-itemsCount: int--><!--Device-SectionOptions-itemsCount: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## margin

```TypeScript
margin?: Margin | Dimension
```

Padding of the section. A value of the Length type specifies the margin for all the four sides.

**Type:** [Margin](../../apis-arkui/arkts-apis/arkts-arkui-margin-t.md) \| [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** {top: 0, right: 0, bottom: 0, left: 0}

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-margin?: Margin | Dimension--><!--Device-SectionOptions-margin?: Margin | Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onGetItemMainSizeByIndex

```TypeScript
onGetItemMainSizeByIndex?: GetItemMainSizeByIndex
```

Callback used to obtain the main axis size,in vp, of the water flow item at a specified index during the layout process of the WaterFlow component. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;. <br>1. When both &lt;em&gt;onGetItemMainSizeByIndex&lt;/em&gt; and the width or height attribute of the water flow item are used, the main axis size is determined by the return value of &lt;em&gt;onGetItemMainSizeByIndex&lt;/em&gt;, which will override the main axis length of water flow item. <br>2. Using &lt;em&gt;onGetItemMainSizeByIndex&lt;/em&gt; can improve the efficiency of jumping to a specific position or index in the &lt;em&gt;WaterFlow&lt;/em&gt; component. Avoid mixing the use of &lt;em&gt;onGetItemMainSizeByIndex&lt;/em&gt; with sections that do not have it set, as this can cause layout exceptions. <br>3. If &lt;em&gt;onGetItemMainSizeByIndex&lt;/em&gt; returns a negative number, the height of the water flow item is 0. &lt;/p&gt;

**Type:** [GetItemMainSizeByIndex](arkts-getitemmainsizebyindex-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-onGetItemMainSizeByIndex?: GetItemMainSizeByIndex--><!--Device-SectionOptions-onGetItemMainSizeByIndex?: GetItemMainSizeByIndex-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rowsGap

```TypeScript
rowsGap?: Dimension
```

Gap between rows. If this parameter is not set, the value of &lt;em&gt;rowsGap&lt;/em&gt; for the water flow is used. If this parameter is set to an invalid value, 0 vp is used.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-rowsGap?: Dimension--><!--Device-SectionOptions-rowsGap?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

