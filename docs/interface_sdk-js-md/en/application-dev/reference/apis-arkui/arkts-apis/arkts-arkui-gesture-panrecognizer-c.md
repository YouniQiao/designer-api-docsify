# PanRecognizer

Defines the gesture recognizer.

**Inheritance/Implementation:** PanRecognizer extends [GestureRecognizer](arkts-arkui-gesture-gesturerecognizer-c.md#GestureRecognizer)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class PanRecognizer--><!--Device-unnamed-export declare class PanRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDirection

```TypeScript
getDirection(): PanDirection
```

Returns the pan recognizer's direction attribute.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanRecognizer-getDirection(): PanDirection--><!--Device-PanRecognizer-getDirection(): PanDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PanDirection](arkts-arkui-gesture-pandirection-e.md) | Pan recognizer direction |

## getDistance

```TypeScript
getDistance(): double
```

Returns the pan recognizer's distance. The unit is vp.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanRecognizer-getDistance(): double--><!--Device-PanRecognizer-getDistance(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | the distance of the pan recognizer. |

## getDistanceMap

```TypeScript
getDistanceMap(): Map<SourceTool, double>
```

Returns the pan recognizer's distance map. The unit is vp.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanRecognizer-getDistanceMap(): Map<SourceTool, double>--><!--Device-PanRecognizer-getDistanceMap(): Map<SourceTool, double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Map&lt;[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md), double&gt; | the distance map of the pan recognizer. |

## getPanGestureOptions

```TypeScript
getPanGestureOptions(): PanGestureOptions
```

Returns the the pan gesture options of the recognizer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanRecognizer-getPanGestureOptions(): PanGestureOptions--><!--Device-PanRecognizer-getPanGestureOptions(): PanGestureOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureOptions](arkts-arkui-gesture-pangestureoptions-c.md) | Pan gesture options |

