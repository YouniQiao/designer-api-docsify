# GridItemAttribute

The GridItemAttribute.

**继承/实现关系：** GridItemAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface GridItemAttribute--><!--Device-unnamed-export declare interface GridItemAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<GridItemAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridItemAttribute-attributeModifier(modifier: AttributeModifier<GridItemAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-GridItemAttribute-attributeModifier(modifier: AttributeModifier<GridItemAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[GridItemAttribute](arkts-griditem-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## columnEnd

```TypeScript
columnEnd(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridItemAttribute-columnEnd(value: int | undefined): this--><!--Device-GridItemAttribute-columnEnd(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## columnStart

```TypeScript
columnStart(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridItemAttribute-columnStart(value: int | undefined): this--><!--Device-GridItemAttribute-columnStart(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onSelect

```TypeScript
onSelect(event: ((isSelected: boolean) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridItemAttribute-onSelect(event: ((isSelected: boolean) => void) | undefined): this--><!--Device-GridItemAttribute-onSelect(event: ((isSelected: boolean) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((isSelected: boolean) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## rowEnd

```TypeScript
rowEnd(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridItemAttribute-rowEnd(value: int | undefined): this--><!--Device-GridItemAttribute-rowEnd(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## rowStart

```TypeScript
rowStart(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridItemAttribute-rowStart(value: int | undefined): this--><!--Device-GridItemAttribute-rowStart(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectable

```TypeScript
selectable(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridItemAttribute-selectable(value: boolean | undefined): this--><!--Device-GridItemAttribute-selectable(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selected

```TypeScript
selected(value: boolean | Bindable<boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridItemAttribute-selected(value: boolean | Bindable<boolean> | undefined): this--><!--Device-GridItemAttribute-selected(value: boolean | Bindable<boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setGridItemOptions

```TypeScript
setGridItemOptions(value?: GridItemOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridItemAttribute-setGridItemOptions(value?: GridItemOptions): this--><!--Device-GridItemAttribute-setGridItemOptions(value?: GridItemOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [GridItemOptions](arkts-griditem-griditemoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

动态设置GridItem组件的属性方法。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GridItemAttribute-default--><!--Device-GridItemAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

