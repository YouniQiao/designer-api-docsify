# TextClockConfiguration

开发者需要自定义class实现ContentModifier接口。

**Inheritance/Implementation:** TextClockConfiguration extends [CommonConfiguration<TextClockConfiguration>](CommonConfiguration<TextClockConfiguration>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface TextClockConfiguration extends CommonConfiguration<TextClockConfiguration>--><!--Device-unnamed-declare interface TextClockConfiguration extends CommonConfiguration<TextClockConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## started

```TypeScript
started: boolean
```

指示文本时钟是否启动。

true：表示启动文本时钟。

false：表示停止文本时钟。

默认值：true

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextClockConfiguration-started: boolean--><!--Device-TextClockConfiguration-started: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeValue

```TypeScript
timeValue: number
```

当前文本时钟时区的UTC秒数。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextClockConfiguration-timeValue: number--><!--Device-TextClockConfiguration-timeValue: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeZoneOffset

```TypeScript
timeZoneOffset: number
```

当前文本时钟时区偏移量。

取值范围为[-14, 12]，表示东十二区到西十二区，其中负值表示东时区，正值表示西时区，比如东八区为-8。设置值为该取值范围内的浮点数时会进行取整，舍弃小数部分。当设置的值不在取值范围内时，将使用当前系统的时区偏移量。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextClockConfiguration-timeZoneOffset: number--><!--Device-TextClockConfiguration-timeZoneOffset: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

