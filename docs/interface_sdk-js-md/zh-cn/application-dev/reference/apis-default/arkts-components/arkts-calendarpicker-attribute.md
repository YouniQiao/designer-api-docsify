# CalendarPickerAttribute

除支持通用属性外，还支持以下属性：

除支持通用事件，还支持以下事件：

@extends CommonMethod @interface CalendarPickerAttribute

**继承/实现关系：** CalendarPickerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface CalendarPickerAttribute--><!--Device-unnamed-export declare interface CalendarPickerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<CalendarPickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CalendarPickerAttribute-attributeModifier(modifier: AttributeModifier<CalendarPickerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CalendarPickerAttribute-attributeModifier(modifier: AttributeModifier<CalendarPickerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CalendarPickerAttribute](arkts-calendarpicker-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## edgeAlign

```TypeScript
edgeAlign(alignType: CalendarAlign | undefined, offset?: Offset): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CalendarPickerAttribute-edgeAlign(alignType: CalendarAlign | undefined, offset?: Offset): this--><!--Device-CalendarPickerAttribute-edgeAlign(alignType: CalendarAlign | undefined, offset?: Offset): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | [CalendarAlign](arkts-calendarpicker-calendaralign-e.md) \| undefined | 是 |  |
| offset | [Offset](../../apis-arkui/arkts-apis/arkts-arkui-offset-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## markToday

```TypeScript
markToday(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CalendarPickerAttribute-markToday(enabled: boolean | undefined): this--><!--Device-CalendarPickerAttribute-markToday(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onChange

```TypeScript
onChange(callback: Callback<Date> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CalendarPickerAttribute-onChange(callback: Callback<Date> | undefined): this--><!--Device-CalendarPickerAttribute-onChange(callback: Callback<Date> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;Date&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## textStyle

```TypeScript
textStyle(value: PickerTextStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CalendarPickerAttribute-textStyle(value: PickerTextStyle | undefined): this--><!--Device-CalendarPickerAttribute-textStyle(value: PickerTextStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置属性修改器。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CalendarPickerAttribute-default--><!--Device-CalendarPickerAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

