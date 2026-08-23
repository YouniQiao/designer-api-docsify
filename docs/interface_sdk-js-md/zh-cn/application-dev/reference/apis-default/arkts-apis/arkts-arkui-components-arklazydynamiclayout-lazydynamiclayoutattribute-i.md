# LazyDynamicLayoutAttribute

LazyDynamicLayout属性

**继承/实现关系：** LazyDynamicLayoutAttribute extends CommonMethod

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export declare interface LazyDynamicLayoutAttribute--><!--Device-unnamed-export declare interface LazyDynamicLayoutAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## attributeModifier

```TypeScript
attributeModifier(
      modifier: AttributeModifier<LazyDynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-LazyDynamicLayoutAttribute-attributeModifier(      modifier: AttributeModifier<LazyDynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-LazyDynamicLayoutAttribute-attributeModifier(      modifier: AttributeModifier<LazyDynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](arkts-common-attributemodifier-i.md)&lt;[LazyDynamicLayoutAttribute](arkts-arkui-components-arklazydynamiclayout-lazydynamiclayoutattribute-i.md)&gt; \| [AttributeModifier](arkts-common-attributemodifier-i.md)&lt;[CommonMethod](arkts-common-commonmethod-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onVisibleIndexesChange

```TypeScript
onVisibleIndexesChange(callback: Callback<int[]> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-LazyDynamicLayoutAttribute-onVisibleIndexesChange(callback: Callback<int[]> | undefined): this--><!--Device-LazyDynamicLayoutAttribute-onVisibleIndexesChange(callback: Callback<int[]> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-callback-t.md)&lt;int[]&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setLazyDynamicLayoutOptions

```TypeScript
setLazyDynamicLayoutOptions(algorithm: LazyLayoutAlgorithm): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-LazyDynamicLayoutAttribute-setLazyDynamicLayoutOptions(algorithm: LazyLayoutAlgorithm): this--><!--Device-LazyDynamicLayoutAttribute-setLazyDynamicLayoutOptions(algorithm: LazyLayoutAlgorithm): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algorithm | [LazyLayoutAlgorithm](../../apis-arkui/arkts-apis/arkts-arkui-lazylayoutalgorithm-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置LazyDynamicLayout选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LazyDynamicLayoutAttribute-default--><!--Device-LazyDynamicLayoutAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

