# @ohos.arkui.advanced.Counter

## Modules to Import

```TypeScript
import { CounterComponent, CounterOptions, CounterType, DateData } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [CommonOptions](arkts-arkui-arkui-advanced-counter-commonoptions-c.md) | Defines the common attributes and events of the **Counter** component. |
| [CounterOptions](arkts-arkui-arkui-advanced-counter-counteroptions-c.md) | Defines the type and style of the **Counter** component. |
| [DateData](arkts-arkui-arkui-advanced-counter-datedata-c.md) | Defines date attributes and methods, including year, month, and day. |
| [DateStyleOptions](arkts-arkui-arkui-advanced-counter-datestyleoptions-c.md) | Defines the attributes and events of the inline date counter. |
| [InlineStyleOptions](arkts-arkui-arkui-advanced-counter-inlinestyleoptions-c.md) | Defines the inline numeric counter attributes and events. |
| [NumberStyleOptions](arkts-arkui-arkui-advanced-counter-numberstyleoptions-c.md) | Defines the list and compact counter attributes and events. |

### Structs

| Name | Description |
| --- | --- |
| [CounterComponent](arkts-arkui-arkui-advanced-counter-countercomponent-s.md) | The **Counter** component is used for precise numerical value adjustment. It supports four styles: list, compact, inline numeric, and inline date, and is suitable for scenarios such as shopping quantity adjustment, parameter setting, and date selection. It provides flexible style configuration and event callback capabilities. |

### Enums

| Name | Description |
| --- | --- |
| [CounterType](arkts-arkui-arkui-advanced-counter-countertype-e.md) | Enumerates counter types. |

## Examples

```TypeScript
### Example 1: Implementing a List Counter

This example implements a list counter by setting type to CounterType.LIST and configuring numberOptions.


```

```TypeScript
### Example 2: Implementing a Compact Counter

This example implements a compact counter by setting type to CounterType.COMPACT and configuring numberOptions.


```

```TypeScript
### Example 3: Implementing an Inline Numeric Counter

This example implements an inline numeric counter by setting type to CounterType.INLINE and configuring inlineOptions.


```

```TypeScript
### Example 4: Implementing an Inline Date Counter

This example implements an inline date counter by setting type to CounterType.INLINE_DATE and configuring dateOptions.


```

```TypeScript
### Example 5: Implementing a Mirrored Layout

This example sets the direction attribute to implement a mirrored layout for list, compact, inline numeric, and inline date counters.
```
