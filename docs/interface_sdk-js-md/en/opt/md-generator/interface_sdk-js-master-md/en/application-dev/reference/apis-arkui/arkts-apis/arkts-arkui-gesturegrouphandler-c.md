# GestureGroupHandler

Defines a gesture group handler object.

**Inheritance/Implementation:** GestureGroupHandler extends [GestureHandler<GestureGroupHandler>](GestureHandler<GestureGroupHandler>)

**Since:** 12

<!--Device-unnamed-declare class GestureGroupHandler extends GestureHandler<GestureGroupHandler>--><!--Device-unnamed-declare class GestureGroupHandler extends GestureHandler<GestureGroupHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: GestureGroupGestureHandlerOptions)
```

Constructor used to create a gesture group handler instance.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureGroupHandler-constructor(options?: GestureGroupGestureHandlerOptions)--><!--Device-GestureGroupHandler-constructor(options?: GestureGroupGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GestureGroupGestureHandlerOptions](arkts-arkui-gesturegroupgesturehandleroptions-i.md) | No |

## onCancel

```TypeScript
onCancel(event: Callback<void>): GestureGroupHandler
```

Sets the cancellation callback for the gesture group handler. The callback is triggered when a sequence gesture (  
[GestureMode](arkts-arkui-gesturemode-e.md#GestureMode).Sequence) is cancelled.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureGroupHandler-onCancel(event: Callback<void>): GestureGroupHandler--><!--Device-GestureGroupHandler-onCancel(event: Callback<void>): GestureGroupHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback & lt;void & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GestureGroupHandler](arkts-arkui-gesturegrouphandler-c.md) |
