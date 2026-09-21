# Radio

The **Radio** component allows users to select from a set of mutually exclusive options.

> **NOTE** > > Since API version 12, the default indicator type for the **Radio** component changes from > **RadioIndicatorType.DOT** to **RadioIndicatorType.TICK**.

## Child Components

Not supported

## Radio

```TypeScript
Radio(options: RadioOptions)
```

Creates a radio button.

**Since:** 8

**Model restriction:** This API can be used in both the stage model and FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RadioOptions](arkts-arkui-radio-comp-radiooptions-i.md) | Yes | Parameters of the radio button. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [RadioConfiguration](arkts-arkui-radio-comp-radioconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. Inherits from [CommonConfiguration](arkts-arkui-common-comp-commonconfiguration-i.md). |
| [RadioOptions](arkts-arkui-radio-comp-radiooptions-i.md) | Radio button information. |
| [RadioStyle](arkts-arkui-radio-comp-radiostyle-i.md) | Radio button color. |

### Types

| Name | Description |
| --- | --- |
| [OnRadioChangeCallback](arkts-arkui-radio-comp-onradiochangecallback-t.md) | Defines the callback type for radio button selected state changes. |

### Enums

| Name | Description |
| --- | --- |
| [RadioIndicatorType](arkts-arkui-radio-comp-radioindicatortype-e.md) | Radio button style. |

## Examples

```TypeScript
### Example 1: Setting the Background Color

This example customizes the background color of the radio button by configuring checkedBackgroundColor.


```

```TypeScript
### Example 2: Setting the Indicator Type

This example customizes the selected style by configuring indicatorType and indicatorBuilder.


```

```TypeScript
### Example 3: Implementing a Custom Radio Button

This example illustrates how to implement a custom radio button using the contentModifier API.
```
