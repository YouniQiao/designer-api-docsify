# CounterV2InlineStyleOptions

Defines the inline style options.

**Inheritance/Implementation:** CounterV2InlineStyleOptions extends [CounterV2CommonOptions](arkts-arkui-arkui-advanced-counterv2-counterv2commonoptions-c.md#CounterV2CommonOptions)

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-unnamed-declare class CounterV2InlineStyleOptions--><!--Device-unnamed-declare class CounterV2InlineStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { CounterV2Component, CounterV2Options, CounterV2Type, CounterV2DateData } from '@kit.ArkUI';
```

## max

```TypeScript
max?: number
```

Set maximum value of the counter component

**Type:** number

**Default:** 999

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2InlineStyleOptions-max?: int--><!--Device-CounterV2InlineStyleOptions-max?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min?: number
```

Set minimum value of the counter component

**Type:** number

**Default:** 0

**Since:** 26.0.0

**Deprecated since:** -1

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2InlineStyleOptions-onChange?: OnInlineCounterV2Change--><!--Device-CounterV2InlineStyleOptions-onChange?: OnInlineCounterV2Change-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textWidth

```TypeScript
textWidth?: number
```

Set text width of the counter component, ranges greater than or equal to 0. If undefined is passed, the text width will adapt to the text content.

**Type:** number

**Default:** undefined

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2InlineStyleOptions-textWidth?: double--><!--Device-CounterV2InlineStyleOptions-textWidth?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: number
```

Set initial value of the counter component, ranges from min to max.

**Type:** number

**Default:** 0

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2InlineStyleOptions-value?: int--><!--Device-CounterV2InlineStyleOptions-value?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
