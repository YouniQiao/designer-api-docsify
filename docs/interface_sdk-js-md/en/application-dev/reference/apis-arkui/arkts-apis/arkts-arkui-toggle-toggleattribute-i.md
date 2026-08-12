# ToggleAttribute

Defines the Toggle component attributes.

**Inheritance/Implementation:** ToggleAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ToggleAttribute extends CommonMethod--><!--Device-unnamed-export declare interface ToggleAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of toggle.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ToggleAttribute-default attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes | The attribute modifier of toggle. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this
```

Set the content modifier of toggle.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this--><!--Device-ToggleAttribute-default contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[ToggleConfiguration](arkts-arkui-toggle-toggleconfiguration-i.md)&gt; \| undefined | Yes | The content modifier of toggle. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((isOn: boolean) => void) | undefined): this
```

Called when the selected state of the component changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default onChange(callback: ((isOn: boolean) => void) | undefined): this--><!--Device-ToggleAttribute-default onChange(callback: ((isOn: boolean) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((isOn: boolean) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

Called when the color of the selected button is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default selectedColor(value: ResourceColor | undefined): this--><!--Device-ToggleAttribute-default selectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setToggleOptions

```TypeScript
default setToggleOptions(options: ToggleOptions): this
```

Set toggle options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default setToggleOptions(options: ToggleOptions): this--><!--Device-ToggleAttribute-default setToggleOptions(options: ToggleOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToggleOptions](arkts-arkui-toggle-toggleoptions-i.md) | Yes | toggle constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the ToggleAttribute. |

## switchPointColor

```TypeScript
default switchPointColor(color: ResourceColor | undefined): this
```

Called when the color of the selected button is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default switchPointColor(color: ResourceColor | undefined): this--><!--Device-ToggleAttribute-default switchPointColor(color: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## switchStyle

```TypeScript
default switchStyle(value: SwitchStyle | undefined): this
```

Set the style of the switch.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default switchStyle(value: SwitchStyle | undefined): this--><!--Device-ToggleAttribute-default switchStyle(value: SwitchStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SwitchStyle](arkts-arkui-toggle-switchstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

