# SwipeEdgeEffect

```TypeScript
declare enum SwipeEdgeEffect
```

Enumerates the edge effects.

**Since:** 9

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Spring

```TypeScript
Spring
```

The **ListItem** can continue to be swiped after the swipe distance exceeds the size of the swipe-out component.

If a delete area is set, the **ListItem** can continue to be swiped after the swipe distance exceeds the delete threshold,

and it rebounds along the spring damping curve after being released.

**Since:** 9

**Model restriction:** This API can be used in both the stage model and FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## None

```TypeScript
None
```

The swipe distance of the **ListItem** cannot exceed the size of the swipe-out component.

If a delete area is set, the swipe distance of the **ListItem** cannot exceed the delete threshold,

and when a delete callback is set, releasing the **ListItem** after the delete threshold is reached triggers the delete callback.

**Since:** 9

**Model restriction:** This API can be used in both the stage model and FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
