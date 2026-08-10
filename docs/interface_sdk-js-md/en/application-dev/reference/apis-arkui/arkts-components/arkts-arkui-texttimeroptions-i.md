# TextTimerOptions

用于构建TextTimer组件的选项。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-interface TextTimerOptions--><!--Device-unnamed-interface TextTimerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TextTimerController
```

TextTimer控制器，用于通过编程方式控制计时器的启动、暂停和重置。不传入时，计时器仍可正常显示但无法通过代码控制其状态。

**Type:** [TextTimerController](arkts-arkui-texttimercontroller-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TextTimerOptions-controller?: TextTimerController--><!--Device-TextTimerOptions-controller?: TextTimerController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: number
```

计时器初始时间，单位为毫秒，isCountDown为true时生效。

默认值：60000

取值范围为(0, 86400000)，即不超过24小时。超出取值范围时置为默认值。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TextTimerOptions-count?: number--><!--Device-TextTimerOptions-count?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isCountDown

```TypeScript
isCountDown?: boolean
```

倒计时开关。

true：计时器开启倒计时，例如从30秒~0秒。

false：计时器开始计时，例如从0秒~30秒。

默认值：false

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TextTimerOptions-isCountDown?: boolean--><!--Device-TextTimerOptions-isCountDown?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startTime

```TypeScript
startTime?: number
```

计时器正向计时模式下的初始时间，仅当isCountDown为false时该参数设置生效。

取值范围：[−2147483648, 2147483647]。

默认值：0 

单位：毫秒 

当值为负数时，计时器将从负值开始计时，经过0后继续向正数计时。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-TextTimerOptions-startTime?: number--><!--Device-TextTimerOptions-startTime?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

