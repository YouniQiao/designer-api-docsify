# SecurityComponentMethod

The universal attributes module for security components enables unified configuration of universal attributes such as layout, size, text, icon, color, border, and interaction behaviors.

This module is mainly used in the following scenarios:  
- Set layout, size, text, icon, color, border, and interaction-related attributes for security components  
such as [PasteButton](./paste_button) and [SaveButton](./save_button).  
- Adjust the display effect and interaction experience of security components while ensuring compliance with  
the security component specifications. For specific constraints,see [Constraints](../../../security/AccessToken/security-component-overview.md#constraints).  
- Reuse the universal attribute capabilities of security components through chained calls.

## Key Enums

- [SecurityComponentLayoutDirection](arkts-arkui-securitycomponentlayoutdirection-e.md): Enumeration of icon and text  
layout directions for the security component. Specifies horizontal or vertical layout.  
- [ButtonType](../arkts-components/arkts-arkui-buttontype-e.md/arkts-arkui-buttontype-e.md): Enumeration of button styles for the security component.  
Specifies capsule, circle, rounded rectangle, or normal button style.

## Key APIs

- [SecurityComponentMethod](arkts-arkui-securitycomponentmethod-c.md): A collection of universal attribute methods for  
security components. Configures layout, size, text, icon, color, border, and interaction attributes for specific security components.

## Child Components

- Not supported

Defines the method of a security component.

**Since:** 10

<!--Device-unnamed-declare class SecurityComponentMethod<T>--><!--Device-unnamed-declare class SecurityComponentMethod<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityDefaultFocus

```TypeScript
accessibilityDefaultFocus(focus: boolean): T
```

Sets the initial focus for the screen reader on the page, specifying the component that the screen reader announces first after the page loads.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SecurityComponentMethod-accessibilityDefaultFocus(focus: boolean): T--><!--Device-SecurityComponentMethod-accessibilityDefaultFocus(focus: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| focus | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityDescription

```TypeScript
accessibilityDescription(description: string | Resource): T
```

Provides an accessibility description for the component. You can set detailed text descriptions to help users understand the component's functionality and the actions it will perform.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SecurityComponentMethod-accessibilityDescription(description: string | Resource): T--><!--Device-SecurityComponentMethod-accessibilityDescription(description: string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| description | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId(nextId: string): T
```

Specifies the next focus component for the screen reader.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SecurityComponentMethod-accessibilityNextFocusId(nextId: string): T--><!--Device-SecurityComponentMethod-accessibilityNextFocusId(nextId: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| nextId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityRole

```TypeScript
accessibilityRole(role: SecurityComponentRoleType): T
```

Sets the accessibility component type. Each component type is announced in a specific way. You can modify the component type based on your app's requirements to control how the component is announced and what content is announced in accessibility mode.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SecurityComponentMethod-accessibilityRole(role: SecurityComponentRoleType): T--><!--Device-SecurityComponentMethod-accessibilityRole(role: SecurityComponentRoleType): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| role | [SecurityComponentRoleType](arkts-arkui-securitycomponentroletype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## align

```TypeScript
align(alignType: Alignment): T
```

Sets the alignment of the icon and text on the security component.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SecurityComponentMethod-align(alignType: Alignment): T--><!--Device-SecurityComponentMethod-align(alignType: Alignment): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alignType | [Alignment](arkts-arkui-alignment-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## alignRules

```TypeScript
alignRules(alignRule: AlignRuleOption): T
```

Sets the alignment rules for child components within a relative container. This API takes effect only when the parent container is [RelativeContainer](./relative_container).

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SecurityComponentMethod-alignRules(alignRule: AlignRuleOption): T--><!--Device-SecurityComponentMethod-alignRules(alignRule: AlignRuleOption): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alignRule | [AlignRuleOption](../arkts-components/arkts-arkui-alignruleoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## alignRules

```TypeScript
alignRules(alignRule: LocalizedAlignRuleOptions): T
```

Sets the alignment rules for child components within a relative container. This API takes effect only when the parent container is [RelativeContainer](./relative_container). In the horizontal direction, this method replaces **left** and **right** in the [alignRules](arkts-arkui-securitycomponentmethod-c.md#alignrules) above with **start**and **end**, respectively, allowing the layout to be mirrored in RTL mode. You are advised to use this method preferentially.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SecurityComponentMethod-alignRules(alignRule: LocalizedAlignRuleOptions): T--><!--Device-SecurityComponentMethod-alignRules(alignRule: LocalizedAlignRuleOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alignRule | [LocalizedAlignRuleOptions](../arkts-components/arkts-arkui-localizedalignruleoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundColor

```TypeScript
backgroundColor(value: ResourceColor): T
```

Sets the background color of the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-backgroundColor(value: ResourceColor): T--><!--Device-SecurityComponentMethod-backgroundColor(value: ResourceColor): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderColor

```TypeScript
borderColor(value: ResourceColor): T
```

Sets the border color of the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-borderColor(value: ResourceColor): T--><!--Device-SecurityComponentMethod-borderColor(value: ResourceColor): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderRadius

```TypeScript
borderRadius(value: Dimension): T
```

Sets the border radius of the security component.

The effect of **borderRadius** is influenced by **ButtonType**. When **ButtonType** is **Capsule** or **Circle**,the **borderRadius** setting does not take effect, and the corner radius is automatically determined by the button type. When the **ButtonType** is **Normal** or **ROUNDED_RECTANGLE**, the **borderRadius** setting takes effect.For details, see [ButtonType](../arkts-components/arkts-arkui-buttontype-e.md/arkts-arkui-buttontype-e.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-borderRadius(value: Dimension): T--><!--Device-SecurityComponentMethod-borderRadius(value: Dimension): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderRadius

```TypeScript
borderRadius(radius: Dimension | BorderRadiuses): T
```

Sets the border radius of the security component, allowing individual setting of the four corner radii.

The effect of **borderRadius** is influenced by **ButtonType**. When **ButtonType** is **Capsule** or **Circle**,the **borderRadius** setting does not take effect, and the corner radius is automatically determined by the button type. When the **ButtonType** is **Normal** or **ROUNDED_RECTANGLE**, the **borderRadius** setting takes effect.For details, see [ButtonType](../arkts-components/arkts-arkui-buttontype-e.md/arkts-arkui-buttontype-e.md).

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SecurityComponentMethod-borderRadius(radius: Dimension | BorderRadiuses): T--><!--Device-SecurityComponentMethod-borderRadius(radius: Dimension | BorderRadiuses): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | [Dimension](arkts-arkui-dimension-t.md) \| [BorderRadiuses](arkts-arkui-units-borderradiuses-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderStyle

```TypeScript
borderStyle(value: BorderStyle): T
```

Sets the border style of the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-borderStyle(value: BorderStyle): T--><!--Device-SecurityComponentMethod-borderStyle(value: BorderStyle): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BorderStyle](arkts-arkui-borderstyle-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderWidth

```TypeScript
borderWidth(value: Dimension): T
```

Sets the border width of the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-borderWidth(value: Dimension): T--><!--Device-SecurityComponentMethod-borderWidth(value: Dimension): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## chainMode

```TypeScript
chainMode(direction: Axis, style: ChainStyle): T
```

Sets the parameters of the chain in which the component is the head. This API takes effect only when the parent container is [RelativeContainer](./relative_container).

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SecurityComponentMethod-chainMode(direction: Axis, style: ChainStyle): T--><!--Device-SecurityComponentMethod-chainMode(direction: Axis, style: ChainStyle): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | [Axis](arkts-arkui-axis-e.md) | Yes |
| style | [ChainStyle](../arkts-components/arkts-arkui-chainstyle-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## constraintSize

```TypeScript
constraintSize(value: ConstraintSizeOptions): T
```

Sets the constraint size, limiting the size range during component layout.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SecurityComponentMethod-constraintSize(value: ConstraintSizeOptions): T--><!--Device-SecurityComponentMethod-constraintSize(value: ConstraintSizeOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ConstraintSizeOptions](arkts-arkui-constraintsizeoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## enabled

```TypeScript
enabled(respond: boolean): T
```

Sets whether the security component is interactive.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SecurityComponentMethod-enabled(respond: boolean): T--><!--Device-SecurityComponentMethod-enabled(respond: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| respond | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## fallbackLineSpacing

```TypeScript
fallbackLineSpacing(enabled: boolean): T
```

Enables adaptive line height based on the actual text height for multi-line text.

The **fallbackLineSpacing** attribute is closely coupled with the **lineHeight** attribute of  
[RichEditorTextStyle](../arkts-components/arkts-arkui-richeditortextstyle-i.md/arkts-arkui-richeditortextstyle-i.md). When the **lineHeight** value is less than the actual rendering height of the text at the current font size, the **fallbackLineSpacing** value determines whether the line height should adapt based on the actual text height.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SecurityComponentMethod-fallbackLineSpacing(enabled: boolean): T--><!--Device-SecurityComponentMethod-fallbackLineSpacing(enabled: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [enabled](#enabled) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## focusBox

```TypeScript
focusBox(style: FocusBoxStyle): T
```

Sets the style of the system focus box for the security component.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-SecurityComponentMethod-focusBox(style: FocusBoxStyle): T--><!--Device-SecurityComponentMethod-focusBox(style: FocusBoxStyle): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [FocusBoxStyle](arkts-arkui-focusboxstyle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## fontColor

```TypeScript
fontColor(value: ResourceColor): T
```

Sets the font color of the text on the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-fontColor(value: ResourceColor): T--><!--Device-SecurityComponentMethod-fontColor(value: ResourceColor): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## fontFamily

```TypeScript
fontFamily(value: string | Resource): T
```

Sets the font family of the text on the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-fontFamily(value: string | Resource): T--><!--Device-SecurityComponentMethod-fontFamily(value: string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## fontSize

```TypeScript
fontSize(value: Dimension): T
```

Sets the font size of the text for the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-fontSize(value: Dimension): T--><!--Device-SecurityComponentMethod-fontSize(value: Dimension): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## fontStyle

```TypeScript
fontStyle(value: FontStyle): T
```

Sets the font style of the text on the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-fontStyle(value: FontStyle): T--><!--Device-SecurityComponentMethod-fontStyle(value: FontStyle): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [FontStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontstyle-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## fontWeight

```TypeScript
fontWeight(value: number | FontWeight | string | Resource): T
```

Sets the font weight of the text on the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-fontWeight(value: number | FontWeight | string | Resource): T--><!--Device-SecurityComponentMethod-fontWeight(value: number | FontWeight | string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| FontWeight \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## height

```TypeScript
height(value: Length): T
```

Sets the height of the security component. If not set, the height adapts to the element content. When used in conjunction with adaptive font size attributes, the height setting affects whether the text is fully displayed.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SecurityComponentMethod-height(value: Length): T--><!--Device-SecurityComponentMethod-height(value: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## heightAdaptivePolicy

```TypeScript
heightAdaptivePolicy(policy: TextHeightAdaptivePolicy): T
```

Sets the method for text height adaptation. This is applicable to scenarios where the text display of a security component needs to be dynamically adjusted to ensure complete text visibility under different sizes or language environments.

The security component text is laid out at [maxFontSize](arkts-arkui-securitycomponentmethod-c.md#maxfontsize). If the text can be completely displayed and no adaptive adjustment is needed, this API does not take effect. Otherwise,adaptation proceeds according to the specified policy, as follows:&lt;br&gt;**TextHeightAdaptivePolicy.MAX_LINES_FIRST**: prioritizes the [maxLines](arkts-arkui-securitycomponentmethod-c.md#maxlines) attribute for adjusting the text height. If the layout size with **maxLines**exceeds the layout constraints, the security component attempts to reduce the font size within the range of  
[minFontSize](arkts-arkui-securitycomponentmethod-c.md#minfontsize) and  
[maxFontSize](arkts-arkui-securitycomponentmethod-c.md#maxfontsize) to fit more text. If the text still cannot be fully displayed, the security component adaptively adjusts its height to show all text.&lt;br&gt;**TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST**: prioritizes the  
[minFontSize](arkts-arkui-securitycomponentmethod-c.md#minfontsize) attribute for adjusting the text height. If the text can be laid out in a single line using **minFontSize**, the security component attempts to increase the font size within the range of **minFontSize** and [maxFontSize](arkts-arkui-securitycomponentmethod-c.md#maxfontsize) to use the largest possible font size. If the text cannot be laid out in a single line using **minFontSize**, the security component attempts to use the [maxLines](arkts-arkui-securitycomponentmethod-c.md#maxlines) attribute for layout. If the text still cannot be fully displayed, the security component adaptively adjusts its height to fully display the text.&lt;br&gt;**TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST**: prioritizes layout constraints for adjusting the text height.&lt;br&gt;If the layout size exceeds the constraints, the security component attempts to reduce the font size within the range of [minFontSize](arkts-arkui-securitycomponentmethod-c.md#minfontsize) and  
[maxFontSize](arkts-arkui-securitycomponentmethod-c.md#maxfontsize). If the layout size still exceeds the constraints after the font size is reduced to **minFontSize**, the security component truncates the excess lines. If the  
[maxLines](arkts-arkui-securitycomponentmethod-c.md#maxlines) attribute is set, the number of lines does not exceed the  
**maxLines** value (horizontal truncation may occur). If **maxLines** is not set, there is no limit on the number of lines.If the security component text is not fully displayed, clicking does not trigger authorization. Whether the text is fully displayed depends on attributes such as **heightAdaptivePolicy**, **minFontSize**, **maxFontSize**,  
**maxLines**, **width**, and **height**.For details, see [Example](../../../reference/apis-arkui/arkui-ts/ts-securitycomponent-attributes.md#example-3)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SecurityComponentMethod-heightAdaptivePolicy(policy: TextHeightAdaptivePolicy): T--><!--Device-SecurityComponentMethod-heightAdaptivePolicy(policy: TextHeightAdaptivePolicy): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policy | [TextHeightAdaptivePolicy](arkts-arkui-textheightadaptivepolicy-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## iconColor

```TypeScript
iconColor(value: ResourceColor): T
```

Sets the icon color of the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-iconColor(value: ResourceColor): T--><!--Device-SecurityComponentMethod-iconColor(value: ResourceColor): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## iconSize

```TypeScript
iconSize(value: Dimension): T
```

Sets the icon size of the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-iconSize(value: Dimension): T--><!--Device-SecurityComponentMethod-iconSize(value: Dimension): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## id

```TypeScript
id(id: string): T
```

Unique ID you assigned for the component.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SecurityComponentMethod-id(id: string): T--><!--Device-SecurityComponentMethod-id(id: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## layoutDirection

```TypeScript
layoutDirection(value: SecurityComponentLayoutDirection): T
```

Sets the layout direction of the icon and text on the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-layoutDirection(value: SecurityComponentLayoutDirection): T--><!--Device-SecurityComponentMethod-layoutDirection(value: SecurityComponentLayoutDirection): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SecurityComponentLayoutDirection](arkts-arkui-securitycomponentlayoutdirection-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## markAnchor

```TypeScript
markAnchor(value: Position): T
```

Sets the anchor of the security component for moving the component with its top-left corner as the reference point.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-markAnchor(value: Position): T--><!--Device-SecurityComponentMethod-markAnchor(value: Position): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Position](arkts-arkui-display-position-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## maxFontScale

```TypeScript
maxFontScale(scale: number | Resource): T
```

Sets the maximum font scale factor. When this API is invoked and the system font scaling causes the text to enlarge, the font scale factor will not exceed the set maximum scale factor.

This API can be used in conjunction with [minFontScale](arkts-arkui-securitycomponentmethod-c.md#minfontscale).  
**maxFontScale** controls the upper limit of the scale factor, and **minFontScale** controls the lower limit. They can be set independently or together to precisely control font scaling.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SecurityComponentMethod-maxFontScale(scale: number | Resource): T--><!--Device-SecurityComponentMethod-maxFontScale(scale: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## maxFontSize

```TypeScript
maxFontSize(maxSize: number | string | Resource): T
```

Sets the maximum font size for text display.

- When used in conjunction with [minFontSize](arkts-arkui-securitycomponentmethod-c.md#minfontsize) and  
[maxLines](arkts-arkui-securitycomponentmethod-c.md#maxlines), or in combination with layout size constraints, this attribute enables font size adaptation. Using this attribute alone will not take effect.  
- **maxFontSize** must be greater than **minFontSize**. If **maxFontSize** is less than **minFontSize**,  
**minFontSize** will be treated as **maxFontSize**.  
- When adaptive font size is effective, the **fontSize** setting does not take effect.  
- If the security component text is not fully displayed, clicking does not trigger authorization. The  
**maxFontSize** setting affects text visibility, which in turn affects authorization behavior.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SecurityComponentMethod-maxFontSize(maxSize: number | string | Resource): T--><!--Device-SecurityComponentMethod-maxFontSize(maxSize: number | string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxSize | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## maxLines

```TypeScript
maxLines(line: number | Resource): T
```

Sets the maximum number of lines for text. By default, text wraps automatically. When this attribute is specified,the text will display at most the specified number of lines. It can be used independently to limit text lines, or in conjunction with [minFontSize](arkts-arkui-securitycomponentmethod-c.md#minfontsize),  
[maxFontSize](arkts-arkui-securitycomponentmethod-c.md#maxfontsize), and  
[heightAdaptivePolicy](arkts-arkui-securitycomponentmethod-c.md#heightadaptivepolicy). When used with adaptive font size attributes, if the security component text is not fully displayed, the click will not trigger authorization. The  
**maxLines** setting affects whether the text can be fully displayed, thereby affecting the authorization behavior of the security component.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SecurityComponentMethod-maxLines(line: number | Resource): T--><!--Device-SecurityComponentMethod-maxLines(line: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| line | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## minFontScale

```TypeScript
minFontScale(scale: number | Resource): T
```

Sets the minimum font scale factor for the text. When this API is invoked and the system font scaling causes the text to shrink, the font scale factor will not fall below the set minimum scale factor.

This API can be used in conjunction with [maxFontScale](arkts-arkui-securitycomponentmethod-c.md#maxfontscale).  
**minFontScale** controls the lower limit of the scale factor and **maxFontScale** controls the upper limit. They can be set independently or together to precisely control font scaling.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SecurityComponentMethod-minFontScale(scale: number | Resource): T--><!--Device-SecurityComponentMethod-minFontScale(scale: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## minFontSize

```TypeScript
minFontSize(minSize: number | string | Resource): T
```

Sets the minimum font size for text display.

- When used in conjunction with [maxFontSize](arkts-arkui-securitycomponentmethod-c.md#maxfontsize) and  
[maxLines](arkts-arkui-securitycomponentmethod-c.md#maxlines), or in combination with layout size constraints, this attribute enables font size adaptation. Using this attribute alone will not take effect.  
- **minFontSize** must be smaller than **maxFontSize**. If the set value is greater than **maxFontSize**,  
**maxFontSize** is used instead.  
- When **minFontSize** is less than or equal to 0, adaptive font size does not take effect.  
- When adaptive font size is effective, the **fontSize** setting does not take effect.  
- If the security component text is not fully displayed, clicking does not trigger authorization. The  
**minFontSize** setting affects text visibility, which in turn affects authorization behavior.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SecurityComponentMethod-minFontSize(minSize: number | string | Resource): T--><!--Device-SecurityComponentMethod-minFontSize(minSize: number | string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| minSize | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## offset

```TypeScript
offset(value: Position | Edges | LocalizedEdges): T
```

Sets the coordinate offset of the security component relative to its own layout position.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-offset(value: Position | Edges | LocalizedEdges): T--><!--Device-SecurityComponentMethod-offset(value: Position | Edges | LocalizedEdges): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Position](arkts-arkui-display-position-i.md) \| Edges \| [LocalizedEdges](arkts-arkui-localizededges-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## padding

```TypeScript
padding(value: Padding | Dimension): T
```

Sets the padding of the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-padding(value: Padding | Dimension): T--><!--Device-SecurityComponentMethod-padding(value: Padding | Dimension): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Padding \| [Dimension](arkts-arkui-dimension-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## position

```TypeScript
position(value: Position): T
```

Sets the absolute position, which is the offset of the top-left corner of the security component relative to the top-left corner of the parent container.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-position(value: Position): T--><!--Device-SecurityComponentMethod-position(value: Position): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Position](arkts-arkui-display-position-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## size

```TypeScript
size(value: SizeOptions): T
```

Sets the width and height. If not set, the width and height adapt to the element content. The **size** method is used to set both width and height at the same time. To set the width or height individually, use the  
[width](arkts-arkui-securitycomponentmethod-c.md#width) or [height](arkts-arkui-securitycomponentmethod-c.md#height) method.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SecurityComponentMethod-size(value: SizeOptions): T--><!--Device-SecurityComponentMethod-size(value: SizeOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## textIconSpace

```TypeScript
textIconSpace(value: Dimension): T
```

Sets the spacing between the icon and text in the security component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecurityComponentMethod-textIconSpace(value: Dimension): T--><!--Device-SecurityComponentMethod-textIconSpace(value: Dimension): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## width

```TypeScript
width(value: Length): T
```

Sets the width of the security component. If not set, the width adapts to the element content. When used in conjunction with adaptive font size attributes, the width setting affects whether the text is fully displayed.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SecurityComponentMethod-width(value: Length): T--><!--Device-SecurityComponentMethod-width(value: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
