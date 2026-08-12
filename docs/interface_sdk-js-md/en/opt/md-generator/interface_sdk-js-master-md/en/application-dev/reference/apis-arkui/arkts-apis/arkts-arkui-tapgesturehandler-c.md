# TapGestureHandler

Defines a type of gesture handler object for tap gestures.

**Inheritance/Implementation:** TapGestureHandler extends [GestureHandler<TapGestureHandler>](GestureHandler<TapGestureHandler>)

**Since:** 12

<!--Device-unnamed-declare class TapGestureHandler extends GestureHandler<TapGestureHandler>--><!--Device-unnamed-declare class TapGestureHandler extends GestureHandler<TapGestureHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: TapGestureHandlerOptions)
```

Constructor used to create a tap gesture handler instance.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TapGestureHandler-constructor(options?: TapGestureHandlerOptions)--><!--Device-TapGestureHandler-constructor(options?: TapGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TapGestureHandlerOptions](arkts-arkui-tapgesturehandleroptions-i.md) | No |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): TapGestureHandler
```

Sets the callback for successful tap gesture recognition.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TapGestureHandler-onAction(event: Callback<GestureEvent>): TapGestureHandler--><!--Device-TapGestureHandler-onAction(event: Callback<GestureEvent>): TapGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TapGestureHandler](arkts-arkui-tapgesturehandler-c.md) |
