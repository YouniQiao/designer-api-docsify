# SelectAttribute

Defines the Select component attributes.

**Inheritance/Implementation:** SelectAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SelectAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SelectAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowModifier

```TypeScript
default arrowModifier(modifier: SymbolGlyphModifier | undefined): this
```

Sets the attribute modifier for the arrow symbol of select.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default arrowModifier(modifier: SymbolGlyphModifier | undefined): this--><!--Device-SelectAttribute-default arrowModifier(modifier: SymbolGlyphModifier | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md) \| undefined | Yes | Set modifier for the arrow symbol of select. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## arrowPosition

```TypeScript
default arrowPosition(value: ArrowPosition | undefined): this
```

Set the layout direction for text and arrow in select

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default arrowPosition(value: ArrowPosition | undefined): this--><!--Device-SelectAttribute-default arrowPosition(value: ArrowPosition | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ArrowPosition](arkts-arkui-select-arrowposition-e.md) \| undefined | Yes | indicates the arrow position in the select |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<SelectAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of select.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default attributeModifier(        modifier: AttributeModifier<SelectAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-SelectAttribute-default attributeModifier(        modifier: AttributeModifier<SelectAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SelectAttribute](arkts-arkui-select-selectattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes | The attribute modifier of select. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## avoidance

```TypeScript
default avoidance(mode: AvoidanceMode | undefined): this
```

Set the select menu avoidance mode

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default avoidance(mode: AvoidanceMode | undefined): this--><!--Device-SelectAttribute-default avoidance(mode: AvoidanceMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [AvoidanceMode](arkts-arkui-select-avoidancemode-e.md) \| undefined | Yes | Enumeration value of the avoidance mode |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the chained object of Select component attributes |

## controlSize

```TypeScript
default controlSize(value: ControlSize | undefined): this
```

Sets the size for controls within Select Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default controlSize(value: ControlSize | undefined): this--><!--Device-SelectAttribute-default controlSize(value: ControlSize | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ControlSize](../arkts-components/arkts-arkui-controlsize-e.md) \| undefined | Yes | control size |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## divider

```TypeScript
default divider(options: DividerOptions | null | undefined): this
```

Set the divider of select.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default divider(options: DividerOptions | null | undefined): this--><!--Device-SelectAttribute-default divider(options: DividerOptions | null | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DividerOptions](arkts-arkui-textpicker-divideroptions-i.md) \| null \| undefined | Yes | Set custom and hidden divider. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## dividerStyle

```TypeScript
default dividerStyle(style: DividerStyleOptions | undefined): this
```

Set the divider style of option

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default dividerStyle(style: DividerStyleOptions | undefined): this--><!--Device-SelectAttribute-default dividerStyle(style: DividerStyleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [DividerStyleOptions](arkts-arkui-dividerstyleoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## font

```TypeScript
default font(value: Font | undefined): this
```

Sets the text properties of the select button itself.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default font(value: Font | undefined): this--><!--Device-SelectAttribute-default font(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

Sets the text color of the select button itself.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default fontColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default fontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## keyboardAvoidMode

```TypeScript
default keyboardAvoidMode(mode: MenuKeyboardAvoidMode | undefined): this
```

Determine the mode of select menu how to avoid keyboard.

No avoiding by default.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default keyboardAvoidMode(mode: MenuKeyboardAvoidMode | undefined): this--><!--Device-SelectAttribute-default keyboardAvoidMode(mode: MenuKeyboardAvoidMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [MenuKeyboardAvoidMode](../arkts-components/arkts-arkui-menukeyboardavoidmode-e.md) \| undefined | Yes | How to avoid keyboard. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The attribute of the select. |

## menuAlign

```TypeScript
default menuAlign(alignType: MenuAlignType | undefined, offset?: Offset | undefined): this
```

Set the alignment between select and menu.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuAlign(alignType: MenuAlignType | undefined, offset?: Offset | undefined): this--><!--Device-SelectAttribute-default menuAlign(alignType: MenuAlignType | undefined, offset?: Offset | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alignType | [MenuAlignType](arkts-arkui-select-menualigntype-e.md) \| undefined | Yes | The type of alignment between select and menu. |
| offset | Offset \| undefined | No | The offset between select and menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## menuBackgroundBlurStyle

```TypeScript
default menuBackgroundBlurStyle(value: BlurStyle | undefined): this
```

set menu background blur Style

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuBackgroundBlurStyle(value: BlurStyle | undefined): this--><!--Device-SelectAttribute-default menuBackgroundBlurStyle(value: BlurStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | Yes | The BackgroundBlurStyle of menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## menuBackgroundBlurStyleOptions

```TypeScript
default menuBackgroundBlurStyleOptions(blurStyle: BackgroundBlurStyleOptions | undefined): this
```

Defines the select menu's background blur style options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuBackgroundBlurStyleOptions(blurStyle: BackgroundBlurStyleOptions | undefined): this--><!--Device-SelectAttribute-default menuBackgroundBlurStyleOptions(blurStyle: BackgroundBlurStyleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurStyle | [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md) \| undefined | Yes | The background blur style options of menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The attribute of the select. |

## menuBackgroundColor

```TypeScript
default menuBackgroundColor(value: ResourceColor | undefined): this
```

set the menu's background color

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuBackgroundColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default menuBackgroundColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | The backgroundColor of menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## menuBackgroundEffect

```TypeScript
default menuBackgroundEffect(effect: BackgroundEffectOptions | undefined): this
```

Defines the select menu's background effect with options

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuBackgroundEffect(effect: BackgroundEffectOptions | undefined): this--><!--Device-SelectAttribute-default menuBackgroundEffect(effect: BackgroundEffectOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effect | [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md) \| undefined | Yes | Background effect, including saturation, brightness, and color. &lt;br&gt;The configuration does not take effect when it is undefined. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The attribute of the select. |

## menuItemContentModifier

```TypeScript
default menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration> | undefined): this
```

Register a ContentModifier for each menu item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration> | undefined): this--><!--Device-SelectAttribute-default menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[MenuItemConfiguration](arkts-arkui-select-menuitemconfiguration-i.md)&gt; \| undefined | Yes | The content modifier of select menu item. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## menuOutline

```TypeScript
default menuOutline(outline: MenuOutlineOptions | undefined): this
```

Sets the outline of menu.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuOutline(outline: MenuOutlineOptions | undefined): this--><!--Device-SelectAttribute-default menuOutline(outline: MenuOutlineOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| outline | [MenuOutlineOptions](arkts-arkui-select-menuoutlineoptions-i.md) \| undefined | Yes | Set the outline of menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## menuSystemMaterial

```TypeScript
default menuSystemMaterial(material: SystemUiMaterial | undefined): this
```

Set system-styled materials for select's menu. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of select's menu.

Device Behavior Differences:The effect of the same material may vary across different devices depending on their computing power.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuSystemMaterial(material: SystemUiMaterial | undefined): this--><!--Device-SelectAttribute-default menuSystemMaterial(material: SystemUiMaterial | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| material | [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t.md) \| undefined | Yes | The select's menu material, undefined means retaining the original visual style of the select's menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The attribute of the select. |

## minKeyboardAvoidDistance

```TypeScript
default minKeyboardAvoidDistance(distance: LengthMetrics | undefined): this
```

Defines the minimum distance between select menu and keyboard.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default minKeyboardAvoidDistance(distance: LengthMetrics | undefined): this--><!--Device-SelectAttribute-default minKeyboardAvoidDistance(distance: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| distance | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | Yes | The minimum avoiding distance. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The attribute of the select. |

## onSelect

```TypeScript
default onSelect(callback: OnSelectCallback | undefined): this
```

Callback for selecting an item from the select.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default onSelect(callback: OnSelectCallback | undefined): this--><!--Device-SelectAttribute-default onSelect(callback: OnSelectCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSelectCallback](arkts-arkui-onselectcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## optionBgColor

```TypeScript
default optionBgColor(value: ResourceColor | undefined): this
```

Sets the background color of the select item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default optionBgColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default optionBgColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## optionFont

```TypeScript
default optionFont(value: Font | undefined): this
```

Sets the text style for select items.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default optionFont(value: Font | undefined): this--><!--Device-SelectAttribute-default optionFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## optionFontColor

```TypeScript
default optionFontColor(value: ResourceColor | undefined): this
```

Sets the text color for select items.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default optionFontColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default optionFontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## optionHeight

```TypeScript
default optionHeight(value: Dimension | undefined): this
```

Set the height of each option.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default optionHeight(value: Dimension | undefined): this--><!--Device-SelectAttribute-default optionHeight(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | The length of option height. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## optionTextModifier

```TypeScript
default optionTextModifier(modifier: TextModifier | undefined): this
```

Sets the attribute modifier for the text of each option.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default optionTextModifier(modifier: TextModifier | undefined): this--><!--Device-SelectAttribute-default optionTextModifier(modifier: TextModifier | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | TextModifier \| undefined | Yes | Set modifier for the text of each option. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## optionWidth

```TypeScript
default optionWidth(value: Dimension | OptionWidthMode | undefined): this
```

Set the width of each option and set whether the option width fit the trigger.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default optionWidth(value: Dimension | OptionWidthMode | undefined): this--><!--Device-SelectAttribute-default optionWidth(value: Dimension | OptionWidthMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| [OptionWidthMode](arkts-arkui-optionwidthmode-e.md) \| undefined | Yes | The length of option width and decide option width to fit trigger or content. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## selected

```TypeScript
default selected(numCount: int | Resource | undefined | Bindable<int> | Bindable<Resource>): this
```

Sets the serial number of the select item, starting from 0.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default selected(numCount: int | Resource | undefined | Bindable<int> | Bindable<Resource>): this--><!--Device-SelectAttribute-default selected(numCount: int | Resource | undefined | Bindable<int> | Bindable<Resource>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| numCount | int \| [Resource](arkts-arkui-resource-t.md) \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;int&gt; \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;[Resource](arkts-arkui-resource-t.md)&gt; | Yes | the serial number of the select item. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## selectedOptionBgColor

```TypeScript
default selectedOptionBgColor(value: ResourceColor | undefined): this
```

Sets the background color of the selected items in the select.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default selectedOptionBgColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default selectedOptionBgColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedOptionFont

```TypeScript
default selectedOptionFont(value: Font | undefined): this
```

Sets the text style of the selected items in the select.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default selectedOptionFont(value: Font | undefined): this--><!--Device-SelectAttribute-default selectedOptionFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedOptionFontColor

```TypeScript
default selectedOptionFontColor(value: ResourceColor | undefined): this
```

Sets the text color of the selected item in the select.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default selectedOptionFontColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default selectedOptionFontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedOptionTextModifier

```TypeScript
default selectedOptionTextModifier(modifier: TextModifier | undefined): this
```

Sets the attribute modifier for the text of selected option.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default selectedOptionTextModifier(modifier: TextModifier | undefined): this--><!--Device-SelectAttribute-default selectedOptionTextModifier(modifier: TextModifier | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | TextModifier \| undefined | Yes | Set modifier for the text of selected option. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## setSelectOptions

```TypeScript
default setSelectOptions(optionArray: Array<SelectOption>): this
```

Set select options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default setSelectOptions(optionArray: Array<SelectOption>): this--><!--Device-SelectAttribute-default setSelectOptions(optionArray: Array<SelectOption>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| optionArray | Array&lt;[SelectOption](arkts-arkui-select-selectoption-i.md)&gt; | Yes | select constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the SelectAttribute. |

## showDefaultSelectedIcon

```TypeScript
default showDefaultSelectedIcon(show:boolean | undefined): this
```

Set whether to display the default selected icon.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default showDefaultSelectedIcon(show:boolean | undefined): this--><!--Device-SelectAttribute-default showDefaultSelectedIcon(show:boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| show | boolean \| undefined | Yes | Set whether to display the default selection icon. true means display the default selected icon false or undefined means do not display the default selected icon, instead indicate selection by highlighting the background color. &lt;br&gt; show is set to true, if the background color of the selected option is set using selectedOptionBgColor, both the background color of the selected item and the default selection icon will be displayed. If the background color of the selected option is not set using selectedOptionBgColor, the background color will1 not be highlighted, and only the default selection icon will be displayed. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## showInSubWindow

```TypeScript
default showInSubWindow(showInSubWindow: boolean | undefined): this
```

Sets whether to display menu in the sub window.

Device Behavior Differences:Setting to display in sub windows is only supported on 2-in-1 devices.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default showInSubWindow(showInSubWindow: boolean | undefined): this--><!--Device-SelectAttribute-default showInSubWindow(showInSubWindow: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| showInSubWindow | boolean \| undefined | Yes | Set whether the Select menu is displayed in the sub window. true means the Select menu is displayed in the sub window, and this setting is only takes effect on 2-in-1 devices. false means the select menu is not displayed in the sub window. &lt;br&gt;Default value:2-in-1 device is true, other devices are false. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The attribute of the select. |

## space

```TypeScript
default space(value: Length | undefined): this
```

Set the space for text and icon in select

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default space(value: Length | undefined): this--><!--Device-SelectAttribute-default space(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | indicates the length of the space |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## textModifier

```TypeScript
default textModifier(modifier: TextModifier | undefined): this
```

Sets the attribute modifier for the text of select.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default textModifier(modifier: TextModifier | undefined): this--><!--Device-SelectAttribute-default textModifier(modifier: TextModifier | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | TextModifier \| undefined | Yes | Set modifier for the text of select. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## value

```TypeScript
default value(resStr: ResourceStr | undefined | Bindable<string> | Bindable<Resource>): this
```

Sets the text display of the select button itself.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default value(resStr: ResourceStr | undefined | Bindable<string> | Bindable<Resource>): this--><!--Device-SelectAttribute-default value(resStr: ResourceStr | undefined | Bindable<string> | Bindable<Resource>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resStr | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;string&gt; \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;[Resource](arkts-arkui-resource-t.md)&gt; | Yes | the text display of the select button itself. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

