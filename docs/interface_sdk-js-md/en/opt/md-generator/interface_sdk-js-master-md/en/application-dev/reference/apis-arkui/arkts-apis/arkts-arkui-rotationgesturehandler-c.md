# RotationGestureHandler

Defines a rotation gesture handler object.

**Inheritance/Implementation:** RotationGestureHandler extends [GestureHandler<RotationGestureHandler>](GestureHandler<RotationGestureHandler>)

**Since:** 12

<!--Device-unnamed-declare class RotationGestureHandler extends GestureHandler<RotationGestureHandler>--><!--Device-unnamed-declare class RotationGestureHandler extends GestureHandler<RotationGestureHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: RotationGestureHandlerOptions)
```

Constructor used to create a rotation gesture handler instance.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-constructor(options?: RotationGestureHandlerOptions)--><!--Device-RotationGestureHandler-constructor(options?: RotationGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RotationGestureHandlerOptions](arkts-arkui-rotationgesturehandleroptions-i.md) | No |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<void>): RotationGestureHandler
```

Sets the callback for rotation gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. No gesture event information is returned.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-onActionCancel(event: Callback<void>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionCancel(event: Callback<void>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): RotationGestureHandler
```

Sets the callback for rotation gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. Compared with   
[onActionCancel](arkts-arkui-rotationgesturehandler-c.md#onactioncancel), this API returns gesture event information.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-RotationGestureHandler-onActionCancel(event: Callback<GestureEvent>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionCancel(event: Callback<GestureEvent>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GestureEvent&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) |

## onActionEnd

```TypeScript
onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler
```

Sets the callback for rotation gesture recognition completion. This callback is triggered when all fingers are lifted after successful recognition.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GestureEvent&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) |

## onActionStart

```TypeScript
onActionStart(event: Callback<GestureEvent>): RotationGestureHandler
```

Sets the callback for successful rotation gesture recognition.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-onActionStart(event: Callback<GestureEvent>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionStart(event: Callback<GestureEvent>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GestureEvent&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) |

## onActionUpdate

```TypeScript
onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler
```

Sets the callback for rotation gesture movement updates. The callback is triggered when the rotation gesture moves.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GestureEvent&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) |
