# BaseEvent

Defines the base event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface BaseEvent--><!--Device-unnamed-export declare interface BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## axisHorizontal

```TypeScript
axisHorizontal?: double
```

the Horizontal axis coordinate.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-axisHorizontal?: double--><!--Device-BaseEvent-axisHorizontal?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## axisPinch

```TypeScript
axisPinch?: double
```

Indicates the Pinch axis coordinate.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-axisPinch?: double--><!--Device-BaseEvent-axisPinch?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## axisVertical

```TypeScript
axisVertical?: double
```

the Vertical axis coordinate.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-axisVertical?: double--><!--Device-BaseEvent-axisVertical?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deviceId

```TypeScript
deviceId?: int
```

Indicates the ID of the input device that triggers the current event.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-deviceId?: int--><!--Device-BaseEvent-deviceId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getModifierKeyState

```TypeScript
getModifierKeyState?: ModifierKeyStateGetter
```

Query the modifier key press state, support 'ctrl'|'alt'|'shift'

**Type:** [ModifierKeyStateGetter](arkts-modifierkeystategetter-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-getModifierKeyState?: ModifierKeyStateGetter--><!--Device-BaseEvent-getModifierKeyState?: ModifierKeyStateGetter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pressure

```TypeScript
pressure: double
```

Press pressure.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-pressure: double--><!--Device-BaseEvent-pressure: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rollAngle

```TypeScript
rollAngle?: double
```

Indicates the angle at which the stylus rotates around the Z-axis.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-rollAngle?: double--><!--Device-BaseEvent-rollAngle?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## source

```TypeScript
source: SourceType
```

Event input device.

**Type:** [SourceType](arkts-common-sourcetype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-source: SourceType--><!--Device-BaseEvent-source: SourceType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sourceTool

```TypeScript
sourceTool: SourceTool
```

Event input source.

**Type:** [SourceTool](arkts-common-sourcetool-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-sourceTool: SourceTool--><!--Device-BaseEvent-sourceTool: SourceTool-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## target

```TypeScript
target: EventTarget
```

Display area of the element that triggers the gesture event.

**Type:** [EventTarget](arkts-common-eventtarget-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-target: EventTarget--><!--Device-BaseEvent-target: EventTarget-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetDisplayId

```TypeScript
targetDisplayId?: int
```

Indicates the screen ID on which the event occurred.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-targetDisplayId?: int--><!--Device-BaseEvent-targetDisplayId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tiltX

```TypeScript
tiltX: double
```

Angle between the projection of the stylus on the device plane and the x-axis.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-tiltX: double--><!--Device-BaseEvent-tiltX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tiltY

```TypeScript
tiltY: double
```

Angle between the projection of the stylus on the device plane and the y-axis.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-tiltY: double--><!--Device-BaseEvent-tiltY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: long
```

Timestamp of the event.

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseEvent-timestamp: long--><!--Device-BaseEvent-timestamp: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

