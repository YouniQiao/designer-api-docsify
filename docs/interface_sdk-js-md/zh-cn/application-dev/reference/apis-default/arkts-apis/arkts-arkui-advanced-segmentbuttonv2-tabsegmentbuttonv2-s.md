# TabSegmentButtonV2

定义页签型分段按钮。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentV2

<!--Device-unnamed-export declare struct TabSegmentButtonV2--><!--Device-unnamed-export declare struct TabSegmentButtonV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
build(): void
```

build函数用于构造TabSegmentButtonV2高级组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Builder  build(): void--><!--Device-TabSegmentButtonV2-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $selectedIndex

```TypeScript
readonly $selectedIndex?: OnSelectedIndexChange
```

配置分段按钮选中项变更时触发的回调函数。

**类型：** [OnSelectedIndexChange](arkts-onselectedindexchange-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Event

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Event  readonly $selectedIndex?: OnSelectedIndexChange--><!--Device-TabSegmentButtonV2-@Event  readonly $selectedIndex?: OnSelectedIndexChange-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundBlurStyle

```TypeScript
readonly buttonBackgroundBlurStyle?: BlurStyle
```

配置分段按钮背板模糊材质。 默认值：undefined 该成员只读，不支持更改。

**类型：** BlurStyle

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly buttonBackgroundBlurStyle?: BlurStyle--><!--Device-TabSegmentButtonV2-@Param  readonly buttonBackgroundBlurStyle?: BlurStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundBlurStyleOptions

```TypeScript
readonly buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

配置分段按钮背板模糊材质配置参数。 默认值：undefined 该成员只读，不支持更改。

**类型：** BackgroundBlurStyleOptions

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-TabSegmentButtonV2-@Param  readonly buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundColor

```TypeScript
readonly buttonBackgroundColor?: ColorMetrics
```

配置分段按钮背板颜色。 默认值：`ColorMetrics。

**类型：** ColorMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly buttonBackgroundColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly buttonBackgroundColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buttonBackgroundEffect

```TypeScript
readonly buttonBackgroundEffect?: BackgroundEffectOptions
```

配置分段按钮背板模糊配置参数。 默认值：undefined 该成员只读，不支持更改。

**类型：** BackgroundEffectOptions

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly buttonBackgroundEffect?: BackgroundEffectOptions--><!--Device-TabSegmentButtonV2-@Param  readonly buttonBackgroundEffect?: BackgroundEffectOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buttonBorderRadius

```TypeScript
readonly buttonBorderRadius?: LengthMetrics
```

配置分段按钮背板的圆角大小。 默认值：`\$r('sys。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly buttonBorderRadius?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly buttonBorderRadius?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buttonMinHeight

```TypeScript
readonly buttonMinHeight?: LengthMetrics
```

配置分段按钮最小高度。 默认值：只有纯文本或者纯图标选项时：`\$r('sys。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly buttonMinHeight?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly buttonMinHeight?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buttonPadding

```TypeScript
readonly buttonPadding?: LengthMetrics
```

配置分段按钮内边距。 默认值：`\$r('sys。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly buttonPadding?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly buttonPadding?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## enableStateAnimation

```TypeScript
readonly enableStateAnimation?: boolean
```

设置当通过变量修改selectedIndex值时，是否开启分段按钮的属性动画。 true表示开启分段按钮的属性动画；未配置该属性或值为false时表示不开启分段按钮的属性动画，使用原有动画。 默认值：false。

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly enableStateAnimation?: boolean--><!--Device-TabSegmentButtonV2-@Param  readonly enableStateAnimation?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemBorderRadius

```TypeScript
readonly itemBorderRadius?: LengthMetrics
```

配置分段按钮选项的圆角大小。 默认值：`\$r('sys。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemBorderRadius?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemBorderRadius?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemFontColor

```TypeScript
readonly itemFontColor?: ColorMetrics
```

配置分段按钮选中项的字体颜色。 默认值：`ColorMetrics。

**类型：** ColorMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemFontColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemFontSize

```TypeScript
readonly itemFontSize?: LengthMetrics
```

配置分段按钮非选中选项的字体大小。 默认值：`14fp` **说明：** 不支持设置百分比类型，异常值按默认值处理。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemFontSize?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemFontSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemFontWeight

```TypeScript
readonly itemFontWeight?: FontWeight
```

配置分段按钮非选中选项的字体字重。 默认值：FontWeight。

**类型：** FontWeight

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemFontWeight?: FontWeight--><!--Device-TabSegmentButtonV2-@Param  readonly itemFontWeight?: FontWeight-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemIconFillColor

```TypeScript
readonly itemIconFillColor?: ColorMetrics
```

配置分段按钮非选中的选项图标颜色。 默认值：`ColorMetrics。

**类型：** ColorMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemIconFillColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemIconFillColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemIconSize

```TypeScript
readonly itemIconSize?: SizeT<LengthMetrics>
```

配置分段按钮选项中Image类型的图标大小。 默认值：`{ width: LengthMetrics。

**类型：** SizeT&lt;LengthMetrics&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemIconSize?: SizeT<LengthMetrics>--><!--Device-TabSegmentButtonV2-@Param  readonly itemIconSize?: SizeT<LengthMetrics>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemMaxFontScale

```TypeScript
readonly itemMaxFontScale?: double | Resource
```

配置分段按钮选项文字大小的最大放大倍数。 默认值：1 **说明：** 设置的值小于1时，按值为1处理，设置的值大于2，按值为2处理，异常值默认不生效。

**类型：** double \| Resource

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemMaxFontScale?: double | Resource--><!--Device-TabSegmentButtonV2-@Param  readonly itemMaxFontScale?: double | Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemMinFontScale

```TypeScript
readonly itemMinFontScale?: double | Resource
```

配置分段按钮选项文字大小的最小字体缩放倍数。 默认值：0 **说明：** 设置的值小于0时，按值为0处理，设置的值大于1，按值为1处理，异常值默认不生效。

**类型：** double \| Resource

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemMinFontScale?: double | Resource--><!--Device-TabSegmentButtonV2-@Param  readonly itemMinFontScale?: double | Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemMinHeight

```TypeScript
readonly itemMinHeight?: LengthMetrics
```

配置分段按钮选项最小高度。 默认值：只有纯文本或者纯图标选项时：`\$r('sys。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemMinHeight?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemMinHeight?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemPadding

```TypeScript
readonly itemPadding?: LocalizedPadding
```

配置分段按钮选项内边距。 默认值：`{ top: LengthMetrics。

**类型：** LocalizedPadding

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemPadding?: LocalizedPadding--><!--Device-TabSegmentButtonV2-@Param  readonly itemPadding?: LocalizedPadding-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
readonly items: SegmentButtonV2Items
```

配置分段按钮的选项集合信息。不支持设置undefined该成员只读，不支持更改。

**类型：** [SegmentButtonV2Items](arkts-arkui-advanced-segmentbuttonv2-segmentbuttonv2items-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Require、@Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Require  @Param  readonly items: SegmentButtonV2Items--><!--Device-TabSegmentButtonV2-@Require  @Param  readonly items: SegmentButtonV2Items-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedBackgroundColor

```TypeScript
readonly itemSelectedBackgroundColor?: ColorMetrics
```

配置分段按钮选中的选项背景颜色。 默认值：`ColorMetrics。

**类型：** ColorMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedBackgroundColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedBackgroundColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontColor

```TypeScript
readonly itemSelectedFontColor?: ColorMetrics
```

配置分段按钮选中项的字体颜色。 默认值：`ColorMetrics。

**类型：** ColorMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedFontColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontSize

```TypeScript
readonly itemSelectedFontSize?: LengthMetrics
```

配置分段按钮选中项的字体大小。 默认值：`14fp` **说明：** 不支持设置百分比类型，异常值按默认值处理。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedFontSize?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedFontSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedFontWeight

```TypeScript
readonly itemSelectedFontWeight?: FontWeight
```

配置分段按钮选中项的字体字重。 默认值：FontWeight。

**类型：** FontWeight

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedFontWeight?: FontWeight--><!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedFontWeight?: FontWeight-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedIconFillColor

```TypeScript
readonly itemSelectedIconFillColor?: ColorMetrics
```

配置分段按钮选中的选项图标颜色。 默认值：`ColorMetrics。

**类型：** ColorMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedIconFillColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedIconFillColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSelectedSymbolFontColor

```TypeScript
readonly itemSelectedSymbolFontColor?: ColorMetrics
```

配置分段按钮选中选项的HM Symbol类型图标颜色。 默认值：`ColorMetrics。

**类型：** ColorMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedSymbolFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemSelectedSymbolFontColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemShadow

```TypeScript
readonly itemShadow?: ShadowOptions | ShadowStyle
```

配置分段按钮选项阴影。 默认值：ShadowStyle。

**类型：** ShadowOptions \| ShadowStyle

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemShadow?: ShadowOptions | ShadowStyle--><!--Device-TabSegmentButtonV2-@Param  readonly itemShadow?: ShadowOptions | ShadowStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSpace

```TypeScript
readonly itemSpace?: LengthMetrics
```

配置分段按钮选项之间的间隔。 默认值：`LengthMetrics。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemSpace?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemSpace?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontColor

```TypeScript
readonly itemSymbolFontColor?: ColorMetrics
```

配置分段按钮非选中选项HM Symbol类型图标的颜色。 默认值：`ColorMetrics。

**类型：** ColorMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemSymbolFontColor?: ColorMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemSymbolFontColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSymbolFontSize

```TypeScript
readonly itemSymbolFontSize?: LengthMetrics
```

配置分段按钮选项中HM Symbol类型图标大小。 默认值：`20fp` **说明：** 不支持设置百分比类型，异常值按默认值处理。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly itemSymbolFontSize?: LengthMetrics--><!--Device-TabSegmentButtonV2-@Param  readonly itemSymbolFontSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## languageDirection

```TypeScript
readonly languageDirection?: Direction
```

配置分段按钮的布局方向。 默认值：Direction。

**类型：** Direction

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Param  readonly languageDirection?: Direction--><!--Device-TabSegmentButtonV2-@Param  readonly languageDirection?: Direction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onItemClicked

```TypeScript
readonly onItemClicked?: Callback<int>
```

配置分段按钮选项被单击时触发的回调函数。

**类型：** Callback&lt;int&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Event

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Event  readonly onItemClicked?: Callback<int>--><!--Device-TabSegmentButtonV2-@Event  readonly onItemClicked?: Callback<int>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
readonly selectedIndex: int
```

配置分段按钮被选中的选项下标，第一项的编号为0，之后顺序增加。不支持设置undefined 该成员只读，不支持更改。 取值限定为整数。

**类型：** int

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Require、@Param

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabSegmentButtonV2-@Require  @Param  readonly selectedIndex: int--><!--Device-TabSegmentButtonV2-@Require  @Param  readonly selectedIndex: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

