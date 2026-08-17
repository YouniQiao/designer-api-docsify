# CounterV2CommonOptions

Defines the common options.

**Since:** 26.0.0

<!--Device-unnamed-declare class CounterV2CommonOptions--><!--Device-unnamed-declare class CounterV2CommonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { CounterV2Component } from 'CounterV2Component';
import { CounterV2Options } from 'CounterV2Options';
import { CounterV2DateData } from 'CounterV2DateData';
import { CounterV2Type } from 'CounterV2Type';
```

## focusable

```TypeScript
focusable?: boolean
```

Set the focusable of the counter component.

**Type:** boolean

**Default:** true

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2CommonOptions-focusable?: boolean--><!--Device-CounterV2CommonOptions-focusable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHoverDecrease

```TypeScript
onHoverDecrease?: OnCounterV2HoverCallback
```

Trigger a mouse hover event at the decrease button.

**Type:** [OnCounterV2HoverCallback](arkts-arkui-oncounterv2hovercallback-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2CommonOptions-onHoverDecrease?: OnCounterV2HoverCallback--><!--Device-CounterV2CommonOptions-onHoverDecrease?: OnCounterV2HoverCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHoverIncrease

```TypeScript
onHoverIncrease?: OnCounterV2HoverCallback
```

Trigger a mouse hover event at the increase button.

**Type:** [OnCounterV2HoverCallback](arkts-arkui-oncounterv2hovercallback-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2CommonOptions-onHoverIncrease?: OnCounterV2HoverCallback--><!--Device-CounterV2CommonOptions-onHoverIncrease?: OnCounterV2HoverCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## step

```TypeScript
step?: int
```

Set the step of the counter component, ranges greater than or equal to 1

**Type:** int

**Default:** 1

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CounterV2CommonOptions-step?: int--><!--Device-CounterV2CommonOptions-step?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

