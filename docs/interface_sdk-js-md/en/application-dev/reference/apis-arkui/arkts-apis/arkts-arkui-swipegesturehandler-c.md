# SwipeGestureHandler

Defines a swipe gesture handler object.

**Inheritance/Implementation:** SwipeGestureHandler extends GestureHandler<SwipeGestureHandler>

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options?: SwipeGestureHandlerOptions)
```

Constructor used to create a swipe gesture handler instance.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SwipeGestureHandlerOptions](arkts-arkui-swipegesturehandleroptions-i.md) | No |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): SwipeGestureHandler
```

Sets the callback for successful swipe gesture recognition.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwipeGestureHandler](arkts-arkui-swipegesturehandler-c.md) |
