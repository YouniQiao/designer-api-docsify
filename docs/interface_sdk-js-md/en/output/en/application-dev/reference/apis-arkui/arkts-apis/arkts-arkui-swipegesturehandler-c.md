# SwipeGestureHandler

Defines a swipe gesture handler object.

**Inheritance/Implementation:** SwipeGestureHandler extends [GestureHandler<SwipeGestureHandler>](GestureHandler<SwipeGestureHandler>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class SwipeGestureHandler extends GestureHandler<SwipeGestureHandler>--><!--Device-unnamed-declare class SwipeGestureHandler extends GestureHandler<SwipeGestureHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: SwipeGestureHandlerOptions)
```

Constructor used to create a swipe gesture handler instance.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeGestureHandler-constructor(options?: SwipeGestureHandlerOptions)--><!--Device-SwipeGestureHandler-constructor(options?: SwipeGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters of the swipe gesture handler. |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): SwipeGestureHandler
```

Sets the callback for successful swipe gesture recognition.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeGestureHandler-onAction(event: Callback<GestureEvent>): SwipeGestureHandler--><!--Device-SwipeGestureHandler-onAction(event: Callback<GestureEvent>): SwipeGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;GestureEvent&gt; | Yes | Callback invoked upon successful swipe gesture recognition. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Swipe gesture handler object. |

