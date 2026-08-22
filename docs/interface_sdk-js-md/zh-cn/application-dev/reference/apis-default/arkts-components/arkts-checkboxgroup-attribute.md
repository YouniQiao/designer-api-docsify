# CheckboxGroupAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** CheckboxGroupAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface CheckboxGroupAttribute--><!--Device-unnamed-export declare interface CheckboxGroupAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(
        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CheckboxGroupAttribute-attributeModifier(        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CheckboxGroupAttribute-attributeModifier(        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CheckboxGroupAttribute](arkts-checkboxgroup-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## checkboxShape

```TypeScript
checkboxShape(value: CheckBoxShape | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CheckboxGroupAttribute-checkboxShape(value: CheckBoxShape | undefined): this--><!--Device-CheckboxGroupAttribute-checkboxShape(value: CheckBoxShape | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CheckBoxShape](../../apis-arkui/arkts-apis/arkts-arkui-checkboxshape-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CheckboxGroupAttribute-contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this--><!--Device-CheckboxGroupAttribute-contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[CheckBoxGroupConfiguration](arkts-checkboxgroup-checkboxgroupconfiguration-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## mark

```TypeScript
mark(value: MarkStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CheckboxGroupAttribute-mark(value: MarkStyle | undefined): this--><!--Device-CheckboxGroupAttribute-mark(value: MarkStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [MarkStyle](../../apis-arkui/arkts-apis/arkts-arkui-markstyle-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onChange

```TypeScript
onChange(callback: OnCheckboxGroupChangeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CheckboxGroupAttribute-onChange(callback: OnCheckboxGroupChangeCallback | undefined): this--><!--Device-CheckboxGroupAttribute-onChange(callback: OnCheckboxGroupChangeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnCheckboxGroupChangeCallback](arkts-oncheckboxgroupchangecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectAll

```TypeScript
selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CheckboxGroupAttribute-selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this--><!--Device-CheckboxGroupAttribute-selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAllSelected | boolean \| undefined \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;boolean&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectedColor

```TypeScript
selectedColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CheckboxGroupAttribute-selectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxGroupAttribute-selectedColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## unselectedColor

```TypeScript
unselectedColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CheckboxGroupAttribute-unselectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxGroupAttribute-unselectedColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置CheckboxGroup的内容修饰器。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CheckboxGroupAttribute-default--><!--Device-CheckboxGroupAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

