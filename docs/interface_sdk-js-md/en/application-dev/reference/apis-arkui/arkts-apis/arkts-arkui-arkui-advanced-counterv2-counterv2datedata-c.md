# CounterV2DateData

Defines the date data.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-declare class CounterV2DateData--><!--Device-unnamed-declare class CounterV2DateData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { CounterV2Component } from 'CounterV2Component';
import { CounterV2Options } from 'CounterV2Options';
import { CounterV2DateData } from 'CounterV2DateData';
import { CounterV2Type } from 'CounterV2Type';
```

## constructor

```TypeScript
constructor(year: int, month: int, day: int)
```

Constructor of the DateData.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2DateData-constructor(year: int, month: int, day: int)--><!--Device-CounterV2DateData-constructor(year: int, month: int, day: int)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | int | Yes | set the year of the DateData. |
| month | int | Yes | set the month of the DateData. |
| day | int | Yes | set the day of the DateData. |

## toString

```TypeScript
toString(): string
```

Convert the date data to string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2DateData-toString(): string--><!--Device-CounterV2DateData-toString(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | date data in string form. |

## day

```TypeScript
day: int
```

The day of the DateData.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2DateData-day: int--><!--Device-CounterV2DateData-day: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## month

```TypeScript
month: int
```

The month of the DateData.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2DateData-month: int--><!--Device-CounterV2DateData-month: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## year

```TypeScript
year: int
```

The year of the DateData, ranges from 1 to 5000.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2DateData-year: int--><!--Device-CounterV2DateData-year: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

