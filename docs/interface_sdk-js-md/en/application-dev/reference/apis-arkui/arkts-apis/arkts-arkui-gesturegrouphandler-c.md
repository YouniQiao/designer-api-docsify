# GestureGroupHandler

Defines a gesture group handler object.

**Inheritance/Implementation:** GestureGroupHandler extends GestureHandler<GestureGroupHandler>

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options?: GestureGroupGestureHandlerOptions)
```

Constructor used to create a gesture group handler instance.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GestureGroupGestureHandlerOptions](arkts-arkui-gesturegroupgesturehandleroptions-i.md) | No |

## onCancel

```TypeScript
onCancel(event: Callback<void>): GestureGroupHandler
```

Sets the cancellation callback for the gesture group handler. The callback is triggered when a sequence gesture ([GestureMode](arkts-arkui-gesturemode-e.md).Sequence) is cancelled.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback & lt;void & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GestureGroupHandler](arkts-arkui-gesturegrouphandler-c.md) |
