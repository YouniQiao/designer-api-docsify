# TouchPadEvent

```TypeScript
declare abstract class TouchPadEvent
```

Describes a raw touchpad event. The event is independent of touch, mouse, axis, and system gesture events.

**Since:** 26.1.0

<!--Device-unnamed-declare abstract class TouchPadEvent--><!--Device-unnamed-declare abstract class TouchPadEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getModifierKeyState

```TypeScript
getModifierKeyState(keys: Array<string>): boolean
```

Obtains the pressed status of modifier keys. The Ctrl, Alt, and Shift keys are supported.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-getModifierKeyState(keys: Array<string>): boolean--><!--Device-TouchPadEvent-getModifierKeyState(keys: Array<string>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | Yes | Modifier key list. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Pressed status of modifier keys. Returns **true** if all specified modifier keys are pressed; returns **false** otherwise. |

## stopPropagation

```TypeScript
stopPropagation(): void
```

Stops propagation of the current touchpad event in the ArkUI node event chain. This operation does not affect touch, mouse, axis, or system gesture events.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-stopPropagation(): void--><!--Device-TouchPadEvent-stopPropagation(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changedContact

```TypeScript
changedContact: TouchPadEventContact
```

Contact that changed and triggered the event.

**Type:** [TouchPadEventContact](arkts-arkui-common-comp-touchpadeventcontact-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-changedContact: TouchPadEventContact--><!--Device-TouchPadEvent-changedContact: TouchPadEventContact-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contacts

```TypeScript
contacts: TouchPadEventContact[]
```

All contacts reported for the event. The number of contacts depends on the hardware capability and has no fixed public upper limit.

**Type:** [TouchPadEventContact](arkts-arkui-common-comp-touchpadeventcontact-i.md)[]

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-contacts: TouchPadEventContact[]--><!--Device-TouchPadEvent-contacts: TouchPadEventContact[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deviceHeight

```TypeScript
deviceHeight: number
```

Height of the touchpad. The unit is mm.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-deviceHeight: double--><!--Device-TouchPadEvent-deviceHeight: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deviceId

```TypeScript
deviceId: number
```

ID of the touchpad that triggers the event. The value must be greater than or equal to 0.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-deviceId: int--><!--Device-TouchPadEvent-deviceId: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deviceWidth

```TypeScript
deviceWidth: number
```

Width of the touchpad. The unit is mm.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-deviceWidth: double--><!--Device-TouchPadEvent-deviceWidth: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayX

```TypeScript
displayX: number
```

X coordinate of the cursor in the coordinate system of the current application screen. Unit: vp.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-displayX: double--><!--Device-TouchPadEvent-displayX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: number
```

Y coordinate of the cursor in the coordinate system of the current application screen. Unit: vp..

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-displayY: double--><!--Device-TouchPadEvent-displayY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX: number
```

X coordinate of the cursor in the global coordinate system. Unit: vp.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-globalDisplayX: double--><!--Device-TouchPadEvent-globalDisplayX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY: number
```

Y coordinate of the cursor in the global coordinate system. Unit: vp.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-globalDisplayY: double--><!--Device-TouchPadEvent-globalDisplayY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## source

```TypeScript
source: SourceType
```

Input source of the event.

**Type:** [SourceType](arkts-arkui-common-comp-sourcetype-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-source: SourceType--><!--Device-TouchPadEvent-source: SourceType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sourceTool

```TypeScript
sourceTool: SourceTool
```

Input tool of the event.

**Type:** [SourceTool](arkts-arkui-common-comp-sourcetool-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-sourceTool: SourceTool--><!--Device-TouchPadEvent-sourceTool: SourceTool-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## target

```TypeScript
target: EventTarget
```

Object that triggers the event.

**Type:** [EventTarget](arkts-arkui-common-comp-eventtarget-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-target: EventTarget--><!--Device-TouchPadEvent-target: EventTarget-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetDisplayId

```TypeScript
targetDisplayId?: number
```

ID of the screen where the event occurs. The value must be greater than or equal to 0. Default value: **0**.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-targetDisplayId?: int--><!--Device-TouchPadEvent-targetDisplayId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: number
```

Timestamp of the event, representing the interval from system startup to event occurrence. Unit: ns.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-timestamp: long--><!--Device-TouchPadEvent-timestamp: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX: number
```

X coordinate of the cursor in the coordinate system of the current application window. Unit: vp.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-windowX: double--><!--Device-TouchPadEvent-windowX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY: number
```

Y coordinate of the cursor in the coordinate system of the current application window. Unit: vp.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-windowY: double--><!--Device-TouchPadEvent-windowY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: number
```

X coordinate of the cursor in the coordinate system of the event-responsive component. Unit: vp.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-x: double--><!--Device-TouchPadEvent-x: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y: number
```

Y coordinate of the cursor in the coordinate system of the event-responsive component. Unit: vp.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEvent-y: double--><!--Device-TouchPadEvent-y: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
