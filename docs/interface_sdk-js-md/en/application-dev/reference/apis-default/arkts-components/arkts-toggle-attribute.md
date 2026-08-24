# ToggleAttribute

Defines the Toggle component attributes.@extends CommonMethod @interface ToggleAttribute

**Inheritance/Implementation:** ToggleAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface ToggleAttribute--><!--Device-unnamed-export declare interface ToggleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ToggleAttribute-attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ToggleAttribute-attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ToggleAttribute](arkts-toggle-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ToggleAttribute-contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this--><!--Device-ToggleAttribute-contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[ToggleConfiguration](arkts-toggle-toggleconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onChange

```TypeScript
onChange(callback: ((isOn: boolean) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ToggleAttribute-onChange(callback: ((isOn: boolean) => void) | undefined): this--><!--Device-ToggleAttribute-onChange(callback: ((isOn: boolean) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((isOn: boolean) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selectedColor

```TypeScript
selectedColor(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ToggleAttribute-selectedColor(value: ResourceColor | undefined): this--><!--Device-ToggleAttribute-selectedColor(value: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setToggleOptions

```TypeScript
setToggleOptions(options: ToggleOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ToggleAttribute-setToggleOptions(options: ToggleOptions): this--><!--Device-ToggleAttribute-setToggleOptions(options: ToggleOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToggleOptions](arkts-toggle-toggleoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## switchPointColor

```TypeScript
switchPointColor(color: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ToggleAttribute-switchPointColor(color: ResourceColor | undefined): this--><!--Device-ToggleAttribute-switchPointColor(color: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## switchStyle

```TypeScript
switchStyle(value: SwitchStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ToggleAttribute-switchStyle(value: SwitchStyle | undefined): this--><!--Device-ToggleAttribute-switchStyle(value: SwitchStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SwitchStyle](arkts-toggle-switchstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set toggle options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default--><!--Device-ToggleAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

