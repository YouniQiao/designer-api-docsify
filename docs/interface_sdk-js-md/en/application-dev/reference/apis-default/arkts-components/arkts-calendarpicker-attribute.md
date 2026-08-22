# CalendarPickerAttribute

Defines the CalendarPicker component attribute functions.

@extends CommonMethod @interface CalendarPickerAttribute

**Inheritance/Implementation:** CalendarPickerAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface CalendarPickerAttribute--><!--Device-unnamed-export declare interface CalendarPickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<CalendarPickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CalendarPickerAttribute-attributeModifier(modifier: AttributeModifier<CalendarPickerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CalendarPickerAttribute-attributeModifier(modifier: AttributeModifier<CalendarPickerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CalendarPickerAttribute](arkts-calendarpicker-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## edgeAlign

```TypeScript
edgeAlign(alignType: CalendarAlign | undefined, offset?: Offset): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CalendarPickerAttribute-edgeAlign(alignType: CalendarAlign | undefined, offset?: Offset): this--><!--Device-CalendarPickerAttribute-edgeAlign(alignType: CalendarAlign | undefined, offset?: Offset): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alignType | [CalendarAlign](arkts-calendarpicker-calendaralign-e.md) \| undefined | Yes |  |
| offset | [Offset](../../apis-arkui/arkts-apis/arkts-arkui-offset-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## markToday

```TypeScript
markToday(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CalendarPickerAttribute-markToday(enabled: boolean | undefined): this--><!--Device-CalendarPickerAttribute-markToday(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onChange

```TypeScript
onChange(callback: Callback<Date> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CalendarPickerAttribute-onChange(callback: Callback<Date> | undefined): this--><!--Device-CalendarPickerAttribute-onChange(callback: Callback<Date> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;Date&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setCalendarPickerOptions

```TypeScript
setCalendarPickerOptions(options?: CalendarOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CalendarPickerAttribute-setCalendarPickerOptions(options?: CalendarOptions): this--><!--Device-CalendarPickerAttribute-setCalendarPickerOptions(options?: CalendarOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CalendarOptions](arkts-calendarpicker-calendaroptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## textStyle

```TypeScript
textStyle(value: PickerTextStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CalendarPickerAttribute-textStyle(value: PickerTextStyle | undefined): this--><!--Device-CalendarPickerAttribute-textStyle(value: PickerTextStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CalendarPickerAttribute-default--><!--Device-CalendarPickerAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

