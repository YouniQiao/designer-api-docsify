# NavigationToolbarOptions

工具栏选项。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface NavigationToolbarOptions--><!--Device-unnamed-declare interface NavigationToolbarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

工具栏背景模糊样式，设置后，工具栏将应用指定的模糊样式；不设置时关闭背景模糊效果。

**Type:** [BlurStyle](arkts-arkui-blurstyle-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationToolbarOptions-backgroundBlurStyle?: BlurStyle--><!--Device-NavigationToolbarOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

工具栏背景模糊选项。

**说明：**

只在设置了backgroundBlurStyle时生效。

不建议与backgroundEffect同时使用。

**Type:** [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NavigationToolbarOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-NavigationToolbarOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

工具栏背景颜色，设置后，工具栏背景将显示为指定颜色；不设置时为系统默认颜色。

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationToolbarOptions-backgroundColor?: ResourceColor--><!--Device-NavigationToolbarOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

设置工具栏背景属性包括：模糊半径，亮度，饱和度，颜色等。

**说明：**

不建议与backgroundBlurStyleOptions同时使用。

**Type:** [BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NavigationToolbarOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-NavigationToolbarOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## barStyle

```TypeScript
barStyle?: BarStyle
```

设置工具栏布局方式。

默认值：BarStyle.STANDARD

**Type:** [BarStyle](arkts-arkui-barstyle-e.md)

**Default:** BarStyle.STANDARD

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-NavigationToolbarOptions-barStyle?: BarStyle--><!--Device-NavigationToolbarOptions-barStyle?: BarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hideItemValue

```TypeScript
hideItemValue?: boolean
```

设置是否隐藏工具栏的文本，默认显示文本。

true：隐藏工具栏的文本；false：不隐藏工具栏的文本。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NavigationToolbarOptions-hideItemValue?: boolean--><!--Device-NavigationToolbarOptions-hideItemValue?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## moreButtonOptions

```TypeScript
moreButtonOptions?: MoreButtonOptions
```

工具栏更多图标的菜单选项。

**Type:** [MoreButtonOptions](../arkts-apis/arkts-arkui-navigation-morebuttonoptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NavigationToolbarOptions-moreButtonOptions?: MoreButtonOptions--><!--Device-NavigationToolbarOptions-moreButtonOptions?: MoreButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

