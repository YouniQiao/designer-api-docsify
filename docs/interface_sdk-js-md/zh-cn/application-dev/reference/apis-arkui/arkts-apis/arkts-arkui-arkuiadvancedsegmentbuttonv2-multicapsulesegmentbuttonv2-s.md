# MultiCapsuleSegmentButtonV2

分段按钮组件用于创建页签型、单选或多选的胶囊型分段按钮，支持文本、图标、Symbol等多种选项类型及图文混合配置，可自定义字体、颜色、圆角等样式。页签型分段按钮适用于页签切换场景，单选胶囊型分段按钮适用于单选切换场景，多选胶囊型分段按 钮适用于多选筛选场景。

**起始版本：** 18

<!--Device-unnamed-export declare struct MultiCapsuleSegmentButtonV2--><!--Device-unnamed-export declare struct MultiCapsuleSegmentButtonV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { SegmentButtonV2ItemOptions, OnSelectedIndexChange, OnSelectedIndexesChange, SegmentButtonV2Item, SegmentButtonV2Items, TabSegmentButtonV2, CapsuleSegmentButtonV2, MultiCapsuleSegmentButtonV2 } from '@kit.ArkUI';
```

## build

```TypeScript
build(): void
```

Sets the build function of the segmented button.

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-build(): void--><!--Device-MultiCapsuleSegmentButtonV2-build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $selectedIndexes

```TypeScript
@Event
  $selectedIndexes: OnSelectedIndexesChange
```

配置分段按钮选中项变更时触发的回调函数。

默认值：undefined，未设置时不触发回调。

**类型：** [OnSelectedIndexesChange](arkts-arkui-onselectedindexeschange-t.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Event  $selectedIndexes: OnSelectedIndexesChange--><!--Device-MultiCapsuleSegmentButtonV2-@Event  $selectedIndexes: OnSelectedIndexesChange-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundBlurStyle

```TypeScript
@Param
  readonly itemBackgroundBlurStyle?: BlurStyle
```

配置分段按钮选项的模糊材质。

默认值：undefined

该成员只读，不支持更改。

**类型：** BlurStyle

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBackgroundBlurStyle?: BlurStyle--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBackgroundBlurStyle?: BlurStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundBlurStyleOptions

```TypeScript
@Param
  readonly itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

配置分段按钮选项的模糊材质配置参数。

默认值：undefined

该成员只读，不支持更改。

**类型：** BackgroundBlurStyleOptions

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundColor

```TypeScript
@Param
  readonly itemBackgroundColor?: ColorMetrics
```

配置分段按钮非选中的选项背板颜色。

默认值：`\$r('sys.color.segment_button_v2_multi_capsule_button_background')`

值为undefined时，按默认值处理。

该成员只读，不支持更改。

**类型：** ColorMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBackgroundColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBackgroundColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemBackgroundEffect

```TypeScript
@Param
  readonly itemBackgroundEffect?: BackgroundEffectOptions
```

配置分段按钮选项的背板效果。

默认值：undefined

该成员只读，不支持更改。

**类型：** BackgroundEffectOptions

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBackgroundEffect?: BackgroundEffectOptions--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBackgroundEffect?: BackgroundEffectOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemBorderRadius

```TypeScript
@Param
  readonly itemBorderRadius?: LengthMetrics
```

配置分段按钮选项的圆角大小。

取值范围：[0, +∞)

默认值：`\$r('sys.float.segment_button_v2_selected_corner_radius')`

超出取值范围按默认值处理。

该成员只读，不支持更改。

**类型：** LengthMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBorderRadius?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemBorderRadius?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemFontColor

```TypeScript
@Param
  readonly itemFontColor?: ColorMetrics
```

配置分段按钮非选中的选项字体颜色。

默认值：`\$r('sys.color.font_secondary')`

值为undefined时，按默认值处理。

**说明：**

items设置textModifier/fontColor属性值时，itemFontColor不生效。

该成员只读，不支持更改。

**类型：** ColorMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemFontColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemFontSize

```TypeScript
@Param
  readonly itemFontSize?: LengthMetrics
```

配置分段按钮非选中的选项字体大小。

取值范围：[0, +∞)

默认值：`14fp`

**说明：**

不支持设置百分比类型，异常值按默认值处理。

items设置textModifier/fontSize属性值时，itemFontSize不生效。

该成员只读，不支持更改。

**类型：** LengthMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemFontSize?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemFontSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemFontWeight

```TypeScript
@Param
  readonly itemFontWeight?: FontWeight
```

配置分段按钮非选中选项的字体字重。

默认值：FontWeight.Medium

超出取值范围按默认值处理。

**说明：**

items设置textModifier/fontWeight属性值时，itemFontWeight不生效。

该成员只读，不支持更改。

**类型：** FontWeight

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemFontWeight?: FontWeight--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemFontWeight?: FontWeight-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemIconFillColor

```TypeScript
@Param
  readonly itemIconFillColor?: ColorMetrics
```

配置分段按钮非选中的选项图标颜色。

默认值：`\$r('sys.color.font_secondary')`

值为undefined时，按默认值处理。

**说明：**

items设置iconModifier/fillColor属性值时，itemIconFillColor不生效。

backgroundSystemMaterial设置自动反色的系统材质时，该属性使用支持反色的特殊系统资源，颜色自动适配到材质背景色的反色。

该成员只读，不支持更改。

**类型：** ColorMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemIconFillColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemIconFillColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemIconSize

```TypeScript
@Param
  readonly itemIconSize?: SizeT<LengthMetrics>
```

配置分段按钮选项中Image类型的图标大小。

取值范围：[0, +∞)

默认值：`{ width: LengthMetrics.vp(24), height: LengthMetrics.vp(24) }`

超出取值范围按默认值处理。

**说明：**

items设置iconModifier/width、height属性值时，itemIconSize不生效。

该成员只读，不支持更改。

**类型：** SizeT&lt;LengthMetrics&gt;

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemIconSize?: SizeT<LengthMetrics>--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemIconSize?: SizeT<LengthMetrics>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemMaxFontScale

```TypeScript
@Param
  readonly itemMaxFontScale?: number | Resource
```

配置分段按钮选项文字大小的最大字体缩放倍数。

取值范围：[1, 2]

默认值：1

**说明：**

设置的值小于 1 时，按值为 1 处理，设置的值大于 2，按值为 2 处理，异常值默认不生效。

该成员只读，不支持更改。

**类型：** number \| Resource

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemMaxFontScale?: number | Resource--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemMaxFontScale?: number | Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemMinFontScale

```TypeScript
@Param
  readonly itemMinFontScale?: number | Resource
```

配置分段按钮选项文字大小的最小字体缩放倍数。

取值范围：[0, 1]

默认值：0

**说明：**

设置的最小字体缩放值小于 0 时，按值为 0 处理，设置的最小字体缩放值大于 1 时，按值为 1 处理，异常值默认不生效。

该成员只读，不支持更改。

**类型：** number \| Resource

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemMinFontScale?: number | Resource--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemMinFontScale?: number | Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemMinHeight

```TypeScript
@Param
  readonly itemMinHeight?: LengthMetrics
```

配置分段按钮选项最小高度。

取值范围：[0, +∞)

默认值：

只有纯文本或者纯图标选项时：`\$r('sys.float.segment_button_v2_singleline_selected_height')`；有图文混合的选项时： `\$r('sys.float.segment_button_v2_doubleline_selected_height')`

超出取值范围按默认值处理。

该成员只读，不支持更改。

**类型：** LengthMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemMinHeight?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemMinHeight?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemPadding

```TypeScript
@Param
  readonly itemPadding?: LocalizedPadding
```

配置分段按钮选项内边距。

默认值： `{ top: LengthMetrics.resource(\$r('sys.float.padding_level2')), bottom: LengthMetrics.resource(\$r('sys.float.padding_level2')), start: LengthMetrics.resource(\$r('sys.float.padding_level4')), end: LengthMetrics.resource(\$r('sys.float.padding_level4')) }`

值为undefined时，按默认值处理。

该成员只读，不支持更改。

**类型：** LocalizedPadding

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemPadding?: LocalizedPadding--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemPadding?: LocalizedPadding-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedBackgroundColor

```TypeScript
@Param
  readonly itemSelectedBackgroundColor?: ColorMetrics
```

配置分段按钮选中的选项背景颜色。

默认值：`\$r('sys.color.segment_button_v2_tab_selected_item_background')`

值为undefined时，按默认值处理。

该成员只读，不支持更改。

**类型：** ColorMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedBackgroundColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedBackgroundColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontColor

```TypeScript
@Param
  readonly itemSelectedFontColor?: ColorMetrics
```

配置分段按钮非选中选项的字体颜色。

默认值：`\$r('sys.color.font_secondary')`

值为undefined时，按默认值处理。

**说明：**

items设置textModifier/fontColor属性值时，itemFontColor不生效。

backgroundSystemMaterial设置自动反色的系统材质时，该属性使用支持反色的特殊系统资源，颜色自动适配到材质背景色的反色。

该成员只读，不支持更改。

**类型：** ColorMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedFontColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontSize

```TypeScript
@Param
  readonly itemSelectedFontSize?: LengthMetrics
```

配置分段按钮选中的选项字体大小。

取值范围：[0, +∞)

默认值：`14fp`

**说明：**

不支持设置百分比类型，异常值按默认值处理。

items设置textModifier/fontSize属性值时，itemSelectedFontSize不生效。

该成员只读，不支持更改。

**类型：** LengthMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedFontSize?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedFontSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontWeight

```TypeScript
@Param
  readonly itemSelectedFontWeight?: FontWeight
```

配置分段按钮选中项的字体字重。

默认值：FontWeight.Medium

超出取值范围按默认值处理。

**说明：**

items设置textModifier/fontWeight属性值时，itemSelectedFontWeight不生效。

该成员只读，不支持更改。

**类型：** FontWeight

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedFontWeight?: FontWeight--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedFontWeight?: FontWeight-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedIconFillColor

```TypeScript
@Param
  readonly itemSelectedIconFillColor?: ColorMetrics
```

配置分段按钮选中的选项图标颜色。

默认值：`\$r('sys.color.font_primary')`

值为undefined时，按默认值处理。

**说明：**

items设置iconModifier/fillColor属性值时，itemSelectedIconFillColor不生效。

backgroundSystemMaterial设置自动反色的系统材质时，该属性使用支持反色的特殊系统资源，颜色自动适配到材质背景色的反色。

该成员只读，不支持更改。

**类型：** ColorMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedIconFillColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedIconFillColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedSymbolFontColor

```TypeScript
@Param
  readonly itemSelectedSymbolFontColor?: ColorMetrics
```

配置分段按钮选中选项的HM Symbol类型图标颜色。

默认值：`\$r('sys.color.font_primary')`

值为undefined时，按默认值处理。

**说明：**

items设置symbolModifier/fontColor属性值时，itemSelectedSymbolFontColor不生效。

backgroundSystemMaterial设置自动反色的系统材质时，该属性使用支持反色的特殊系统资源，颜色自动适配到材质背景色的反色。

该成员只读，不支持更改。

**类型：** ColorMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedSymbolFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSelectedSymbolFontColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSpace

```TypeScript
@Param
  readonly itemSpace?: LengthMetrics
```

配置分段按钮选项之间的间隔。

取值范围：[0, +∞)

默认值：`LengthMetrics.vp(1)`

**说明：**

不支持设置百分比类型，异常值按默认值处理。

该成员只读，不支持更改。

**类型：** LengthMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSpace?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSpace?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontColor

```TypeScript
@Param
  readonly itemSymbolFontColor?: ColorMetrics
```

配置分段按钮非选中选项HM Symbol类型图标的颜色。

默认值：`\$r('sys.color.font_secondary')`

值为undefined时，按默认值处理。

**说明：**

items设置symbolModifier/fontColor属性值时，itemSymbolFontColor不生效。

backgroundSystemMaterial设置自动反色的系统材质时，该属性使用支持反色的特殊系统资源，颜色自动适配到材质背景色的反色。

该成员只读，不支持更改。

**类型：** ColorMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSymbolFontColor?: ColorMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSymbolFontColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontSize

```TypeScript
@Param
  readonly itemSymbolFontSize?: LengthMetrics
```

配置分段按钮选项中HM Symbol类型图标大小。

取值范围：[0, +∞)

默认值：`20fp`

**说明：**

不支持设置百分比类型，异常值按默认值处理。

items设置symbolModifier/fontSize属性值时，itemSymbolFontSize不生效。

该成员只读，不支持更改。

**类型：** LengthMetrics

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSymbolFontSize?: LengthMetrics--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly itemSymbolFontSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
  @Param
  readonly items: SegmentButtonV2Items
```

配置分段按钮的选项集合信息。

值为undefined时，不显示选项信息。

该成员只读，不支持更改。

**类型：** [SegmentButtonV2Items](arkts-arkui-arkuiadvancedsegmentbuttonv2-segmentbuttonv2items-c.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Require  @Param  readonly items: SegmentButtonV2Items--><!--Device-MultiCapsuleSegmentButtonV2-@Require  @Param  readonly items: SegmentButtonV2Items-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## languageDirection

```TypeScript
@Param
  readonly languageDirection?: Direction
```

配置分段按钮的布局方向。

默认值：Direction.Auto

超出取值范围按默认值处理。

该成员只读，不支持更改。

**类型：** Direction

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly languageDirection?: Direction--><!--Device-MultiCapsuleSegmentButtonV2-@Param  readonly languageDirection?: Direction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onItemClicked

```TypeScript
@Event
  onItemClicked?: Callback<number>
```

配置分段按钮选项被单击时触发的回调函数。回调参数为number类型，表示被单击选项的下标，第一项编号为0，之后按顺序递增。

默认值：undefined，未设置时不触发回调。

**类型：** Callback&lt;number&gt;

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Event  onItemClicked?: Callback<number>--><!--Device-MultiCapsuleSegmentButtonV2-@Event  onItemClicked?: Callback<number>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@Require
  @Param
  readonly selectedIndexes: number[]
```

配置分段按钮被选中的选项下标集合，第一项的编号为0，之后顺序增加。

值为undefined时，不选中任何选项。

**说明：**

仅支持有效的按钮编号（第一个按钮编号为0，之后按顺序累加，取值范围：[0, items长度-1]），如没有选中项可传入空数组`[]`。传入无效编号（小于0或大于items长度-1）时，该编号不选中对应选项。

该成员只读，不支持更改。

**类型：** number[]

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MultiCapsuleSegmentButtonV2-@Require  @Param  readonly selectedIndexes: number[]--><!--Device-MultiCapsuleSegmentButtonV2-@Require  @Param  readonly selectedIndexes: number[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

