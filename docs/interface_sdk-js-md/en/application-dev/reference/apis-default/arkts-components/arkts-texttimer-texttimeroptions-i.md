# TextTimerOptions

Parameters of the TextTimer component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface TextTimerOptions--><!--Device-unnamed-export interface TextTimerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TextTimerController
```

TextTimer controller.

**Type:** [TextTimerController](arkts-texttimer-texttimercontroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerOptions-controller?: TextTimerController--><!--Device-TextTimerOptions-controller?: TextTimerController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: long
```

Timer duration, in milliseconds. It is effective only when isCountDown is true. The maximum value is 86400000 ms (24 hours). Default value: 60000 ms.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is between 0 and 86,400,000, it is used as the initial countdown time. <br>Otherwise, the default value is used as the initial countdown time. </p>

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

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

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerOptions-isCountDown?: boolean--><!--Device-TextTimerOptions-isCountDown?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startTime

```TypeScript
startTime?: int
```

The start time of the timer. It is effective only when isCountDown is false. The value should be an integer.Unit: ms. Default value: 0.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerOptions-startTime?: int--><!--Device-TextTimerOptions-startTime?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

