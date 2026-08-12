# PinchGestureHandler

Defines a type of gesture handler object for pinch gestures.

**Inheritance/Implementation:** PinchGestureHandler extends [GestureHandler<PinchGestureHandler>](GestureHandler<PinchGestureHandler>)

**Since:** 12

<!--Device-unnamed-declare class PinchGestureHandler extends GestureHandler<PinchGestureHandler>--><!--Device-unnamed-declare class PinchGestureHandler extends GestureHandler<PinchGestureHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: PinchGestureHandlerOptions)
```

Constructor used to create a pinch gesture handler instance.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-constructor(options?: PinchGestureHandlerOptions)--><!--Device-PinchGestureHandler-constructor(options?: PinchGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [PinchGestureHandlerOptions](arkts-arkui-pinchgesturehandleroptions-i.md) | No |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<void>): PinchGestureHandler
```

Sets the callback for pinch gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. No gesture event information is returned.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-onActionCancel(event: Callback<void>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionCancel(event: Callback<void>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback & lt;void & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): PinchGestureHandler
```

Sets the callback for pinch gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. Compared with   
[onActionCancel](#onActionCancel), this API returns gesture event information.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PinchGestureHandler-onActionCancel(event: Callback<GestureEvent>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionCancel(event: Callback<GestureEvent>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) |

## onActionEnd

```TypeScript
onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler
```

Sets the callback for pinch gesture recognition completion. This callback is triggered when all fingers are lifted after successful recognition.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) |

## onActionStart

```TypeScript
onActionStart(event: Callback<GestureEvent>): PinchGestureHandler
```

Sets the callback for successful pinch gesture recognition.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-onActionStart(event: Callback<GestureEvent>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionStart(event: Callback<GestureEvent>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) |

## onActionUpdate

```TypeScript
onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler
```

Sets the callback for pinch gesture movement updates. The callback is triggered when the pinch gesture moves.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) |
