# TextTimerOptions

Parameters of the TextTimer component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface TextTimerOptions--><!--Device-unnamed-export interface TextTimerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TextTimerController
```

TextTimer controller.

**Type:** TextTimerController

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerOptions-controller?: TextTimerController--><!--Device-TextTimerOptions-controller?: TextTimerController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: long
```

Timer duration, in milliseconds. It is effective only when isCountDown is true. The maximum value is 86400000 ms (24 hours). Default value: 60000 ms. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If the value is between 0 and 86,400,000, it is used as the initial countdown time. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_Otherwise, the default value is used as the initial countdown time. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerOptions-count?: long--><!--Device-TextTimerOptions-count?: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isCountDown

```TypeScript
isCountDown?: boolean
```

Whether the timer is a countdown. The value true means that the timer counts down, and false means that the timer counts up. Default value: false.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerOptions-isCountDown?: boolean--><!--Device-TextTimerOptions-isCountDown?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startTime

```TypeScript
startTime?: int
```

The start time of the timer. It is effective only when isCountDown is false. The value should be an integer. Unit: ms. Default value: 0.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerOptions-startTime?: int--><!--Device-TextTimerOptions-startTime?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

