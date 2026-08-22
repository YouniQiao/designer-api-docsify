# SecurityComponentMethod

Declares the interface for the method of a security component.

@interface SecurityComponentMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface SecurityComponentMethod--><!--Device-unnamed-export declare interface SecurityComponentMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityDefaultFocus

```TypeScript
accessibilityDefaultFocus(focus: boolean | undefined): this
```

Sets the default focus flag of the accessibility feature.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-accessibilityDefaultFocus(focus: boolean | undefined): this--><!--Device-SecurityComponentMethod-accessibilityDefaultFocus(focus: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| focus | boolean \| undefined | Yes | Set to true if the component is the default accessibility focus. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attributes of the security component. |

## accessibilityDescription

```TypeScript
accessibilityDescription(description: string | Resource | undefined): this
```

Sets the accessibility description.

This property provides additional context or explanation for the component, helping users understand its actions or functions. <p>&lt;strong&gt;Note&lt;/strong&gt;: You can provide further explanation for the current component, such as the potential consequences of an operation, especially those not implicitly conveyed by the component's text or role type. If a component includes text information, a role type (other than ROLE_NONE), and an accessibility description, the system reads them when the component is selected.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-accessibilityDescription(description: string | Resource | undefined): this--><!--Device-SecurityComponentMethod-accessibilityDescription(description: string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| description | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes | Accessibility description. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attributes of the security component. |

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId(nextId: string | undefined): this
```

Sets the ID of the next component to receive accessibility focus.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-accessibilityNextFocusId(nextId: string | undefined): this--><!--Device-SecurityComponentMethod-accessibilityNextFocusId(nextId: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nextId | string \| undefined | Yes | ID of the next component to receive accessibility focus. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attributes of the security component. |

## accessibilityRole

```TypeScript
accessibilityRole(role: SecurityComponentRoleType | undefined): this
```

Sets the accessibility role, which represents the custom type of the component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-accessibilityRole(role: SecurityComponentRoleType | undefined): this--><!--Device-SecurityComponentMethod-accessibilityRole(role: SecurityComponentRoleType | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| role | [SecurityComponentRoleType](arkts-arkui-securitycomponent-securitycomponentroletype-e.md) \| undefined | Yes | Component type of the accessibility feature. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attributes of the security component. |

## align

```TypeScript
align(alignType: Alignment | undefined): this
```

align

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-align(alignType: Alignment | undefined): this--><!--Device-SecurityComponentMethod-align(alignType: Alignment | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alignType | [Alignment](arkts-arkui-alignment-e.md) \| undefined | Yes | Indicates the align type of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## alignRules

```TypeScript
alignRules(alignRule: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this
```

Specifies the alignRules of relative container

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-alignRules(alignRule: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this--><!--Device-SecurityComponentMethod-alignRules(alignRule: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alignRule | [AlignRuleOption](../arkts-components/arkts-arkui-alignruleoption-i.md) \| [LocalizedAlignRuleOptions](../arkts-components/arkts-arkui-localizedalignruleoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## backgroundColor

```TypeScript
backgroundColor(value: ResourceColor | undefined): this
```

Background color.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-backgroundColor(value: ResourceColor | undefined): this--><!--Device-SecurityComponentMethod-backgroundColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | Indicates the background color of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## borderColor

```TypeScript
borderColor(value: ResourceColor | undefined): this
```

Color of the border.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-borderColor(value: ResourceColor | undefined): this--><!--Device-SecurityComponentMethod-borderColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | Indicates the border color of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## borderRadius

```TypeScript
borderRadius(radius: Dimension | BorderRadiuses | undefined): this
```

Radius of the border.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-borderRadius(radius: Dimension | BorderRadiuses | undefined): this--><!--Device-SecurityComponentMethod-borderRadius(radius: Dimension | BorderRadiuses | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | [Dimension](arkts-arkui-dimension-t.md) \| [BorderRadiuses](arkts-arkui-borderradiuses-t.md) \| undefined | Yes | Indicates the border radius of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## borderStyle

```TypeScript
borderStyle(value: BorderStyle | undefined): this
```

Style of the border.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-borderStyle(value: BorderStyle | undefined): this--><!--Device-SecurityComponentMethod-borderStyle(value: BorderStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BorderStyle](arkts-arkui-borderstyle-e.md) \| undefined | Yes | Indicates the border style of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## borderWidth

```TypeScript
borderWidth(value: Dimension | undefined): this
```

Width of the border.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-borderWidth(value: Dimension | undefined): this--><!--Device-SecurityComponentMethod-borderWidth(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | Indicates the border width of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## chainMode

```TypeScript
chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this
```

Specifies the direction and style of chain in relative container

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this--><!--Device-SecurityComponentMethod-chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | [Axis](arkts-arkui-axis-e.md) \| undefined | Yes | Indicates direction of the chain |
| style | [ChainStyle](../arkts-components/arkts-arkui-chainstyle-e.md) \| undefined | Yes | Indicates style of the chain |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## constraintSize

```TypeScript
constraintSize(value: ConstraintSizeOptions | undefined): this
```

constraint Size: minWidth: minimum Width, maxWidth: maximum Width, minHeight: minimum Height, maxHeight: maximum Height.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-constraintSize(value: ConstraintSizeOptions | undefined): this--><!--Device-SecurityComponentMethod-constraintSize(value: ConstraintSizeOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ConstraintSizeOptions](arkts-arkui-constraintsizeoptions-i.md) \| undefined | Yes | Indicates the constraint size of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## enabled

```TypeScript
enabled(respond: boolean | undefined): this
```

If the value is true, the component is available and can respond to operations such as clicking. If it is set to false, click operations are not responded.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-enabled(respond: boolean | undefined): this--><!--Device-SecurityComponentMethod-enabled(respond: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| respond | boolean \| undefined | Yes | Indicates whether the button is responded to. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## fallbackLineSpacing

```TypeScript
fallbackLineSpacing(enabled: boolean | undefined): this
```

Whether to include the ascent and descent of fallback fonts to prevent line overlap.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-fallbackLineSpacing(enabled: boolean | undefined): this--><!--Device-SecurityComponentMethod-fallbackLineSpacing(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | Whether to enable the feature. The default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attributes of the security component. |

## focusBox

```TypeScript
focusBox(style: FocusBoxStyle | undefined): this
```

Set the focusBox style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-focusBox(style: FocusBoxStyle | undefined): this--><!--Device-SecurityComponentMethod-focusBox(style: FocusBoxStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [FocusBoxStyle](arkts-arkui-focusboxstyle-i.md) \| undefined | Yes | FocusBox style. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## fontColor

```TypeScript
fontColor(value: ResourceColor | undefined): this
```

Font color of the inner text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-fontColor(value: ResourceColor | undefined): this--><!--Device-SecurityComponentMethod-fontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | Indicates the font color of the text in the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## fontFamily

```TypeScript
fontFamily(value: string | Resource | undefined): this
```

Font family of the inner text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-fontFamily(value: string | Resource | undefined): this--><!--Device-SecurityComponentMethod-fontFamily(value: string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes | Indicates the font family of the text in the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## fontSize

```TypeScript
fontSize(value: Dimension | undefined): this
```

Font size of the inner text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-fontSize(value: Dimension | undefined): this--><!--Device-SecurityComponentMethod-fontSize(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | Indicates the font size of the text in the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## fontStyle

```TypeScript
fontStyle(value: FontStyle | undefined): this
```

Font style of the inner text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-fontStyle(value: FontStyle | undefined): this--><!--Device-SecurityComponentMethod-fontStyle(value: FontStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FontStyle](arkts-arkui-fontstyle-e.md) \| undefined | Yes | Indicates the font style of the text in the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## fontWeight

```TypeScript
fontWeight(value: int | FontWeight | string | Resource | undefined): this
```

Font weight of the inner text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-fontWeight(value: int | FontWeight | string | Resource | undefined): this--><!--Device-SecurityComponentMethod-fontWeight(value: int | FontWeight | string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes | Font weight of the text in the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## height

```TypeScript
height(value: Length | undefined): this
```

Sets the height of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-height(value: Length | undefined): this--><!--Device-SecurityComponentMethod-height(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | Indicates the height of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## heightAdaptivePolicy

```TypeScript
heightAdaptivePolicy(policy: TextHeightAdaptivePolicy | undefined): this
```

Called when the height adaptive policy is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-heightAdaptivePolicy(policy: TextHeightAdaptivePolicy | undefined): this--><!--Device-SecurityComponentMethod-heightAdaptivePolicy(policy: TextHeightAdaptivePolicy | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [TextHeightAdaptivePolicy](arkts-arkui-textheightadaptivepolicy-e.md) \| undefined | Yes | The height adaptive policy. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## iconColor

```TypeScript
iconColor(value: ResourceColor | undefined): this
```

Color of the icon.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-iconColor(value: ResourceColor | undefined): this--><!--Device-SecurityComponentMethod-iconColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | Indicates the icon color in the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## iconSize

```TypeScript
iconSize(value: Dimension | undefined): this
```

Icon size.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-iconSize(value: Dimension | undefined): this--><!--Device-SecurityComponentMethod-iconSize(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | Indicates the size of the icon. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## id

```TypeScript
id(id: string | undefined): this
```

Id. User can set an id to the component to identify it.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-id(id: string | undefined): this--><!--Device-SecurityComponentMethod-id(id: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## layoutDirection

```TypeScript
layoutDirection(value: SecurityComponentLayoutDirection | undefined): this
```

Layout direction of the icon and text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-layoutDirection(value: SecurityComponentLayoutDirection | undefined): this--><!--Device-SecurityComponentMethod-layoutDirection(value: SecurityComponentLayoutDirection | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SecurityComponentLayoutDirection](arkts-arkui-securitycomponent-securitycomponentlayoutdirection-e.md) \| undefined | Yes | Indicates the layout direction of the icon and text. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## markAnchor

```TypeScript
markAnchor(value: Position | undefined): this
```

Anchor of the security component for positioning. The top start edge of the component is used as the reference point for offset.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-markAnchor(value: Position | undefined): this--><!--Device-SecurityComponentMethod-markAnchor(value: Position | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| undefined | Yes | Indicates the anchor of the component when it is positioned. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## maxFontScale

```TypeScript
maxFontScale(scale: double | Resource | undefined): this
```

Sets the maximum font scale factor for text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-maxFontScale(scale: double | Resource | undefined): this--><!--Device-SecurityComponentMethod-maxFontScale(scale: double | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes | Maximum font scale factor to set. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attributes of the security component. |

## maxFontSize

```TypeScript
maxFontSize(maxSize: double | string | Resource | undefined): this
```

Called when the maximum font size of the font is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-maxFontSize(maxSize: double | string | Resource | undefined): this--><!--Device-SecurityComponentMethod-maxFontSize(maxSize: double | string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxSize | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## maxLines

```TypeScript
maxLines(line: int | Resource | undefined): this
```

Called when the maximum number of lines of text is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-maxLines(line: int | Resource | undefined): this--><!--Device-SecurityComponentMethod-maxLines(line: int | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| line | int \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## minFontScale

```TypeScript
minFontScale(scale: double | Resource | undefined): this
```

Sets the minimum font scale factor for text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-minFontScale(scale: double | Resource | undefined): this--><!--Device-SecurityComponentMethod-minFontScale(scale: double | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes | Minimum font scale factor to set. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attributes of the security component. |

## minFontSize

```TypeScript
minFontSize(minSize: double | string | Resource | undefined): this
```

Called when the minimum font size of the font is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-minFontSize(minSize: double | string | Resource | undefined): this--><!--Device-SecurityComponentMethod-minFontSize(minSize: double | string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minSize | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## offset

```TypeScript
offset(value: Position | Edges | LocalizedEdges | undefined): this
```

Coordinate offset relative to the layout completion position. Setting this attribute does not affect the layout of the parent container. The position is adjusted only during drawing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-offset(value: Position | Edges | LocalizedEdges | undefined): this--><!--Device-SecurityComponentMethod-offset(value: Position | Edges | LocalizedEdges | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| [Edges](arkts-arkui-edges-i.md) \| [LocalizedEdges](arkts-arkui-localizededges-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) |  |

## padding

```TypeScript
padding(value: Padding | Dimension | undefined): this
```

Padding between the background border and icon/inner text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-padding(value: Padding | Dimension | undefined): this--><!--Device-SecurityComponentMethod-padding(value: Padding | Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Padding](arkts-arkui-padding-t.md) \| [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | Indicates the padding of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## position

```TypeScript
position(value: Position | undefined): this
```

Position of the security component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-position(value: Position | undefined): this--><!--Device-SecurityComponentMethod-position(value: Position | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| undefined | Yes | Indicates the position of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## size

```TypeScript
size(value: SizeOptions | undefined): this
```

The size of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-size(value: SizeOptions | undefined): this--><!--Device-SecurityComponentMethod-size(value: SizeOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) \| undefined | Yes | Indicates the size of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## textIconSpace

```TypeScript
textIconSpace(value: Dimension | undefined): this
```

Space between the inner text and icon.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-textIconSpace(value: Dimension | undefined): this--><!--Device-SecurityComponentMethod-textIconSpace(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | Indicates the space between the inner text and icon. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

## width

```TypeScript
width(value: Length | undefined): this
```

Sets the width of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-width(value: Length | undefined): this--><!--Device-SecurityComponentMethod-width(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | Indicates the width of the security component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

