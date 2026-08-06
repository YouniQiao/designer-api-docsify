# Text

The **Text** component is used to display a piece of textual information.

## Child Components

This component can contain the [Span]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, [ImageSpan]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_,  
[SymbolSpan]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, and [ContainerSpan]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ child components.
    **NOTE**  
    
    Use \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ to  
    implement \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ scenarios.

## Text

```TypeScript
Text(content?: string | Resource, value?: TextOptions)
```

Defines the constructor of Text.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextInterface-(content?: string | Resource, value?: TextOptions): TextAttribute--><!--Device-TextInterface-(content?: string | Resource, value?: TextOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string \| Resource | No | Plain text. This parameter takes effect when the child component [Span]\_\_\_JSDOC\_LINK\_USD\_0\_\_\_ is not included and [styled string]\_\_\_JSDOC\_LINK\_USD\_1\_\_\_ is not set.\_\_\_HTML\_TAG\_USD\_2\_\_\_Default value: **' '**\_\_\_HTML\_TAG\_USD\_3\_\_\_**NOTE**\_\_\_HTML\_TAG\_USD\_4\_\_\_Priority of displayed content: Styled string > Content of the **Span** component > Text content of the **Text** component.  |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Initialization options of the component. |

## Summary

