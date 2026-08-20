# ScrollBarAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** ScrollBarAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface ScrollBarAttribute--><!--Device-unnamed-export declare interface ScrollBarAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ScrollBarAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ScrollBarAttribute-attributeModifier(modifier: AttributeModifier<ScrollBarAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ScrollBarAttribute-attributeModifier(modifier: AttributeModifier<ScrollBarAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ScrollBarAttribute](arkts-scrollbar-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableNestedScroll

```TypeScript
enableNestedScroll(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ScrollBarAttribute-enableNestedScroll(enabled: boolean | undefined): this--><!--Device-ScrollBarAttribute-enableNestedScroll(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollBarColor

```TypeScript
scrollBarColor(color: ColorMetrics | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ScrollBarAttribute-scrollBarColor(color: ColorMetrics | undefined): this--><!--Device-ScrollBarAttribute-scrollBarColor(color: ColorMetrics | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ColorMetrics](../arkts-apis/arkts-graphics-colormetrics-c.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setScrollBarOptions

```TypeScript
setScrollBarOptions(value: ScrollBarOptions): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ScrollBarAttribute-setScrollBarOptions(value: ScrollBarOptions): this--><!--Device-ScrollBarAttribute-setScrollBarOptions(value: ScrollBarOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollBarOptions](arkts-scrollbar-scrollbaroptions-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

动态设置ScrollBar组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ScrollBarAttribute-default--><!--Device-ScrollBarAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

