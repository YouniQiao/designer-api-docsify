# TouchType

定义触摸操作的触发状态类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum TouchType--><!--Device-unnamed-export declare enum TouchType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Down

```TypeScript
Down = 0
```

手指按下时触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchType-Down = 0--><!--Device-TouchType-Down = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Up

```TypeScript
Up = 1
```

手指抬起时触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchType-Up = 1--><!--Device-TouchType-Up = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Move

```TypeScript
Move = 2
```

手指按压并在屏幕上移动时触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchType-Move = 2--><!--Device-TouchType-Move = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Cancel

```TypeScript
Cancel = 3
```

触摸事件取消时触发。例如：1.手指按住屏幕同时点击Home键返回桌面，此时会触发Cancel；2.&lt;!--RP2--&gt;&lt;!--RP2End--&gt;手指触摸过程中存在手写笔操作，手指的触摸操作会收到Cancel事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchType-Cancel = 3--><!--Device-TouchType-Cancel = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_ENTER

```TypeScript
HOVER_ENTER = 9
```

无障碍模式下，手指按下时触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchType-HOVER_ENTER = 9--><!--Device-TouchType-HOVER_ENTER = 9-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_MOVE

```TypeScript
HOVER_MOVE = 10
```

无障碍模式下，触摸移动时触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchType-HOVER_MOVE = 10--><!--Device-TouchType-HOVER_MOVE = 10-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_EXIT

```TypeScript
HOVER_EXIT = 11
```

无障碍模式下，抬手时触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchType-HOVER_EXIT = 11--><!--Device-TouchType-HOVER_EXIT = 11-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HOVER_CANCEL

```TypeScript
HOVER_CANCEL = 12
```

无障碍模式下，取消当前触发的事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchType-HOVER_CANCEL = 12--><!--Device-TouchType-HOVER_CANCEL = 12-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

