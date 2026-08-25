# PanRecognizer

Defines the gesture recognizer.@extends GestureRecognizer

**Inheritance/Implementation:** PanRecognizer extends [GestureRecognizer](arkts-arkui-gesture-gesturerecognizer-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDirection

```TypeScript
getDirection(): PanDirection
```

Returns the pan recognizer's direction attribute.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanDirection](arkts-arkui-gesture-pandirection-e.md) |

## getDistance

```TypeScript
getDistance(): double
```

Returns the pan recognizer's distance. The unit is vp.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| double |

## getDistanceMap

```TypeScript
getDistanceMap(): Map<SourceTool, double>
```

Returns the pan recognizer's distance map. The unit is vp.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Map&lt;[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md), double&gt; |

## getPanGestureOptions

```TypeScript
getPanGestureOptions(): PanGestureOptions
```

Returns the the pan gesture options of the recognizer.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanGestureOptions](arkts-arkui-gesture-pangestureoptions-c.md) |
