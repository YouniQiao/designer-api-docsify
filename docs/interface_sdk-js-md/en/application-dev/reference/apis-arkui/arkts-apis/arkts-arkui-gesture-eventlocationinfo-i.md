# EventLocationInfo

用于点击手势获取点击位置坐标。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface EventLocationInfo--><!--Device-unnamed-export declare interface EventLocationInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCurrentLocalPosition

```TypeScript
default getCurrentLocalPosition(): Coordinate2D
```

获取点击位置相对于当前组件实时位置的左上角坐标。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventLocationInfo-default getCurrentLocalPosition(): Coordinate2D--><!--Device-EventLocationInfo-default getCurrentLocalPosition(): Coordinate2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Coordinate2D](arkts-arkui-coordinate2d-i.md) | 获取点击位置相对于当前组件实时位置的左上角坐标。 |

## displayX

```TypeScript
displayX: double
```

相对于屏幕的左上角X坐标。

取值范围：[0, +∞) 

单位：vp

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventLocationInfo-displayX: double--><!--Device-EventLocationInfo-displayX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: double
```

相对于屏幕的左上角Y坐标。

取值范围：[0, +∞) 

单位：vp

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventLocationInfo-displayY: double--><!--Device-EventLocationInfo-displayY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX?: double
```

在[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)中的X坐标。

取值范围：[0, +∞) 

单位：vp

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventLocationInfo-globalDisplayX?: double--><!--Device-EventLocationInfo-globalDisplayX?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY?: double
```

在[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)中的Y坐标。

取值范围：[0, +∞) 

单位：vp

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventLocationInfo-globalDisplayY?: double--><!--Device-EventLocationInfo-globalDisplayY?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX: double
```

相对于窗口的左上角X坐标。

取值范围：[0, +∞) 

单位：vp

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventLocationInfo-windowX: double--><!--Device-EventLocationInfo-windowX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY: double
```

相对于窗口的左上角Y坐标。

取值范围：[0, +∞) 

单位：vp

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventLocationInfo-windowY: double--><!--Device-EventLocationInfo-windowY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: double
```

相对于组件左上角的X坐标。

取值范围：[0, +∞) 

单位：vp

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventLocationInfo-x: double--><!--Device-EventLocationInfo-x: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y: double
```

相对于组件左上角的Y坐标。

取值范围：[0, +∞) 

单位：vp

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventLocationInfo-y: double--><!--Device-EventLocationInfo-y: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

