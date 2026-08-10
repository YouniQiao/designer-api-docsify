# NavigationToolbarOptions

工具栏选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavigationToolbarOptions--><!--Device-unnamed-export declare interface NavigationToolbarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

标题栏背景模糊样式，不设置时关闭背景模糊效果。

**Type:** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationToolbarOptions-backgroundBlurStyle?: BlurStyle--><!--Device-NavigationToolbarOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

标题栏背景模糊选项。  
**说明：**只在设置了backgroundBlurStyle时生效。不建议与backgroundEffect同时使用。

**Type:** [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationToolbarOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-NavigationToolbarOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

标题栏背景颜色，不设置时为系统默认颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationToolbarOptions-backgroundColor?: ResourceColor--><!--Device-NavigationToolbarOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

设置标题栏背景属性包括：模糊半径，亮度，饱和度，颜色等。  
**说明：**不建议与backgroundBlurStyleOptions同时使用。

**Type:** [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationToolbarOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-NavigationToolbarOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## barStyle

```TypeScript
barStyle?: BarStyle
```

设置工具栏布局方式。默认值： BarStyle.STANDARD。

**Type:** [BarStyle](../arkts-components/arkts-arkui-barstyle-e.md)

**Default:** BarStyle.STANDARD

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationToolbarOptions-barStyle?: BarStyle--><!--Device-NavigationToolbarOptions-barStyle?: BarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hideItemValue

```TypeScript
hideItemValue?: boolean
```

设置是否隐藏工具栏的文本，默认显示文本。true：隐藏工具栏的文本；false：不隐藏工具栏的文本。默认值： false。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationToolbarOptions-hideItemValue?: boolean--><!--Device-NavigationToolbarOptions-hideItemValue?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## moreButtonOptions

```TypeScript
moreButtonOptions?: MoreButtonOptions
```

工具栏更多图标的菜单选项。

**Type:** [MoreButtonOptions](arkts-arkui-navigation-morebuttonoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationToolbarOptions-moreButtonOptions?: MoreButtonOptions--><!--Device-NavigationToolbarOptions-moreButtonOptions?: MoreButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

