# TouchType

```TypeScript
declare enum TouchType
```

Sets the trigger status type of a touch operation.

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Down

```TypeScript
Down
```

A finger is pressed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Up

```TypeScript
Up
```

A finger is lifted.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Move

```TypeScript
Move
```

A finger moves on the screen in pressed state.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Cancel

```TypeScript
Cancel
```

A touch event is canceled. For example: 1. When a finger is held on the screen and the Home key is tapped to return to the home screen, **Cancel** is triggered; 2. <!--RP2--><!--RP2End-->When a stylus operation occurs during a finger touch, the finger touch operation receives a Cancel event.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_ENTER

```TypeScript
HOVER_ENTER = 9
```

A finger is pressed in accessibility mode.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_MOVE

```TypeScript
HOVER_MOVE = 10
```

The touch moves in accessibility mode.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_EXIT

```TypeScript
HOVER_EXIT = 11
```

A finger is lifted in accessibility mode.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_CANCEL

```TypeScript
HOVER_CANCEL = 12
```

The current event is canceled in accessibility mode.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
