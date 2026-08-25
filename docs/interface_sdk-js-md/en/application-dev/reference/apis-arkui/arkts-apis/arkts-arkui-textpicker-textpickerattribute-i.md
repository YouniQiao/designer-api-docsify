# TextPickerAttribute

Defines the TextPicker component attributes.@extends CommonMethod @interface TextPickerAttribute

**Inheritance/Implementation:** TextPickerAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextPickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## canLoop

```TypeScript
default canLoop(value: boolean | undefined): this
```

Sets whether scrolling is loopable.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## defaultPickerItemHeight

```TypeScript
default defaultPickerItemHeight(value: double | string | undefined): this
```

Sets the height of each item in the picker.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## defaultTextStyle

```TypeScript
default defaultTextStyle(style: TextPickerTextStyle | undefined): this
```

Sets the style of the text items when the text style change animation during the scrolling process is disabled.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [TextPickerTextStyle](arkts-arkui-textpicker-textpickertextstyle-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

Sets the sensitivity to the digital crown rotation.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sensitivity | [CrownSensitivity](arkts-arkui-crownsensitivity-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## disableTextStyleAnimation

```TypeScript
default disableTextStyleAnimation(disabled: boolean | undefined): this
```

Sets whether to enable the text style change animation during the scrolling process.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| disabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## disappearTextStyle

```TypeScript
default disappearTextStyle(value: PickerTextStyle | TextPickerTextStyle | undefined): this
```

Sets the font color, font size, and font weight for the top and bottom items.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md) \| [TextPickerTextStyle](arkts-arkui-textpicker-textpickertextstyle-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## divider

```TypeScript
default divider(value: DividerOptions | null | undefined): this
```

Sets the divider style.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [DividerOptions](arkts-arkui-textpicker-divideroptions-i.md) \| null \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enable: boolean | undefined): this
```

Specifies whether to enable haptic feedback.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## gradientHeight

```TypeScript
default gradientHeight(value: Dimension | undefined): this
```

Sets the height for the fade effect. If this attribute is not set, the default fade effect is displayed.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Avoid changing the attribute data during the animation process of this component. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: OnTextPickerChangeCallback | undefined): this
```

Triggered when the text picker snaps to the selected item. Compared to onChange, this API supports the undefined type for the callback parameter.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnTextPickerChangeCallback](arkts-arkui-ontextpickerchangecallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## onEnterSelectedArea

```TypeScript
default onEnterSelectedArea(callback: TextPickerEnterSelectedAreaCallback | undefined): this
```

Triggered during the scrolling of the text picker when an item enters the divider area. When the picker contains text only or a combination of images and text, value indicates the text of the selected item. When the picker contains images only, value is empty.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [TextPickerEnterSelectedAreaCallback](arkts-arkui-textpickerenterselectedareacallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## onScrollStop

```TypeScript
default onScrollStop(callback: TextPickerScrollStopCallback | undefined): this
```

Triggered when the scrolling in the text picker stops. If the scrolling is initiated by a gesture, this event is triggered when the finger is lifted from the screen and the scrolling stops.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [TextPickerScrollStopCallback](arkts-arkui-textpickerscrollstopcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## selectedBackgroundStyle

```TypeScript
default selectedBackgroundStyle(style: PickerBackgroundStyle | undefined): this
```

Sets the background style of selected items.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [PickerBackgroundStyle](arkts-arkui-textpicker-pickerbackgroundstyle-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## selectedIndex

```TypeScript
default selectedIndex(value: int | int[] | undefined): this
```

Sets the index of the default selected item in the array. Its priority is higher than that of the selected value in options. For a single-column picker, use a value of the int type. For a multi-column (linked) picker, use a value of the int[] type.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| int[] \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## selectedTextStyle

```TypeScript
default selectedTextStyle(value: PickerTextStyle | TextPickerTextStyle | undefined): this
```

Sets the font color, font size, and font weight for the selected item.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md) \| [TextPickerTextStyle](arkts-arkui-textpicker-textpickertextstyle-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## setTextPickerOptions

```TypeScript
default setTextPickerOptions(options?: TextPickerOptions): this
```

Sets the text picker options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TextPickerOptions](arkts-arkui-textpicker-textpickeroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |

## textStyle

```TypeScript
default textStyle(value: PickerTextStyle | TextPickerTextStyle | undefined): this
```

Sets the font color, font size, and font weight for all items except the top, bottom, and selected items.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md) \| [TextPickerTextStyle](arkts-arkui-textpicker-textpickertextstyle-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) |
