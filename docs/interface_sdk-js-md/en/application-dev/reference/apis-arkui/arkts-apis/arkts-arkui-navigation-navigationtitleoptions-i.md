# NavigationTitleOptions

标题栏选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavigationTitleOptions--><!--Device-unnamed-export declare interface NavigationTitleOptions-End-->

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

<!--Device-NavigationTitleOptions-backgroundBlurStyle?: BlurStyle--><!--Device-NavigationTitleOptions-backgroundBlurStyle?: BlurStyle-End-->

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

<!--Device-NavigationTitleOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-NavigationTitleOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

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

<!--Device-NavigationTitleOptions-backgroundColor?: ResourceColor--><!--Device-NavigationTitleOptions-backgroundColor?: ResourceColor-End-->

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

<!--Device-NavigationTitleOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-NavigationTitleOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## barStyle

```TypeScript
barStyle?: BarStyle
```

设置标题栏布局方式。默认值： BarStyle.STANDARD。

**Type:** [BarStyle](../arkts-components/arkts-arkui-barstyle-e.md)

**Default:** BarStyle.STANDARD

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-barStyle?: BarStyle--><!--Device-NavigationTitleOptions-barStyle?: BarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

是否响应悬停态。使用规则：1. 需满足Navigation为全屏大小；2. 标题栏显示模式为[Free](../arkts-components/arkts-arkui-navigationtitlemode-e.md/arkts-arkui-navigationtitlemode-e.md)时或者标题栏布局方式为[STANDARD](../arkts-components/arkts-arkui-barstyle-e.md/arkts-arkui-barstyle-e.md)时，此接口设置无效。true：响应悬停态；false：不响应悬停态。默认值： false。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-enableHoverMode?: boolean--><!--Device-NavigationTitleOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mainTitleModifier

```TypeScript
mainTitleModifier?: TextModifier
```

主标题属性修改器。1. 通过Modifier设置的属性会覆盖系统默认的属性（如果Modifier设置了fontSize，maxFontSize，minFontSize任一属性，则系统设置的大小相关属性不生效，以开发者的设置为准）；2. 不设该属性或者设置了异常值，则恢复系统默认设置；3. [Free](../arkts-components/arkts-arkui-navigationtitlemode-e.md/arkts-arkui-navigationtitlemode-e.md)模式下设置字体大小时，原有滑动改变标题大小的效果失效。

**Type:** TextModifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-mainTitleModifier?: TextModifier--><!--Device-NavigationTitleOptions-mainTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paddingEnd

```TypeScript
paddingEnd?: LengthMetrics
```

标题栏结束端内间距。仅支持以下任一场景：1. 使用非自定义菜单，即[菜单value](NavigationAttribute.menus)为Array&lt;NavigationMenuItem&gt;；2. 没有右上角菜单，且使用非自定义标题，即[标题value](NavigationAttribute.title)类型为ResourceStr或NavigationCommonTitle。默认值： LengthMetrics.resource(`\$r('sys.float.margin_right')`)。

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.resource($r('sys.float.margin_right'))

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-paddingEnd?: LengthMetrics--><!--Device-NavigationTitleOptions-paddingEnd?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paddingStart

```TypeScript
paddingStart?: LengthMetrics
```

标题栏起始端内间距。仅支持以下任一场景：1. 显示返回图标，即[hideBackButton](NavigationAttribute.hideBackButton)为false；2. 使用非自定义标题，即[标题value](NavigationAttribute.title)类型为ResourceStr或NavigationCommonTitle。默认值： LengthMetrics.resource(\$r('sys.float.margin_left'))。

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.resource($r('sys.float.margin_left'))

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-paddingStart?: LengthMetrics--><!--Device-NavigationTitleOptions-paddingStart?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scrollEffectOptions

```TypeScript
scrollEffectOptions?: ScrollEffectOptions
```

标题栏滑动模糊效果选项。

**Type:** [ScrollEffectOptions](../arkts-components/arkts-arkui-scrolleffectoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-scrollEffectOptions?: ScrollEffectOptions--><!--Device-NavigationTitleOptions-scrollEffectOptions?: ScrollEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subTitleModifier

```TypeScript
subTitleModifier?: TextModifier
```

子标题属性修改器。1. 通过Modifier设置的属性会覆盖系统默认的属性（如果Modifier设置了fontSize，maxFontSize，minFontSize任一属性，则系统设置的大小相关属性不生效，以开发者的设置为准）；2. 不设该属性或者设置了异常值，则恢复系统默认设置。

**Type:** TextModifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-subTitleModifier?: TextModifier--><!--Device-NavigationTitleOptions-subTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

