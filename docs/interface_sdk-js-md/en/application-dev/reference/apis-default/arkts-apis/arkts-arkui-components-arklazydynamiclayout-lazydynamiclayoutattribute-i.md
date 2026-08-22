# LazyDynamicLayoutAttribute

The LazyDynamicLayoutAttribute

**Inheritance/Implementation:** LazyDynamicLayoutAttribute extends CommonMethod

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare interface LazyDynamicLayoutAttribute--><!--Device-unnamed-export declare interface LazyDynamicLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## attributeModifier

```TypeScript
attributeModifier(
      modifier: AttributeModifier<LazyDynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-LazyDynamicLayoutAttribute-attributeModifier(      modifier: AttributeModifier<LazyDynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-LazyDynamicLayoutAttribute-attributeModifier(      modifier: AttributeModifier<LazyDynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](arkts-common-attributemodifier-i.md)&lt;[LazyDynamicLayoutAttribute](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-arklazydynamiclayout-lazydynamiclayoutattribute-c.md)&gt; \| [AttributeModifier](arkts-common-attributemodifier-i.md)&lt;[CommonMethod](arkts-common-commonmethod-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onVisibleIndexesChange

```TypeScript
onVisibleIndexesChange(callback: Callback<int[]> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-LazyDynamicLayoutAttribute-onVisibleIndexesChange(callback: Callback<int[]> | undefined): this--><!--Device-LazyDynamicLayoutAttribute-onVisibleIndexesChange(callback: Callback<int[]> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-callback-t.md)&lt;int[]&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setLazyDynamicLayoutOptions

```TypeScript
setLazyDynamicLayoutOptions(algorithm: LazyLayoutAlgorithm): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-LazyDynamicLayoutAttribute-setLazyDynamicLayoutOptions(algorithm: LazyLayoutAlgorithm): this--><!--Device-LazyDynamicLayoutAttribute-setLazyDynamicLayoutOptions(algorithm: LazyLayoutAlgorithm): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithm | [LazyLayoutAlgorithm](../../apis-arkui/arkts-apis/arkts-arkui-lazylayoutalgorithm-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set LazyDynamicLayout options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyDynamicLayoutAttribute-default--><!--Device-LazyDynamicLayoutAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

