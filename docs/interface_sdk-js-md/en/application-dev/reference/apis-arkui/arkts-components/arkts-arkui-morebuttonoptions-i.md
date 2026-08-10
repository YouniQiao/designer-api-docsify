# MoreButtonOptions

更多图标的菜单选项。设置后，可自定义更多按钮的背景模糊样式、背景效果等。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-unnamed-declare interface MoreButtonOptions--><!--Device-unnamed-declare interface MoreButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

更多图标的菜单背景模糊样式，设置后，更多图标的菜单将应用指定的模糊样式；不设置时关闭背景模糊效果。

**Type:** [BlurStyle](arkts-arkui-blurstyle-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MoreButtonOptions-backgroundBlurStyle?: BlurStyle--><!--Device-MoreButtonOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

更多图标的菜单背景模糊选项。

**说明：**

只在设置了backgroundBlurStyle时生效。

不建议与backgroundEffect同时使用。

**Type:** [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MoreButtonOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-MoreButtonOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

设置更多图标的菜单背景属性包括：模糊半径，亮度，饱和度，颜色等。

**说明：**

不建议与backgroundBlurStyleOptions同时使用。

**Type:** [BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MoreButtonOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-MoreButtonOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

