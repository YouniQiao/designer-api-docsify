# Select properties/events

In addition to the universal attributes, the following attributes are supported.

**Inheritance/Implementation:** SelectAttribute extends CommonMethod<SelectAttribute>

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## arrowModifier

```TypeScript
arrowModifier(modifier: Optional<SymbolGlyphModifier>)
```

Creates an arrow modifier to customize the drop-down arrow icon style of the **Select** button. After **arrowModifier** is applied, the drop-down arrow icon style of the **Select** button will be completely customized by the developer.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [Optional](arkts-arkui-optional-t.md)&lt;SymbolGlyphModifier&gt; | Yes |

## arrowPosition

```TypeScript
arrowPosition(value: ArrowPosition)
```

Sets the alignment between the text and arrow of an option.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [ArrowPosition](arkts-arkui-arrowposition-e.md) | Yes |

## arrowPosition

```TypeScript
arrowPosition(position: Optional<ArrowPosition>)
```

Sets the alignment between the text and arrow of an option. Compared with [arrowPosition](#arrowposition), this API supports the **undefined** type for the **position** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | [Optional](arkts-arkui-optional-t.md)&lt;[ArrowPosition](arkts-arkui-arrowposition-e.md)&gt; | Yes |

## avoidance

```TypeScript
avoidance(mode: AvoidanceMode)
```

Sets the avoidance mode for the drop-down menu.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AvoidanceMode](arkts-arkui-avoidancemode-e.md) | Yes |

## controlSize

```TypeScript
controlSize(value: ControlSize)
```

Sets the size of the **Select** component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [ControlSize](arkts-arkui-controlsize-e.md) | Yes |

## controlSize

```TypeScript
controlSize(size: Optional<ControlSize>)
```

Sets the size of the **Select** component. Compared with [controlSize](#controlsize)&lt;sup&gt;12+&lt;/sup&gt;, this API supports the **undefined** type for **size** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | [Optional](arkts-arkui-optional-t.md)&lt;[ControlSize](arkts-arkui-controlsize-e.md)&gt; | Yes |

## divider

```TypeScript
divider(options: Optional<DividerOptions> | null)
```

Sets the divider style. If this attribute is not set, the divider is displayed based on the default value.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[DividerOptions](arkts-arkui-divideroptions-i.md)&gt; \| null | Yes |

## dividerStyle

```TypeScript
dividerStyle(style: Optional<DividerStyleOptions>)
```

Sets the divider style. If this attribute is not set, the divider is displayed based on the default value. This attribute cannot be used together with the **divider** attribute. The last one called will take effect.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[DividerStyleOptions](../arkts-apis/arkts-arkui-dividerstyleoptions-i.md)&gt; | Yes |

## font

```TypeScript
font(value: Font)
```

Sets the text style of the drop-down button. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [Font](#font) | Yes |

## font

```TypeScript
font(selectFont: Optional<Font>)
```

Sets the text style of the drop-down button. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size. Compared with [font](#font), this API supports the **undefined** type for the **selectFont** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectFont | [Optional](arkts-arkui-optional-t.md)&lt;Font&gt; | Yes |

## fontColor

```TypeScript
fontColor(value: ResourceColor)
```

Sets the font color of the drop-down button.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## fontColor

```TypeScript
fontColor(resColor: Optional<ResourceColor>)
```

Sets the font color of the drop-down button. Compared with [fontColor](#fontcolor), this API supports the **undefined** type for the **resColor** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resColor | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes |

## keyboardAvoidMode

```TypeScript
keyboardAvoidMode(mode: Optional<MenuKeyboardAvoidMode>)
```

Sets whether the drop-down menu avoids the soft keyboard. If this API is not used, the drop-down menu avoids the soft keyboard by default.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [Optional](arkts-arkui-optional-t.md)&lt;[MenuKeyboardAvoidMode](arkts-arkui-menukeyboardavoidmode-e.md)&gt; | Yes |

## menuAlign

```TypeScript
menuAlign(alignType: MenuAlignType, offset?: Offset)
```

Sets the alignment between the drop-down button and the drop-down menu.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [alignType](../arkts-apis/arkts-arkui-atomicservice-atomicservicesearch-menualignparams-i.md) | [MenuAlignType](arkts-arkui-menualigntype-e.md) | Yes |
| offset | [Offset](../arkts-apis/arkts-arkui-componentutils-offset-i.md) | No |

## menuAlign

```TypeScript
menuAlign(alignType: Optional<MenuAlignType>, offset?: Offset)
```

Sets the alignment between the drop-down button and the drop-down menu. Compared with [menuAlign](#menualign)&lt;sup&gt;10+&lt;/sup&gt;, this API supports the **undefined** type for the **alignType** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [alignType](../arkts-apis/arkts-arkui-atomicservice-atomicservicesearch-menualignparams-i.md) | [Optional](arkts-arkui-optional-t.md)&lt;[MenuAlignType](arkts-arkui-menualigntype-e.md)&gt; | Yes |
| offset | [Offset](../arkts-apis/arkts-arkui-componentutils-offset-i.md) | No |

## menuBackgroundBlurStyle

```TypeScript
menuBackgroundBlurStyle(value: BlurStyle)
```

Sets the background blur style of the drop-down menu.

> **NOTE：**&gt;
> This API can be called within attributeModifier since API version 12.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [BlurStyle](arkts-arkui-blurstyle-e.md) | Yes |

## menuBackgroundBlurStyle

```TypeScript
menuBackgroundBlurStyle(style: Optional<BlurStyle>)
```

Sets the background blur style of the drop-down menu. Compared with [menuBackgroundBlurStyle](#menubackgroundblurstyle)&lt;sup&gt;11+&lt;/sup&gt;, this API supports the **undefined** type for the **style** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;BlurStyle&gt; | Yes |

## menuBackgroundBlurStyleOptions

```TypeScript
menuBackgroundBlurStyleOptions(blurStyle: Optional<BackgroundBlurStyleOptions>)
```

Defines the select menu's background blur style with options

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurStyle](arkts-arkui-sheetoptions-i.md) | [Optional](arkts-arkui-optional-t.md)&lt;[BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md)&gt; | Yes |

## menuBackgroundColor

```TypeScript
menuBackgroundColor(value: ResourceColor)
```

Sets the background color of the drop-down menu.

> **NOTE：**&gt;
> This API can be called within attributeModifier since API version 12.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## menuBackgroundColor

```TypeScript
menuBackgroundColor(resColor: Optional<ResourceColor>)
```

Sets the background color of the drop-down menu. Compared with [menuBackgroundColor](#menubackgroundcolor)&lt;sup&gt;11+&lt;/sup&gt;, this API supports the **undefined** type for the **resColor** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resColor | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes |

## menuBackgroundEffect

```TypeScript
menuBackgroundEffect(effect: Optional<BackgroundEffectOptions>)
```

Defines the select menu's background effect with options

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [Optional](arkts-arkui-optional-t.md)&lt;[BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md)&gt; | Yes |

## menuItemContentModifier

```TypeScript
menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration>)
```

Creates a content modifier for the drop-down menu. After **menuItemContentModifier** is applied, the drop-down menu content will be completely customized by the developer, and the **Select** component's attributes, including the divider, option color, and drop-down menu font color, will not take effect.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[MenuItemConfiguration](arkts-arkui-menuitemconfiguration-i.md)&gt; | Yes |

## menuItemContentModifier

```TypeScript
menuItemContentModifier(modifier: Optional<ContentModifier<MenuItemConfiguration>>)
```

Creates a content modifier for the drop-down menu. Compared with [menuItemContentModifier](#menuitemcontentmodifier) &lt;sup&gt;12+&lt;/sup&gt;, this API supports the **undefined** type for **modifier** parameter. After **menuItemContentModifier** is applied, the drop-down menu content will be completely customized by the developer, and the **Select** component's attributes, including the divider, option color, and drop-down menu font color, will not take effect.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [Optional](arkts-arkui-optional-t.md)&lt;[ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[MenuItemConfiguration](arkts-arkui-menuitemconfiguration-i.md)&gt;&gt; | Yes |

## menuOutline

```TypeScript
menuOutline(outline: MenuOutlineOptions)
```

Sets the outline style for the drop-down menu.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [outline](arkts-arkui-commonmethod-c.md) | [MenuOutlineOptions](arkts-arkui-menuoutlineoptions-i.md) | Yes |

## menuSystemMaterial

```TypeScript
menuSystemMaterial(material: Optional<SystemUiMaterial>)
```

Set system-styled materials for select's menu. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of select's menu.Device Behavior Differences:The effect of the same material may vary across different devices depending on their computing power.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| material | [Optional](arkts-arkui-optional-t.md)&lt;[SystemUiMaterial](arkts-arkui-systemuimaterial-t.md)&gt; | Yes |

## minKeyboardAvoidDistance

```TypeScript
minKeyboardAvoidDistance(distance: Optional<LengthMetrics>)
```

Sets the minimum distance for the **Select** component to avoid the soft keyboard. If this API is not used, the minimum distance is 8 vp by default. This API is valid only when [keyboardAvoidMode](#keyboardavoidmode) is set to avoid the soft keyboard.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| distance | [Optional](arkts-arkui-optional-t.md)&lt;LengthMetrics&gt; | Yes |

## onSelect

```TypeScript
onSelect(callback: (index: number, value: string) => void)
```

Triggered when a drop-down menu option is selected.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (index: number, value: string) = & gt; void | Yes |

## onSelect

```TypeScript
onSelect(callback: Optional<OnSelectCallback>)
```

Triggered when a drop-down menu option is selected. Compared with onSelect, this API supports the **undefined** type for the **callback** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Optional](arkts-arkui-optional-t.md)&lt;[OnSelectCallback](arkts-arkui-onselectcallback-t.md)&gt; | Yes |

## optionBgColor

```TypeScript
optionBgColor(value: ResourceColor)
```

Sets the background color of options in the drop-down menu.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## optionBgColor

```TypeScript
optionBgColor(resColor: Optional<ResourceColor>)
```

Sets the background color of options in the drop-down menu. Compared with [optionBgColor](#optionbgcolor), this API supports the **undefined** type for the **resColor** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resColor | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes |

## optionFont

```TypeScript
optionFont(value: Font)
```

Sets the text font of options in the drop-down menu. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [Font](#font) | Yes |

## optionFont

```TypeScript
optionFont(selectFont: Optional<Font>)
```

Sets the text font of options in the drop-down menu. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size.Compared with [optionFont](#optionfont), this API supports the **undefined** type for the **selectFont** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectFont | [Optional](arkts-arkui-optional-t.md)&lt;Font&gt; | Yes |

## optionFontColor

```TypeScript
optionFontColor(value: ResourceColor)
```

Sets the font color of options in the drop-down menu.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## optionFontColor

```TypeScript
optionFontColor(resColor: Optional<ResourceColor>)
```

Sets the font color of options in the drop-down menu. Compared with [optionFontColor](#optionfontcolor), this API supports the **undefined** type for the **resColor** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resColor | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes |

## optionHeight

```TypeScript
optionHeight(value: Dimension)
```

Sets the maximum height for the drop-down menu. Percentage values are not supported. The default maximum height is 80% of the available screen height, and any custom maximum height setting must not exceed this limit.This attribute has no effect when set to abnormal values or zero.If the actual height of all drop-down menu options is less than the set height, the menu will automatically adjust to the actual content height.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) | Yes |

## optionHeight

```TypeScript
optionHeight(height: Optional<Dimension>)
```

Sets the maximum height for the drop-down menu. Percentage values are not supported. The default maximum height is 80% of the available screen height, and any custom maximum height setting must not exceed this limit. Compared with [optionHeight](#optionheight)&lt;sup&gt;11+&lt;/sup&gt;, this API supports the **undefined** type for the **height** parameter.This attribute has no effect when set to abnormal values or zero.If the actual height of all drop-down menu options is less than the set height, the menu will automatically adjust to the actual content height.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| height | [Optional](arkts-arkui-optional-t.md)&lt;[Dimension](../arkts-apis/arkts-arkui-dimension-t.md)&gt; | Yes |

## optionTextModifier

```TypeScript
optionTextModifier(modifier: Optional<TextModifier>)
```

Creates an option text modifier to customize the text style of unselected options in the drop-down menu. After **optionTextModifier** is applied, the unselected option text style will be completely customized by the developer.If both [optionFont](#optionfont) and **Font** of **optionTextModifier** are set, [optionFont](#optionfont) takes precedence. Any unspecified attributes in **optionFont** will use default values.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [Optional](arkts-arkui-optional-t.md)&lt;[TextModifier](../arkts-apis/arkts-arkui-textmodifier-c.md)&gt; | Yes |

## optionWidth

```TypeScript
optionWidth(value: Dimension | OptionWidthMode )
```

Sets the width for the drop-down menu option. Percentage values are not supported. **OptionWidthMode** specifies whether to inherit the width of the drop-down button.If an invalid value or a value less than the minimum width of 56 vp is set, the attribute has no effect. In this case, the option width uses the default value, which is the width of two columns.The **Select** component maintains 16 vp spacing from both left and right screen edges by default. This creates a 3 2 vp total horizontal margin (16 vp × 2). To prevent horizontal shifting when the drop-down menu is displayed, set the width of the component itself and its menu options to a value less than or equal to **calc(100% - 32 vp)**.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [OptionWidthMode](../arkts-apis/arkts-arkui-optionwidthmode-e.md) | Yes |

## optionWidth

```TypeScript
optionWidth(width: Optional<Dimension | OptionWidthMode> )
```

Sets the width for the drop-down menu option. Percentage values are not supported. **OptionWidthMode** specifies whether to inherit the width of the drop-down button. Compared with [optionWidth](#optionwidth)&lt;sup&gt;11+&lt;/sup&gt;, this API supports the **undefined** type for the **width** parameter.If an invalid value or a value less than the minimum width of 56 vp is set, the attribute has no effect. In this case, the option width uses the default value, which is the width of two columns.The **Select** component maintains 16 vp spacing from both left and right screen edges by default. This creates a 3 2 vp total horizontal margin (16 vp × 2). To prevent horizontal shifting when the drop-down menu is displayed, set the width of the component itself and its menu options to a value less than or equal to **calc(100% - 32 vp)**.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | [Optional](arkts-arkui-optional-t.md)&lt;[Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [OptionWidthMode](../arkts-apis/arkts-arkui-optionwidthmode-e.md)&gt; | Yes |

## selected

```TypeScript
selected(value: number | Resource)
```

Sets the index of the initially selected option in the drop-down menu, where the first option has an index of 0. When **selected** is set to an invalid value or is not set, the default default **-1** is used, which indicates no selection. When **selected** is set to **undefined** or **null**, the first option is selected.Since API version 10, this attribute supports two-way binding through [\$\$](../../../ui/state-management/arkts-two-way-sync.md).Since API version 18, this attribute supports two-way binding through [!!](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## selected

```TypeScript
selected(numCount: Optional<number | Resource>)
```

Sets the index of the initially selected option in the drop-down menu, where the first option has an index of 0. When **selected** is set to an invalid value or is not set, the default default **-1** is used, which indicates no selection. When **selected** is set to **undefined** or **null**, the first option is selected.This attribute supports two-way binding through [\$\$](../../../ui/state-management/arkts-two-way-sync.md) and [!!](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters).

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| numCount | [Optional](arkts-arkui-optional-t.md)&lt;number \| Resource & gt; | Yes |

## selectedOptionBgColor

```TypeScript
selectedOptionBgColor(value: ResourceColor)
```

Sets the background color of the selected option in the drop-down menu.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## selectedOptionBgColor

```TypeScript
selectedOptionBgColor(resColor: Optional<ResourceColor>)
```

Sets the background color of the selected option in the drop-down menu. Compared with [selectedOptionBgColor](#selectedoptionbgcolor), this API supports the **undefined** type for the **resColor** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resColor | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes |

## selectedOptionFont

```TypeScript
selectedOptionFont(value: Font)
```

Sets the text font of the selected option in the drop-down menu. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [Font](#font) | Yes |

## selectedOptionFont

```TypeScript
selectedOptionFont(selectFont: Optional<Font>)
```

Sets the text font of the selected option in the drop-down menu. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size. Compared with [selectedOptionFont](#selectedoptionfont), this API supports the **undefined** type for the **selectFont** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectFont | [Optional](arkts-arkui-optional-t.md)&lt;Font&gt; | Yes |

## selectedOptionFontColor

```TypeScript
selectedOptionFontColor(value: ResourceColor)
```

Sets the font color of the selected option in the drop-down menu.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## selectedOptionFontColor

```TypeScript
selectedOptionFontColor(resColor: Optional<ResourceColor>)
```

Sets the font color of the selected option in the drop-down menu. Compared with [selectedOptionFontColor](#selectedoptionfontcolor), this API supports the **undefined** type for the **resColor** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resColor | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes |

## selectedOptionTextModifier

```TypeScript
selectedOptionTextModifier(modifier: Optional<TextModifier>)
```

Creates a selected-option text modifier to customize the text style of selected options in the drop-down menu. After **selectedOptionTextModifier** is applied, the selected-option text style will be completely customized by the developer.If both [selectedOptionFont](#selectedoptionfont) and **Font** of **selectedOptionTextModifier** are set, [selectedOptionFont](#selectedoptionfont) takes precedence. If **selectedOptionFont** is not set, [optionFont](#optionfont) settings are applied. Any unspecified attributes in **selectedOptionFont** or **optionFont** will use default values.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [Optional](arkts-arkui-optional-t.md)&lt;[TextModifier](../arkts-apis/arkts-arkui-textmodifier-c.md)&gt; | Yes |

## showDefaultSelectedIcon

```TypeScript
showDefaultSelectedIcon(show: boolean)
```

Sets whether to display the default selection icon.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| show | boolean | Yes |

## showInSubWindow

```TypeScript
showInSubWindow(showInSubWindow: Optional<boolean>)
```

Sets whether the drop-down menu is displayed in the subwindow. If this API is not used, the drop-down menu is not displayed in the subwindow by default.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [showInSubWindow](#showinsubwindow) | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## space

```TypeScript
space(value: Length)
```

Sets the spacing between the text and arrow of a drop-down menu option. This attribute cannot be set in percentage. If the value specified is **null**, **undefined**, or less than or equal to 8, the default value is used.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## space

```TypeScript
space(spaceLength: Optional<Length>)
```

Sets the spacing between the text and arrow of a drop-down menu option. This attribute cannot be set in percentage. If the value specified is **null**, **undefined**, or less than or equal to 8, the default value is used.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| spaceLength | [Optional](arkts-arkui-optional-t.md)&lt;[Length](../arkts-apis/arkts-arkui-length-t.md)&gt; | Yes |

## textModifier

```TypeScript
textModifier(modifier: Optional<TextModifier>)
```

Creates a text modifier to customize the text style of the **Select** button. After **textModifier** is applied, the text style of the **Select** button will be completely customized by the developer.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [Optional](arkts-arkui-optional-t.md)&lt;[TextModifier](../arkts-apis/arkts-arkui-textmodifier-c.md)&gt; | Yes |

## value

```TypeScript
value(value: ResourceStr)
```

Sets the text content of drop-down button. After a menu option is selected, the button text will automatically update to display the selected option's text.Since API version 10, this attribute supports two-way binding through [\$\$](../../../ui/state-management/arkts-two-way-sync.md).Since API version 18, this attribute supports two-way binding through [!!](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |

## value

```TypeScript
value(resStr: Optional<ResourceStr>)
```

Sets the text content of drop-down button. After a menu option is selected, the button text will automatically update to display the selected option's text. Compared with [value](#value), this API supports the **undefined** type for the **resStr** parameter.This attribute supports two-way binding through [\$\$](../../../ui/state-management/arkts-two-way-sync.md) and [!!](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters).

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resStr | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)&gt; | Yes |
