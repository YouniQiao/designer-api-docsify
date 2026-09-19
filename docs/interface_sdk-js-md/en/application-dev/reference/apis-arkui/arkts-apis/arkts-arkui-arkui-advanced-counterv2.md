# @ohos.arkui.advanced.CounterV2

## Modules to Import

```TypeScript
import { CounterV2Component, CounterV2Options, CounterV2DateData, CounterV2Type } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [CounterV2CommonOptions](arkts-arkui-arkui-advanced-counterv2-counterv2commonoptions-c.md) | Defines the common attributes and events of the **CounterV2** component. |
| [CounterV2DateData](arkts-arkui-arkui-advanced-counterv2-counterv2datedata-c.md) | Defines common date attributes and methods, including year, month, and day. |
| [CounterV2DateStyleOptions](arkts-arkui-arkui-advanced-counterv2-counterv2datestyleoptions-c.md) | Defines the attributes and events of the inline date **CounterV2**. |
| [CounterV2InlineStyleOptions](arkts-arkui-arkui-advanced-counterv2-counterv2inlinestyleoptions-c.md) | Defines the attributes and events of the inline number **CounterV2**. |
| [CounterV2NumberStyleOptions](arkts-arkui-arkui-advanced-counterv2-counterv2numberstyleoptions-c.md) | Defines the attributes and events of the list and compact **CounterV2**. |
| [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md) | Defines the type and style of the **CounterV2** component. |

### Structs

| Name | Description |
| --- | --- |
| [CounterV2Component](arkts-arkui-arkui-advanced-counterv2-counterv2component-s.md) | The **CounterV2** component enables precise numeric value adjustment. It provides four types: list, compact, inline number, and inline date, which are applicable to scenarios such as shopping cart quantity adjustment and date selection. |

### Enums

| Name | Description |
| --- | --- |
| [CounterV2Type](arkts-arkui-arkui-advanced-counterv2-counterv2type-e.md) | Specifies the **CounterV2** type. |

### Types

| Name | Description |
| --- | --- |
| [OnCounterV2HoverCallback](arkts-arkui-oncounterv2hovercallback-t.md) | Defines the mouse hover callback type for the **CounterV2** component. |
| [OnDateCounterV2ChangeCallback](arkts-arkui-ondatecounterv2changecallback-t.md) | Defines the callback for date changes of the inline date **CounterV2**. |
| [OnInlineCounterV2Change](arkts-arkui-oninlinecounterv2change-t.md) | Defines the callback for the value change of the inline number **CounterV2**. |

## Examples

```TypeScript
### Example 1: List CounterV2

This example implements a list CounterV2 by setting [CounterV2Type](arkts-arkui-arkui-advanced-counterv2-counterv2type-e.md).LIST and the numberOptions attribute of [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md).

Since API version 26.0.0, [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md) supports the numberOptions attributes.


```

```TypeScript
### Example 2: Compact CounterV2

This example implements a compact CounterV2 by setting [CounterV2Type](arkts-arkui-arkui-advanced-counterv2-counterv2type-e.md).COMPACT and the numberOptions attributes of [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md).

Since API version 26.0.0, [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md) supports the numberOptions attribute.


```

```TypeScript
### Example 3: Inline Number CounterV2

This example implements an inline number CounterV2 by setting [CounterV2Type](arkts-arkui-arkui-advanced-counterv2-counterv2type-e.md).INLINE and the inlineOptions attribute of [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md).

Since API version 26.0.0, [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md) supports the inlineOptions attribute.


```

```TypeScript
### Example 4: Inline Date CounterV2

This example implements an inline date CounterV2 by setting [CounterV2Type](arkts-arkui-arkui-advanced-counterv2-counterv2type-e.md).INLINE_DATE and the dateOptions attribute of [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md).

Since API version 26.0.0, [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md) supports the dateOptions attribute.


```

```TypeScript
### Example 5: Mirrored Layout Display

This example uses the direction attribute of [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md) to implement mirrored layouts for the list, compact, inline number, and inline date CounterV2 components.

Since API version 26.0.0, [CounterV2Options](arkts-arkui-arkui-advanced-counterv2-counterv2options-c.md) supports the direction attribute.
```
