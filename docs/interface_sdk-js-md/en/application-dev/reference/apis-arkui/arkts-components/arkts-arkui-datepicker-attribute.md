# DatePicker properties/events

In addition to the universal attributes, the following attributes are supported.In addition to the universal events, the following events are supported.@extends CommonMethod [since 8 - 10] @extends CommonMethod&lt;DatePickerAttribute&gt; [since 11]

**Inheritance/Implementation:** DatePickerAttribute extends CommonMethod<DatePickerAttribute>

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## canLoop

```TypeScript
canLoop(isLoop: Optional<boolean>)
```

Sets whether to enable cyclic scrolling.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isLoop | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether to enable cyclic scrolling.   - **true**: Cyclic scrolling is enabled, where the year values increment or decrement with month cycling, and month values increment or decrement with day cycling.   - **false**: Cyclic scrolling is disabled, preventing out-of-bounds scrolling in year, month, and day columns and cross-column value synchronization.   Default value: **true**.If the value of **isLoop** is **undefined**, the default value is used. |

## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)
```

Sets the sensitivity to the digital crown rotation.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensitivity | [Optional](arkts-arkui-optional-t.md)&lt;[CrownSensitivity](../arkts-apis/arkts-arkui-crownsensitivity-e.md)&gt; | Yes | Sensitivity to the digital crown rotation.Default value: **CrownSensitivity.MEDIUM |

## disappearTextStyle

```TypeScript
disappearTextStyle(value: PickerTextStyle)
```

Sets the text style for edge items (the second item above or below the selected item).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](arkts-arkui-pickertextstyle-i.md) | Yes | Text color, font size, and font weight for edge items.Default value:{color: '#ff182431',font: {size: '14fp', weight: FontWeight.Regular}} |

## disappearTextStyle

```TypeScript
disappearTextStyle(style: Optional<PickerTextStyle>)
```

Sets the text style for edge items (the second item above or below the selected item). Compared to [disappearTextStyle&lt;sup&gt;10+&lt;/sup&gt;](#disappeartextstyle), this API supports the **undefined** type for the **style** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[PickerTextStyle](arkts-arkui-pickertextstyle-i.md)&gt; | Yes | Text color, font size, and font weight for edge items.Default value:{color: '#ff182431',font: {size: '14fp', weight: FontWeight.Regular}}If the value of **style** is **undefined**, the default value is used. |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(enable: Optional<boolean>)
```

Sets whether to enable haptic feedback.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether to enable haptic feedback.   - **true**: Enable haptic feedback.  - **false**: Disable haptic feedback.   Default value: **true**.Whether this parameter takes effect after being set to **true** depends on hardware support.If the value of **enable** is **undefined**, the default value is used. |

## lunar

```TypeScript
lunar(value: boolean)
```

Sets whether to display dates in lunar calendar format.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to display dates in lunar calendar format.   - **true**: Display dates in lunar calendar format.   - **false**: Do not display dates in lunar calendar format.   Default value: **false |

## lunar

```TypeScript
lunar(isLunar: Optional<boolean>)
```

Sets whether to display dates in lunar calendar format. Compared to [lunar](#lunar), the **isLunar** parameter supports the **undefined** type.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isLunar | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether to display dates in lunar calendar format.   - **true**: Display dates in lunar calendar format.   - **false**: Do not display dates in lunar calendar format.   Default value: **false**If the value of **isLunar** is **undefined**, the default value is used. |

## onChange

```TypeScript
onChange(callback: (value: DatePickerResult) => void)
```

Triggered when the date picker snaps to the selected item. This event cannot be triggered by two-way bound state variables.This API is supported since API version 8 and deprecated since API version 10. You are advised to use [onDateChange](#ondatechange) instead.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** [onDateChange](#ondatechange)(callback: Callback&lt;Date&gt;)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (value: DatePickerResult) = & gt; void | Yes | Selected time. |

## onDateChange

```TypeScript
onDateChange(callback: Callback<Date>)
```

Triggered when the date picker snaps to the selected item. This event cannot be triggered by two-way bound state variables.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback & lt;Date & gt; | Yes | Selected date, where the year, month, and day portions are subject to the selection, the hour and minute portions are subject to the current system time, and the second portion is always **00**.<br>**Since:** 18 |

## onDateChange

```TypeScript
onDateChange(callback: Optional<Callback<Date>>)
```

Triggered when the date picker snaps to the selected item. This event cannot be triggered by two-way bound state variables. Compared to [onDateChange&lt;sup&gt;10+&lt;/sup&gt;](#ondatechange), this API supports the **undefined** type for the **callback** parameter.

> **NOTE：**
> 
> This API can be called within attributeModifier since API version 20.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Optional](arkts-arkui-optional-t.md)&lt;Callback&lt;Date&gt;&gt; | Yes | Selected date, where the year, month, and day portions are subject to the selection, the hour and minute portions are subject to the current system time, and the second portion is always **00**.If **callback** is set to **undefined**, the callback function is not used. |

## selectedTextStyle

```TypeScript
selectedTextStyle(value: PickerTextStyle)
```

Sets the text style for the selected item.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](arkts-arkui-pickertextstyle-i.md) | Yes | Font color, font size, and font weight of the selected item.Default value:{color: '#ff007dff',font: {size: '20fp', weight: FontWeight.Medium}} |

## selectedTextStyle

```TypeScript
selectedTextStyle(style: Optional<PickerTextStyle>)
```

Sets the text style for the selected item. Compared to [selectedTextStyle&lt;sup&gt;10+&lt;/sup&gt;](#selectedtextstyle), this API supports the **undefined** type for the **style** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[PickerTextStyle](arkts-arkui-pickertextstyle-i.md)&gt; | Yes | Font color, font size, and font weight of the selected item.Default value:{color: '#ff007dff',font: {size: '20fp', weight: FontWeight.Medium}}If the value of **style** is **undefined**, the default value is used. |

## textStyle

```TypeScript
textStyle(value: PickerTextStyle)
```

Sets the text style for candidate items (the first item immediately above or below the selected item).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](arkts-arkui-pickertextstyle-i.md) | Yes | Text color, font size, and font weight for candidate items.Default value:{color: '#ff182431',font: {size: '16fp', weight: FontWeight.Regular}} |

## textStyle

```TypeScript
textStyle(style: Optional<PickerTextStyle>)
```

Sets the text style for candidate items (the first item immediately above or below the selected item). Compared to [textStyle&lt;sup&gt;10+&lt;/sup&gt;](#textstyle), this API supports the **undefined** type for the **style** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[PickerTextStyle](arkts-arkui-pickertextstyle-i.md)&gt; | Yes | Text color, font size, and font weight for candidate items.Default value:{color: '#ff182431',font: {size: '16fp', weight: FontWeight.Regular}}If the value of **style** is **undefined**, the default value is used. |
