# DrawableTabBarIndicator

使用图片资源作为下划线的对象。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-unnamed-declare interface DrawableTabBarIndicator--><!--Device-unnamed-declare interface DrawableTabBarIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: Length
```

下划线的圆角半径（不支持百分比设置）。

默认值：0.0

单位：vp

取值范围：[0, +∞)。异常值时取默认值。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Default:** 0

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-DrawableTabBarIndicator-borderRadius?: Length--><!--Device-DrawableTabBarIndicator-borderRadius?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## drawable

```TypeScript
drawable?: DrawableDescriptor
```

下划线的图源。支持[DrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md/arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md)、  
[PixelMapDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-pixelmapdrawabledescriptor-c.md/arkts-arkui-arkui-drawabledescriptor-pixelmapdrawabledescriptor-c.md)、  
[LayeredDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md/arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md)和  
[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)类型。当传入无效图源时将显示默认的实线型下划线。

**Type:** [DrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-DrawableTabBarIndicator-drawable?: DrawableDescriptor--><!--Device-DrawableTabBarIndicator-drawable?: DrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Length
```

下划线的高度（不支持百分比设置）。

默认值：2.0

单位：vp

取值范围：[0, +∞)。异常值时取默认值。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Default:** 2vp

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-DrawableTabBarIndicator-height?: Length--><!--Device-DrawableTabBarIndicator-height?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marginTop

```TypeScript
marginTop?: Length
```

下划线与文字的间距（不支持百分比设置）。

默认值：8.0

单位：vp

取值范围：[0, +∞)。异常值时取默认值。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Default:** 8vp

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-DrawableTabBarIndicator-marginTop?: Length--><!--Device-DrawableTabBarIndicator-marginTop?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Length
```

下划线的宽度（不支持百分比设置）。

默认值：0.0

单位：vp

取值范围：[0, +∞)。异常值时取默认值。

宽度设置为0时，按页签文本宽度显示。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Default:** 0

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-DrawableTabBarIndicator-width?: Length--><!--Device-DrawableTabBarIndicator-width?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

