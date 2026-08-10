# TextTimerConfiguration

ContentModifier接口使用的TextTimer配置。

开发者需要自定义class实现ContentModifier接口。

**Inheritance/Implementation:** TextTimerConfiguration extends [CommonConfiguration<TextTimerConfiguration>](CommonConfiguration<TextTimerConfiguration>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextTimerConfiguration extends CommonConfiguration<TextTimerConfiguration>--><!--Device-unnamed-export declare interface TextTimerConfiguration extends CommonConfiguration<TextTimerConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count: long
```

计时器时间（isCountDown为true时生效），单位为毫秒。最长不超过86400000毫秒（24小时）。 0<count<86400000时，count值为倒计时初始值。否则，使用默认值为倒计时初始值。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerConfiguration-count: long--><!--Device-TextTimerConfiguration-count: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## elapsedTime

```TypeScript
elapsedTime: long
```

计时器经过的时间，单位为设置格式的最小单位。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerConfiguration-elapsedTime: long--><!--Device-TextTimerConfiguration-elapsedTime: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isCountDown

```TypeScript
isCountDown: boolean
```

是否倒计时。

true：计时器开启倒计时，例如从30秒 ~ 0秒；false：计时器开始计时，例如从0秒 ~ 30秒。

默认值：false。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerConfiguration-isCountDown: boolean--><!--Device-TextTimerConfiguration-isCountDown: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startTime

```TypeScript
startTime?: int
```

计时器经过的时间，单位为设置格式的最小单位。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerConfiguration-startTime?: int--><!--Device-TextTimerConfiguration-startTime?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## started

```TypeScript
started: boolean
```

是否已经开始了计时。

true：开始计时；false：未开始计时。

默认值：false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerConfiguration-started: boolean--><!--Device-TextTimerConfiguration-started: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

