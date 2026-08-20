# Button

The **Button** component can be used to create different types of buttons.

> **NOTE**

## Child Components

This component can contain only one child component.

## Button

```TypeScript
Button()
```

Creates an empty button.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonInterface-(): ButtonAttribute--><!--Device-ButtonInterface-(): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Button

```TypeScript
Button(options: ButtonOptions)
```

Creates a button that can contain a single child component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonInterface-(options: ButtonOptions): ButtonAttribute--><!--Device-ButtonInterface-(options: ButtonOptions): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ButtonOptions](arkts-arkui-buttonoptions-i.md) | Yes | Button settings. |

## Button

```TypeScript
Button(label: ResourceStr, options?: ButtonOptions)
```

Creates a button based on text content. In this case, the component cannot contain child components.

By default, the text content is displayed in a one line.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonInterface-(label: ResourceStr, options?: ButtonOptions): ButtonAttribute--><!--Device-ButtonInterface-(label: ResourceStr, options?: ButtonOptions): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | ResourceStr | Yes | Button text.<br>Note: If the text is longer than the width of the button, it is truncated. |
| options | [ButtonOptions](arkts-arkui-buttonoptions-i.md) | No | Button settings. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |

### Types

| Name | Description |
| --- | --- |

### Enums

| Name | Description |
| --- | --- |

