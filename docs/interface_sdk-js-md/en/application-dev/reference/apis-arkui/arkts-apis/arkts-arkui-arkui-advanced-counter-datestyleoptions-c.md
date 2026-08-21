# DateStyleOptions

Defines the date style options.

**Inheritance/Implementation:** DateStyleOptions extends [CommonOptions](arkts-arkui-arkui-advanced-counter-commonoptions-c.md)

**Since:** 11

<!--Device-unnamed-declare class DateStyleOptions--><!--Device-unnamed-declare class DateStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { CounterComponent, CounterOptions, CounterType, DateData } from '@kit.ArkUI';
import { CounterV2Component, CounterV2Options, CounterV2DateData, CounterV2Type } from '@kit.ArkUI';
```

## day

```TypeScript
day?: number
```

Set the day of the counter component.

**Type:** number

**Default:** 1

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DateStyleOptions-day?: number--><!--Device-DateStyleOptions-day?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## month

```TypeScript
month?: number
```

Set the month of the counter component.

**Type:** number

**Default:** 1

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DateStyleOptions-month?: number--><!--Device-DateStyleOptions-month?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDateChange

```TypeScript
onDateChange?: (date: DateData) => void
```

Trigger an event when the date of the counter has been changed.

**Type:** (date: DateData) =&gt; void

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DateStyleOptions-onDateChange?: (date: DateData) => void--><!--Device-DateStyleOptions-onDateChange?: (date: DateData) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## year

```TypeScript
year?: number
```

Set the year of the counter component, ranges from 1 to 5000.

**Type:** number

**Default:** 1

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DateStyleOptions-year?: number--><!--Device-DateStyleOptions-year?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

