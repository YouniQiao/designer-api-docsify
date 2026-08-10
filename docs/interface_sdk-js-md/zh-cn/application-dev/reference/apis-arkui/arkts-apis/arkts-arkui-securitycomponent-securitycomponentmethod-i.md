# SecurityComponentMethod

Declares the interface for the method of a security component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface SecurityComponentMethod--><!--Device-unnamed-export declare interface SecurityComponentMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityDefaultFocus

```TypeScript
accessibilityDefaultFocus(focus: boolean | undefined): this
```

Sets the default focus flag of the accessibility feature.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-accessibilityDefaultFocus(focus: boolean | undefined): this--><!--Device-SecurityComponentMethod-accessibilityDefaultFocus(focus: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| focus | boolean \| undefined | 是 | Set to true if the component is the default accessibility focus. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the security component. |

## accessibilityDescription

```TypeScript
accessibilityDescription(description: string | Resource | undefined): this
```

Sets the accessibility description.

This property provides additional context or explanation for the component,helping users understand its actions or functions.&lt;p&gt;&lt;strong&gt;Note&lt;/strong&gt;:You can provide further explanation for the current component, such as the potential consequences of an operation, especially those not implicitly conveyed by the component's text or role type. If a component includes text information, a role type (other than ROLE_NONE),and an accessibility description, the system reads them when the component is selected.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-accessibilityDescription(description: string | Resource | undefined): this--><!--Device-SecurityComponentMethod-accessibilityDescription(description: string | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| description | string \| Resource \| undefined | 是 | Accessibility description. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the security component. |

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId(nextId: string | undefined): this
```

Sets the ID of the next component to receive accessibility focus.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-accessibilityNextFocusId(nextId: string | undefined): this--><!--Device-SecurityComponentMethod-accessibilityNextFocusId(nextId: string | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nextId | string \| undefined | 是 | ID of the next component to receive accessibility focus. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the security component. |

## accessibilityRole

```TypeScript
accessibilityRole(role: SecurityComponentRoleType | undefined): this
```

Sets the accessibility role, which represents the custom type of the component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-accessibilityRole(role: SecurityComponentRoleType | undefined): this--><!--Device-SecurityComponentMethod-accessibilityRole(role: SecurityComponentRoleType | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| role | [SecurityComponentRoleType](arkts-arkui-securitycomponentroletype-e.md) \| undefined | 是 | Component type of the accessibility feature. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the security component. |

## align

```TypeScript
align(alignType: Alignment | undefined): this
```

align

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-align(alignType: Alignment | undefined): this--><!--Device-SecurityComponentMethod-align(alignType: Alignment | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | [Alignment](arkts-arkui-alignment-e.md) \| undefined | 是 | Indicates the align type of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## alignRules

```TypeScript
alignRules(alignRule: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this
```

Specifies the alignRules of relative container

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-alignRules(alignRule: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this--><!--Device-SecurityComponentMethod-alignRules(alignRule: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignRule | [AlignRuleOption](../arkts-components/arkts-arkui-alignruleoption-i.md) \| LocalizedAlignRuleOptions \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## backgroundColor

```TypeScript
backgroundColor(value: ResourceColor | undefined): this
```

Background color.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-backgroundColor(value: ResourceColor | undefined): this--><!--Device-SecurityComponentMethod-backgroundColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | Indicates the background color of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## borderColor

```TypeScript
borderColor(value: ResourceColor | undefined): this
```

Color of the border.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-borderColor(value: ResourceColor | undefined): this--><!--Device-SecurityComponentMethod-borderColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | Indicates the border color of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## borderRadius

```TypeScript
borderRadius(radius: Dimension | BorderRadiuses | undefined): this
```

Radius of the border.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-borderRadius(radius: Dimension | BorderRadiuses | undefined): this--><!--Device-SecurityComponentMethod-borderRadius(radius: Dimension | BorderRadiuses | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | [Dimension](arkts-arkui-dimension-t.md) \| BorderRadiuses \| undefined | 是 | Indicates the border radius of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## borderStyle

```TypeScript
borderStyle(value: BorderStyle | undefined): this
```

Style of the border.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-borderStyle(value: BorderStyle | undefined): this--><!--Device-SecurityComponentMethod-borderStyle(value: BorderStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderStyle](arkts-arkui-borderstyle-e.md) \| undefined | 是 | Indicates the border style of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## borderWidth

```TypeScript
borderWidth(value: Dimension | undefined): this
```

Width of the border.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-borderWidth(value: Dimension | undefined): this--><!--Device-SecurityComponentMethod-borderWidth(value: Dimension | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 | Indicates the border width of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## chainMode

```TypeScript
chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this
```

Specifies the direction and style of chain in relative container

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this--><!--Device-SecurityComponentMethod-chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | [Axis](arkts-arkui-axis-e.md) \| undefined | 是 | Indicates direction of the chain |
| style | [ChainStyle](../arkts-components/arkts-arkui-chainstyle-e.md) \| undefined | 是 | Indicates style of the chain |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## constraintSize

```TypeScript
constraintSize(value: ConstraintSizeOptions | undefined): this
```

constraint Size:minWidth: minimum Width, maxWidth: maximum Width, minHeight: minimum Height, maxHeight: maximum Height.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-constraintSize(value: ConstraintSizeOptions | undefined): this--><!--Device-SecurityComponentMethod-constraintSize(value: ConstraintSizeOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ConstraintSizeOptions](arkts-arkui-constraintsizeoptions-i.md) \| undefined | 是 | Indicates the constraint size of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## enabled

```TypeScript
enabled(respond: boolean | undefined): this
```

If the value is true, the component is available and can respond to operations such as clicking. If it is set to false, click operations are not responded.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-enabled(respond: boolean | undefined): this--><!--Device-SecurityComponentMethod-enabled(respond: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| respond | boolean \| undefined | 是 | Indicates whether the button is responded to. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## fallbackLineSpacing

```TypeScript
fallbackLineSpacing(enabled: boolean | undefined): this
```

Whether to include the ascent and descent of fallback fonts to prevent line overlap.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-fallbackLineSpacing(enabled: boolean | undefined): this--><!--Device-SecurityComponentMethod-fallbackLineSpacing(enabled: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 | Whether to enable the feature. The default value is false. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the security component. |

## focusBox

```TypeScript
focusBox(style: FocusBoxStyle | undefined): this
```

Set the focusBox style.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-focusBox(style: FocusBoxStyle | undefined): this--><!--Device-SecurityComponentMethod-focusBox(style: FocusBoxStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [FocusBoxStyle](arkts-arkui-focusboxstyle-i.md) \| undefined | 是 | FocusBox style. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## fontColor

```TypeScript
fontColor(value: ResourceColor | undefined): this
```

Font color of the inner text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-fontColor(value: ResourceColor | undefined): this--><!--Device-SecurityComponentMethod-fontColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | Indicates the font color of the text in the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## fontFamily

```TypeScript
fontFamily(value: string | Resource | undefined): this
```

Font family of the inner text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-fontFamily(value: string | Resource | undefined): this--><!--Device-SecurityComponentMethod-fontFamily(value: string | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| Resource \| undefined | 是 | Indicates the font family of the text in the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## fontSize

```TypeScript
fontSize(value: Dimension | undefined): this
```

Font size of the inner text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-fontSize(value: Dimension | undefined): this--><!--Device-SecurityComponentMethod-fontSize(value: Dimension | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 | Indicates the font size of the text in the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## fontStyle

```TypeScript
fontStyle(value: FontStyle | undefined): this
```

Font style of the inner text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-fontStyle(value: FontStyle | undefined): this--><!--Device-SecurityComponentMethod-fontStyle(value: FontStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](arkts-arkui-fontstyle-e.md) \| undefined | 是 | Indicates the font style of the text in the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## fontWeight

```TypeScript
fontWeight(value: int | FontWeight | string | Resource | undefined): this
```

Font weight of the inner text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-fontWeight(value: int | FontWeight | string | Resource | undefined): this--><!--Device-SecurityComponentMethod-fontWeight(value: int | FontWeight | string | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| FontWeight \| string \| Resource \| undefined | 是 | Font weight of the text in the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## height

```TypeScript
height(value: Length | undefined): this
```

Sets the height of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-height(value: Length | undefined): this--><!--Device-SecurityComponentMethod-height(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | Indicates the height of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## heightAdaptivePolicy

```TypeScript
heightAdaptivePolicy(policy: TextHeightAdaptivePolicy | undefined): this
```

Called when the height adaptive policy is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-heightAdaptivePolicy(policy: TextHeightAdaptivePolicy | undefined): this--><!--Device-SecurityComponentMethod-heightAdaptivePolicy(policy: TextHeightAdaptivePolicy | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | [TextHeightAdaptivePolicy](arkts-arkui-textheightadaptivepolicy-e.md) \| undefined | 是 | The height adaptive policy. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## iconColor

```TypeScript
iconColor(value: ResourceColor | undefined): this
```

Color of the icon.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-iconColor(value: ResourceColor | undefined): this--><!--Device-SecurityComponentMethod-iconColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | Indicates the icon color in the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## iconSize

```TypeScript
iconSize(value: Dimension | undefined): this
```

Icon size.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-iconSize(value: Dimension | undefined): this--><!--Device-SecurityComponentMethod-iconSize(value: Dimension | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 | Indicates the size of the icon. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## id

```TypeScript
id(id: string | undefined): this
```

Id. User can set an id to the component to identify it.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-id(id: string | undefined): this--><!--Device-SecurityComponentMethod-id(id: string | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## layoutDirection

```TypeScript
layoutDirection(value: SecurityComponentLayoutDirection | undefined): this
```

Layout direction of the icon and text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-layoutDirection(value: SecurityComponentLayoutDirection | undefined): this--><!--Device-SecurityComponentMethod-layoutDirection(value: SecurityComponentLayoutDirection | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SecurityComponentLayoutDirection](arkts-arkui-securitycomponentlayoutdirection-e.md) \| undefined | 是 | Indicates the layout direction of the icon and text. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## markAnchor

```TypeScript
markAnchor(value: Position | undefined): this
```

Anchor of the security component for positioning. The top start edge of the component is used as the reference point for offset.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-markAnchor(value: Position | undefined): this--><!--Device-SecurityComponentMethod-markAnchor(value: Position | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| undefined | 是 | Indicates the anchor of the component when it is positioned. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## maxFontScale

```TypeScript
maxFontScale(scale: double | Resource | undefined): this
```

Sets the maximum font scale factor for text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-maxFontScale(scale: double | Resource | undefined): this--><!--Device-SecurityComponentMethod-maxFontScale(scale: double | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | double \| Resource \| undefined | 是 | Maximum font scale factor to set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the security component. |

## maxFontSize

```TypeScript
maxFontSize(maxSize: double | string | Resource | undefined): this
```

Called when the maximum font size of the font is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-maxFontSize(maxSize: double | string | Resource | undefined): this--><!--Device-SecurityComponentMethod-maxFontSize(maxSize: double | string | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSize | double \| string \| Resource \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## maxLines

```TypeScript
maxLines(line: int | Resource | undefined): this
```

Called when the maximum number of lines of text is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-maxLines(line: int | Resource | undefined): this--><!--Device-SecurityComponentMethod-maxLines(line: int | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| line | int \| Resource \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## minFontScale

```TypeScript
minFontScale(scale: double | Resource | undefined): this
```

Sets the minimum font scale factor for text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-minFontScale(scale: double | Resource | undefined): this--><!--Device-SecurityComponentMethod-minFontScale(scale: double | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | double \| Resource \| undefined | 是 | Minimum font scale factor to set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the security component. |

## minFontSize

```TypeScript
minFontSize(minSize: double | string | Resource | undefined): this
```

Called when the minimum font size of the font is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-minFontSize(minSize: double | string | Resource | undefined): this--><!--Device-SecurityComponentMethod-minFontSize(minSize: double | string | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minSize | double \| string \| Resource \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## offset

```TypeScript
offset(value: Position | Edges | LocalizedEdges | undefined): this
```

Coordinate offset relative to the layout completion position.Setting this attribute does not affect the layout of the parent container.The position is adjusted only during drawing.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-offset(value: Position | Edges | LocalizedEdges | undefined): this--><!--Device-SecurityComponentMethod-offset(value: Position | Edges | LocalizedEdges | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| Edges \| LocalizedEdges \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## padding

```TypeScript
padding(value: Padding | Dimension | undefined): this
```

Padding between the background border and icon/inner text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-padding(value: Padding | Dimension | undefined): this--><!--Device-SecurityComponentMethod-padding(value: Padding | Dimension | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Padding](arkts-arkui-units-padding-i.md) \| Dimension \| undefined | 是 | Indicates the padding of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## position

```TypeScript
position(value: Position | undefined): this
```

Position of the security component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-position(value: Position | undefined): this--><!--Device-SecurityComponentMethod-position(value: Position | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| undefined | 是 | Indicates the position of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## size

```TypeScript
size(value: SizeOptions | undefined): this
```

The size of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-size(value: SizeOptions | undefined): this--><!--Device-SecurityComponentMethod-size(value: SizeOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) \| undefined | 是 | Indicates the size of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## textIconSpace

```TypeScript
textIconSpace(value: Dimension | undefined): this
```

Space between the inner text and icon.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-textIconSpace(value: Dimension | undefined): this--><!--Device-SecurityComponentMethod-textIconSpace(value: Dimension | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 | Indicates the space between the inner text and icon. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

## width

```TypeScript
width(value: Length | undefined): this
```

Sets the width of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-width(value: Length | undefined): this--><!--Device-SecurityComponentMethod-width(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | Indicates the width of the security component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

