# PanGestureOptions

Defines the PanGesture options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PanGestureOptions--><!--Device-unnamed-export declare class PanGestureOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value?: PanGestureHandlerOptions)
```

Constructor parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-constructor(value?: PanGestureHandlerOptions)--><!--Device-PanGestureOptions-constructor(value?: PanGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PanGestureHandlerOptions](arkts-arkui-pangesturehandleroptions-i.md) | No |  |

## getDirection

```TypeScript
getDirection(): PanDirection
```

Get the pan direction attribute.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-getDirection(): PanDirection--><!--Device-PanGestureOptions-getDirection(): PanDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PanDirection](arkts-arkui-gesture-pandirection-e.md) | Pan gesture direction |

## getDistance

```TypeScript
getDistance(): double
```

Returns the pan gesture's distance.The unit is vp.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-getDistance(): double--><!--Device-PanGestureOptions-getDistance(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | the distance of the pan gesture. |

## setDirection

```TypeScript
setDirection(value: PanDirection): void
```

Sets the direction attribute.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-setDirection(value: PanDirection): void--><!--Device-PanGestureOptions-setDirection(value: PanDirection): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PanDirection](arkts-arkui-gesture-pandirection-e.md) | Yes |  |

## setDistance

```TypeScript
setDistance(value: double): void
```

Sets the setDistance attribute.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-setDistance(value: double): void--><!--Device-PanGestureOptions-setDistance(value: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes |  |

## setFingers

```TypeScript
setFingers(value: int): void
```

Sets the setFingers attribute.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-setFingers(value: int): void--><!--Device-PanGestureOptions-setFingers(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes |  |

