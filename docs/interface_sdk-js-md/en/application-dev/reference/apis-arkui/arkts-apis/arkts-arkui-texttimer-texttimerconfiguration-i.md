# TextTimerConfiguration

TextTimerConfiguration used by content modifier.

**Inheritance/Implementation:** TextTimerConfiguration extends CommonConfiguration<TextTimerConfiguration>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count: long
```

Timer duration, in milliseconds. It is effective only when isCountDown is true. The maximum value is 86400000 ms (24 hours).<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is between 0 and 86,400,000, it is used as the initial countdown time. <br>Otherwise, the default value is used as the initial countdown time. </p>

**Type:** long

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## elapsedTime

```TypeScript
elapsedTime: long
```

Elapsed time of the timer, in the minimum unit of the format.

**Type:** long

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isCountDown

```TypeScript
isCountDown: boolean
```

Whether the timer is a countdown. The value true means that the timer counts down, and false means that the timer counts up.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## started

```TypeScript
started: boolean
```

Whether the timer has already started.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startTime

```TypeScript
startTime?: int
```

The start time of the timer. It is effective only when isCountDown is false. The value should be an integer.Unit: ms. Default value: 0.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
