# TextClockAttribute

Defines the TextClock component attributes.

**Inheritance/Implementation:** TextClockAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextClockAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<TextClockConfiguration> | undefined): this
```

Set the content modifier of textclock.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[TextClockConfiguration](arkts-arkui-textclock-textclockconfiguration-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## dateTimeOptions

```TypeScript
default dateTimeOptions(dateTimeOptions: DateTimeOptions | undefined): this
```

Set hour format

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [dateTimeOptions](#datetimeoptions) | DateTimeOptions \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

Called when the value of TextClock fontColor is set

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: ResourceStr | undefined): this
```

Called when the value of TextClock fontFamily is set

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontFeature

```TypeScript
default fontFeature(value: string | undefined): this
```

Called when the text fontFeature is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| undefined | Yes | The fontFeature. normal \|  & lt;feature-tag-value & gt;, where & lt;feature-tag-value & gt; = & lt;string & gt; [ & lt;integer & gt; \ | on \|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: Length | undefined): this
```

Called when the value of TextClock fontSize is set

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontStyle

```TypeScript
default fontStyle(value: FontStyle | undefined): this
```

Called when the value of TextClock fontStyle is set

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [FontStyle](arkts-arkui-fontstyle-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | string | undefined): this
```

Called when the value of TextClock fontWeight is set

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| string \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## format

```TypeScript
default format(value: ResourceStr | undefined): this
```

set display time format,such as "yyyy/mm/dd","yyyy-mm-dd". support time format: yyyy,mm,mmm(English month abbreviation),mmmm(Full name of the month in English), dd,ddd(English Week abbreviation),dddd(Full name of the week in English), HH/hh(24-hour clock/12-hour clock),MM/mm(minute),SS/ss(second). The default value is "hh:mm:ss" when TextClock is not in a form. The default value is "hh:mm" when TextClock is in a form. If the value has second or millisecond, the value will be set to the default value.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## onDateChange

```TypeScript
default onDateChange(event: Callback<long> | undefined): this
```

Provides a date change callback. The callback parameter is Unix Time Stamp, The number of milliseconds that have elapsed since January 1, 1970 (UTC). The minimum callback interval for this event default is seconds when TextClock is not in a form. The minimum callback interval for this event is minutes when TextClock is in a form. If visibility is Hidden the callback be disabled when TextClock is in a form. You can listen to this callback, Use the format attribute method to customize data display in the callback.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;long&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## setTextClockOptions

```TypeScript
default setTextClockOptions(options?: TextClockOptions): this
```

Set TextClock options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TextClockOptions](arkts-arkui-textclock-textclockoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## textShadow

```TypeScript
default textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this
```

Called when the text shadow is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| Array&lt;[ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |
