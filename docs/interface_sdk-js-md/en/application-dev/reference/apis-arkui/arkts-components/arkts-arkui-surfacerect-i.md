# SurfaceRect

Describes the rectangle of the surface held by the **XComponent**. &gt; **NOTE：**&gt; The **surfaceWidth** and **surfaceHeight** attributes default to the size of the **XComponent** if the &gt; [setXComponentSurfaceRect](arkts-arkui-xcomponentcontroller-c.md#setxcomponentsurfacerect) API is not called and neither &gt; [border](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-border.md#border) nor &gt; padding is set. &gt; &gt; Make sure the values of **surfaceWidth** and **surfaceHeight** do not exceed 8192 px. Exceeding this limit may &gt; lead to rendering issues. &gt; &gt; In immersive scenarios, the default layout of **SurfaceRect** does not include the safe area. To achieve an &gt; immersive effect, you must set the surface display area using the &gt; [setXComponentSurfaceRect](arkts-arkui-xcomponentcontroller-c.md#setxcomponentsurfacerect) API.

**Since:** 12

<!--Device-unnamed-declare interface SurfaceRect--><!--Device-unnamed-declare interface SurfaceRect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## offsetX

```TypeScript
offsetX?: number
```

X-coordinate of the surface rectangle relative to the upper-left corner of the **XComponent**. Unit: px

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SurfaceRect-offsetX?: number--><!--Device-SurfaceRect-offsetX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offsetY

```TypeScript
offsetY?: number
```

Y-coordinate of the surface rectangle relative to the upper left corner of the **XComponent**. Unit: px

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SurfaceRect-offsetY?: number--><!--Device-SurfaceRect-offsetY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## surfaceHeight

```TypeScript
surfaceHeight: number
```

Height of the surface rectangle. Unit: px.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SurfaceRect-surfaceHeight: number--><!--Device-SurfaceRect-surfaceHeight: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## surfaceWidth

```TypeScript
surfaceWidth: number
```

Width of the surface rectangle. Unit: px.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SurfaceRect-surfaceWidth: number--><!--Device-SurfaceRect-surfaceWidth: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

