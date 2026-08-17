# CounterV2InlineStyleOptions

Defines the inline style options.

**Inheritance/Implementation:** CounterV2InlineStyleOptions extends [CounterV2CommonOptions](arkts-arkui-arkui-advanced-counterv2-counterv2commonoptions-c.md#counterv2commonoptions)

**Since:** 26.0.0

<!--Device-unnamed-declare class CounterV2InlineStyleOptions--><!--Device-unnamed-declare class CounterV2InlineStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { CounterV2Component } from 'CounterV2Component';
import { CounterV2Options } from 'CounterV2Options';
import { CounterV2DateData } from 'CounterV2DateData';
import { CounterV2Type } from 'CounterV2Type';
```

## max

```TypeScript
max?: int
```

Set maximum value of the counter component

**Type:** int

**Default:** 999

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2InlineStyleOptions-max?: int--><!--Device-CounterV2InlineStyleOptions-max?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min?: int
```

Set minimum value of the counter component

**Type:** int

**Default:** 0

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2InlineStyleOptions-min?: int--><!--Device-CounterV2InlineStyleOptions-min?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: OnInlineCounterV2Change
```

Trigger an event when the value of the counter has been changed.

**Type:** [OnInlineCounterV2Change](arkts-arkui-oninlinecounterv2change-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2InlineStyleOptions-onChange?: OnInlineCounterV2Change--><!--Device-CounterV2InlineStyleOptions-onChange?: OnInlineCounterV2Change-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textWidth

```TypeScript
textWidth?: double
```

Set text width of the counter component, ranges greater than or equal to 0. If undefined is passed, the text width will adapt to the text content.

**Type:** double

**Default:** undefined

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2InlineStyleOptions-textWidth?: double--><!--Device-CounterV2InlineStyleOptions-textWidth?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: int
```

Set initial value of the counter component, ranges from min to max.

**Type:** int

**Default:** 0

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2InlineStyleOptions-value?: int--><!--Device-CounterV2InlineStyleOptions-value?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

