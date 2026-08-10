# SurfaceRect

描述XComponent所持有的surface的矩形。

> **说明：**

> 如果未调用[setXComponentSurfaceRect](arkts-arkui-xcomponentcontroller-c.md#setxcomponentsurfacerect)接口，且未设置
> [border](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-border.md#border)和
> [padding](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#padding)，则**surfaceWidth**和**surfaceHeight**属性默认为**XComponent**的尺寸。
> 
> 请确保**surfaceWidth**和**surfaceHeight**的值不超过8192 px。超过此限制可能导致渲染问题。
> 
> 在沉浸式场景中，**SurfaceRect**的默认布局不包含安全区域。要实现沉浸式效果，必须使用
> [setXComponentSurfaceRect](arkts-arkui-xcomponentcontroller-c.md#setxcomponentsurfacerect)接口设置surface显示区域。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface SurfaceRect--><!--Device-unnamed-declare interface SurfaceRect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offsetX

```TypeScript
offsetX?: number
```

surface矩形相对于XComponent左上角的X坐标。

单位：px。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SurfaceRect-offsetX?: number--><!--Device-SurfaceRect-offsetX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offsetY

```TypeScript
offsetY?: number
```

surface矩形相对于XComponent左上角的Y坐标。

单位：px。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SurfaceRect-offsetY?: number--><!--Device-SurfaceRect-offsetY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## surfaceHeight

```TypeScript
surfaceHeight: number
```

surface矩形的高度。

单位：px。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SurfaceRect-surfaceHeight: number--><!--Device-SurfaceRect-surfaceHeight: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## surfaceWidth

```TypeScript
surfaceWidth: number
```

surface矩形的宽度。

单位：px。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SurfaceRect-surfaceWidth: number--><!--Device-SurfaceRect-surfaceWidth: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

