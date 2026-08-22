# ListItemAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** ListItemAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface ListItemAttribute--><!--Device-unnamed-export declare interface ListItemAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ListItemAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListItemAttribute-attributeModifier(modifier: AttributeModifier<ListItemAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ListItemAttribute-attributeModifier(modifier: AttributeModifier<ListItemAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ListItemAttribute](arkts-listitem-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onSelect

```TypeScript
onSelect(event: ((isSelected: boolean) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListItemAttribute-onSelect(event: ((isSelected: boolean) => void) | undefined): this--><!--Device-ListItemAttribute-onSelect(event: ((isSelected: boolean) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((isSelected: boolean) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectable

```TypeScript
selectable(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListItemAttribute-selectable(value: boolean | undefined): this--><!--Device-ListItemAttribute-selectable(value: boolean | undefined): this-End-->

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

<!--Device-ListItemAttribute-selected(value: boolean | Bindable<boolean> | undefined): this--><!--Device-ListItemAttribute-selected(value: boolean | Bindable<boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setListItemOptions

```TypeScript
setListItemOptions(value?: ListItemOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListItemAttribute-setListItemOptions(value?: ListItemOptions): this--><!--Device-ListItemAttribute-setListItemOptions(value?: ListItemOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ListItemOptions](arkts-listitem-listitemoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## swipeAction

```TypeScript
swipeAction(value: SwipeActionOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListItemAttribute-swipeAction(value: SwipeActionOptions | undefined): this--><!--Device-ListItemAttribute-swipeAction(value: SwipeActionOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SwipeActionOptions](arkts-listitem-swipeactionoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

动态设置ListItem组件的属性方法。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListItemAttribute-default--><!--Device-ListItemAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

