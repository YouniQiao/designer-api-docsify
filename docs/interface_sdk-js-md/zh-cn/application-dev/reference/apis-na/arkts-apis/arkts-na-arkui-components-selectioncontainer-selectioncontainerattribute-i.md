# SelectionContainerAttribute

支持[通用属性](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md)。 &gt; **说明：** &gt; &gt; - 不支持[隐私遮罩](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-obscured.md)。 &gt; &gt; - 不支持[图形变换](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-transformation.md)，跨节点场景中Text子组件不支持图形变 &gt; 换。

**继承/实现关系：** SelectionContainerAttribute extends CommonMethod

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare interface SelectionContainerAttribute--><!--Device-unnamed-export declare interface SelectionContainerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>
    | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>    | undefined): this--><!--Device-SelectionContainerAttribute-attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>    | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | AttributeModifier&lt;[SelectionContainerAttribute](arkts-na-arkui-components-selectioncontainer-selectioncontainerattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## bindSelectionMenu

```TypeScript
bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,
    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this--><!--Device-SelectionContainerAttribute-bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spanType | TextSpanType \| undefined | 是 |  |
| content | CustomBuilder \| undefined | 是 |  |
| responseType | TextResponseType \| undefined | 是 |  |
| options | [SelectionContainerMenuOptions](arkts-na-arkui-components-selectioncontainer-selectioncontainermenuoptions-i.md) \| undefined | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## caretColor

```TypeScript
caretColor(color: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-caretColor(color: ResourceColor | undefined): this--><!--Device-SelectionContainerAttribute-caretColor(color: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | ResourceColor \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## copyOption

```TypeScript
copyOption(value: CopyOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-copyOption(value: CopyOptions | undefined): this--><!--Device-SelectionContainerAttribute-copyOption(value: CopyOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | CopyOptions \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## editMenuOptions

```TypeScript
editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this--><!--Device-SelectionContainerAttribute-editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| editMenu | [SelectionContainerEditMenuOptions](arkts-na-arkui-components-selectioncontainer-selectioncontainereditmenuoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableHapticFeedback

```TypeScript
enableHapticFeedback(isEnabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-enableHapticFeedback(isEnabled: boolean | undefined): this--><!--Device-SelectionContainerAttribute-enableHapticFeedback(isEnabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onCopy

```TypeScript
onCopy(callback: Callback<string> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-onCopy(callback: Callback<string> | undefined): this--><!--Device-SelectionContainerAttribute-onCopy(callback: Callback<string> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onTextSelectionChange

```TypeScript
onTextSelectionChange(callback: Callback<Array<string>> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-onTextSelectionChange(callback: Callback<Array<string>> | undefined): this--><!--Device-SelectionContainerAttribute-onTextSelectionChange(callback: Callback<Array<string>> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;Array&lt;string&gt;&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onWillCopy

```TypeScript
onWillCopy(callback: Callback<string, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-onWillCopy(callback: Callback<string, boolean> | undefined): this--><!--Device-SelectionContainerAttribute-onWillCopy(callback: Callback<string, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;string, boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(color: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-selectedBackgroundColor(color: ResourceColor | undefined): this--><!--Device-SelectionContainerAttribute-selectedBackgroundColor(color: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | ResourceColor \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setSelectionContainerOptions

```TypeScript
setSelectionContainerOptions(): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-setSelectionContainerOptions(): this--><!--Device-SelectionContainerAttribute-setSelectionContainerOptions(): this-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
## textJoinStyle

```TypeScript
textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-SelectionContainerAttribute-textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this--><!--Device-SelectionContainerAttribute-textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [SelectionContainerTextJoinStyle](arkts-na-arkui-components-selectioncontainer-selectioncontainertextjoinstyle-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置SelectionContainer选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectionContainerAttribute-default--><!--Device-SelectionContainerAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

