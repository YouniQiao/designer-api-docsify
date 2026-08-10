# TextTimerConfiguration

ContentModifier接口使用的TextTimer配置。

开发者需要自定义class实现ContentModifier接口。

**Inheritance/Implementation:** TextTimerConfiguration extends [CommonConfiguration<TextTimerConfiguration>](CommonConfiguration<TextTimerConfiguration>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface TextTimerConfiguration extends CommonConfiguration<TextTimerConfiguration>--><!--Device-unnamed-declare interface TextTimerConfiguration extends CommonConfiguration<TextTimerConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count: number
```

计时器初始时间，单位为毫秒，isCountDown为true时生效。

默认值：60000

取值范围为(0, 86400000)，即不超过24小时。超出取值范围时置为默认值。

**Type:** number

**Default:** 60000

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextTimerConfiguration-count: number--><!--Device-TextTimerConfiguration-count: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## elapsedTime

```TypeScript
elapsedTime: number
```

计时器经过的时间，单位为设置格式的最小单位。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextTimerConfiguration-elapsedTime: number--><!--Device-TextTimerConfiguration-elapsedTime: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isCountDown

```TypeScript
isCountDown: boolean
```

是否倒计时。

true：计时器开启倒计时，例如从30秒 ~ 0秒；false：计时器开始计时，例如从0秒 ~ 30秒。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextTimerConfiguration-isCountDown: boolean--><!--Device-TextTimerConfiguration-isCountDown: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startTime

```TypeScript
startTime?: number
```

计时器正向计时模式下的初始时间，仅当isCountDown为false时该参数设置生效。

取值范围：无上限，支持负数。

默认值：0 

单位：毫秒 

当值为负数时，计时器将从负值开始计时，经过0后继续向正数计时。

**Type:** number

**Default:** 0

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextTimerConfiguration-startTime?: number--><!--Device-TextTimerConfiguration-startTime?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## started

```TypeScript
started: boolean
```

是否已经开始了计时。

true：开始计时；false：未开始计时。

默认值：false

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextTimerConfiguration-started: boolean--><!--Device-TextTimerConfiguration-started: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

