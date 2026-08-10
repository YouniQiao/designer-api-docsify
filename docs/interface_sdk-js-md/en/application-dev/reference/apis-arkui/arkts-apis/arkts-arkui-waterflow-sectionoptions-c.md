# SectionOptions

描述瀑布流项分组的配置信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class SectionOptions--><!--Device-unnamed-export declare class SectionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onGetItemMainSizeByIndex

```TypeScript
onGetItemMainSizeByIndex?: GetItemMainSizeByIndex
```

瀑布流组件布局过程中获取指定index的FlowItem的主轴大小的回调，纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;。&lt;br&gt;1. 同时使用onGetItemMainSizeByIndex和FlowItem的宽高属性时，主轴大小以onGetItemMainSizeByIndex返回结果为准，onGetItemMainSizeByIndex会覆盖FlowItem的主轴长度。&lt;br&gt;2. 使用onGetItemMainSizeByIndex可以提高瀑布流跳转到指定位置或index时的效率，避免混用设置onGetItemMainSizeByIndex和未设置的分组，会导致布局异常。&lt;br&gt;3. onGetItemMainSizeByIndex返回负数时FlowItem高度为0。&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-onGetItemMainSizeByIndex?: GetItemMainSizeByIndex--><!--Device-SectionOptions-onGetItemMainSizeByIndex?: GetItemMainSizeByIndex-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnsGap

```TypeScript
columnsGap?: Dimension
```

该分组的列间距，不设置该参数时默认使用瀑布流的columnsGap，设置非法值时使用0vp。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-columnsGap?: Dimension--><!--Device-SectionOptions-columnsGap?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## crossCount

```TypeScript
crossCount?: int
```

该分组纵向布局时的列数，或横向布局时的行数。取值限定为整数。&lt;br&gt; 小于1的按默认值处理。

**Type:** int

**Default:** 1 one column in vertical layout, or one row in horizontal layout

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-crossCount?: int--><!--Device-SectionOptions-crossCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemsCount

```TypeScript
itemsCount: int
```

该分组中FlowItem的数量。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-itemsCount: int--><!--Device-SectionOptions-itemsCount: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## margin

```TypeScript
margin?: Margin | Dimension
```

该分组的外边距，参数为Length类型时，四个方向外边距同时生效。

**Type:** [Margin](arkts-arkui-margin-t.md) \| Dimension

**Default:** {top: 0, right: 0, bottom: 0, left: 0}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-margin?: Margin | Dimension--><!--Device-SectionOptions-margin?: Margin | Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rowsGap

```TypeScript
rowsGap?: Dimension
```

该分组的行间距，不设置该参数时默认使用瀑布流的rowsGap，设置非法值时使用0vp。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SectionOptions-rowsGap?: Dimension--><!--Device-SectionOptions-rowsGap?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

