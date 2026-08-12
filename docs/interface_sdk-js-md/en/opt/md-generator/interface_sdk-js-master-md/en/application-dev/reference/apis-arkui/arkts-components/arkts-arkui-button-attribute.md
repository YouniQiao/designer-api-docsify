# Button properties/events

In addition to the [universal attributes](common), the following attributes are supported.

The [universal events](common) are supported.

**Inheritance/Implementation:** ButtonAttribute extends [CommonMethod<ButtonAttribute>](CommonMethod<ButtonAttribute>)

**Since:** 7

<!--Device-unnamed-declare class ButtonAttribute extends CommonMethod<ButtonAttribute>--><!--Device-unnamed-declare class ButtonAttribute extends CommonMethod<ButtonAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonStyle

```TypeScript
buttonStyle(value: ButtonStyleMode)
```

Sets the style and primacy for the button. The system automatically adjusts the button background color and text color based on the enumerated value. You can also use the   
[backgroundColor](CommonMethod#backgroundColor(value: ResourceColor)),   
[fontColor](ButtonAttribute#fontColor), and [role](ButtonAttribute#role) APIs to set the background color and text color. The actual displayed effect will be determined by the last setting.

> **NOTE：**
> 
> This API can be called within [attributeModifier](CommonMethod#attributeModifier) since API version 12.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-ButtonAttribute-buttonStyle(value: ButtonStyleMode): ButtonAttribute--><!--Device-ButtonAttribute-buttonStyle(value: ButtonStyleMode): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ButtonStyleMode](arkts-arkui-buttonstylemode-e.md) | Yes |

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<ButtonConfiguration>)
```

Creates a content modifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ButtonAttribute-contentModifier(modifier: ContentModifier<ButtonConfiguration>): ButtonAttribute--><!--Device-ButtonAttribute-contentModifier(modifier: ContentModifier<ButtonConfiguration>): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[ButtonConfiguration](arkts-arkui-buttonconfiguration-i.md)&gt; | Yes |

## controlSize

```TypeScript
controlSize(value: ControlSize)
```

Sets the size for the button.

> **NOTE：**
> 
> This API can be called within [attributeModifier](CommonMethod#attributeModifier) since API version 12.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-ButtonAttribute-controlSize(value: ControlSize): ButtonAttribute--><!--Device-ButtonAttribute-controlSize(value: ControlSize): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ControlSize](arkts-arkui-controlsize-e.md) | Yes |

## fontColor

```TypeScript
fontColor(value: ResourceColor)
```

Sets the font color for the button.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonAttribute-fontColor(value: ResourceColor): ButtonAttribute--><!--Device-ButtonAttribute-fontColor(value: ResourceColor): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## fontFamily

```TypeScript
fontFamily(value: string | Resource)
```

Sets the font family.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonAttribute-fontFamily(value: string | Resource): ButtonAttribute--><!--Device-ButtonAttribute-fontFamily(value: string | Resource): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## fontSize

```TypeScript
fontSize(value: Length)
```

Sets the font size for the button.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonAttribute-fontSize(value: Length): ButtonAttribute--><!--Device-ButtonAttribute-fontSize(value: Length): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## fontStyle

```TypeScript
fontStyle(value: FontStyle)
```

Sets the font style for the button.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonAttribute-fontStyle(value: FontStyle): ButtonAttribute--><!--Device-ButtonAttribute-fontStyle(value: FontStyle): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [FontStyle](#fontstyle) | Yes |

## fontWeight

```TypeScript
fontWeight(value: number | FontWeight | string)
```

Sets the font weight for the button.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonAttribute-fontWeight(value: number | FontWeight | string): ButtonAttribute--><!--Device-ButtonAttribute-fontWeight(value: number | FontWeight | string): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| FontWeight \| string | Yes |

## labelStyle

```TypeScript
labelStyle(value: LabelStyle)
```

Sets the label style for the button.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ButtonAttribute-labelStyle(value: LabelStyle): ButtonAttribute--><!--Device-ButtonAttribute-labelStyle(value: LabelStyle): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LabelStyle](arkts-arkui-labelstyle-i.md) | Yes |

## maxFontScale

```TypeScript
maxFontScale(scale: number | Resource)
```

Sets the maximum font scale factor for text.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ButtonAttribute-maxFontScale(scale: number | Resource): ButtonAttribute--><!--Device-ButtonAttribute-maxFontScale(scale: number | Resource): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## minFontScale

```TypeScript
minFontScale(scale: number | Resource)
```

Sets the minimum font scale factor for text.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ButtonAttribute-minFontScale(scale: number | Resource): ButtonAttribute--><!--Device-ButtonAttribute-minFontScale(scale: number | Resource): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## role

```TypeScript
role(value: ButtonRole)
```

Sets the role of the button. The system automatically adjusts the button background color and text color based on the enumerated value. You can also use the   
[backgroundColor](CommonMethod#backgroundColor(value: ResourceColor)),   
[fontColor](ButtonAttribute#fontColor), and [buttonStyle](ButtonAttribute#buttonStyle) APIs to set the background color and text color. The actual displayed effect will be determined by the last setting.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ButtonAttribute-role(value: ButtonRole): ButtonAttribute--><!--Device-ButtonAttribute-role(value: ButtonRole): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ButtonRole](arkts-arkui-buttonrole-e.md) | Yes |

## stateEffect

```TypeScript
stateEffect(value: boolean)
```

Specifies whether to enable the pressed state effect when the button is clicked.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonAttribute-stateEffect(value: boolean): ButtonAttribute--><!--Device-ButtonAttribute-stateEffect(value: boolean): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## type

```TypeScript
type(value: ButtonType)
```

Sets the button type.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonAttribute-type(value: ButtonType): ButtonAttribute--><!--Device-ButtonAttribute-type(value: ButtonType): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ButtonType](arkts-arkui-buttontype-e.md) | Yes |
