# TouchType

定义触摸操作的触发状态类型。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare enum TouchType--><!--Device-unnamed-declare enum TouchType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Down

```TypeScript
Down
```

手指按下时触发。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TouchType-Down--><!--Device-TouchType-Down-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Up

```TypeScript
Up
```

手指抬起时触发。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TouchType-Up--><!--Device-TouchType-Up-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Move

```TypeScript
Move
```

手指按压并在屏幕上移动时触发。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TouchType-Move--><!--Device-TouchType-Move-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Cancel

```TypeScript
Cancel
```

触摸事件取消时触发。例如：1.手指按住屏幕同时点击Home键返回桌面，此时会触发Cancel；2.手指触摸过程中存在手写笔操作，手指的触摸操作会收到Cancel事件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TouchType-Cancel--><!--Device-TouchType-Cancel-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_ENTER

```TypeScript
HOVER_ENTER = 9
```

无障碍模式下，手指按下时触发。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TouchType-HOVER_ENTER = 9--><!--Device-TouchType-HOVER_ENTER = 9-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_MOVE

```TypeScript
HOVER_MOVE = 10
```

无障碍模式下，触摸移动时触发。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TouchType-HOVER_MOVE = 10--><!--Device-TouchType-HOVER_MOVE = 10-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_EXIT

```TypeScript
HOVER_EXIT = 11
```

无障碍模式下，抬手时触发。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TouchType-HOVER_EXIT = 11--><!--Device-TouchType-HOVER_EXIT = 11-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_CANCEL

```TypeScript
HOVER_CANCEL = 12
```

无障碍模式下，取消当前触发的事件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TouchType-HOVER_CANCEL = 12--><!--Device-TouchType-HOVER_CANCEL = 12-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

