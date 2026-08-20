# WaterFlowAttribute

除支持通用属性和[滚动组件通用属性](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#属性)外，还支持 以下属性：

> **说明：**
> 
> WaterFlow组件使用通用属性clip&lt;sup&gt;12+&lt;/sup&gt;和通用属性 &gt; clip&lt;sup&gt;18+&lt;/sup&gt;时默认值都为true。
> 
> WaterFlow组件内容裁剪模式ContentClipMode&lt;sup&gt;14+&lt;/sup&gt;枚举说明为ContentClipMode.CONTENT_ONLY，padding区域会 &gt; 被裁剪不显示。

**继承/实现关系：** WaterFlowAttribute extends ScrollableCommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface WaterFlowAttribute--><!--Device-unnamed-export declare interface WaterFlowAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<WaterFlowAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-attributeModifier(modifier: AttributeModifier<WaterFlowAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-WaterFlowAttribute-attributeModifier(modifier: AttributeModifier<WaterFlowAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[WaterFlowAttribute](arkts-waterflow-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## cachedCount

```TypeScript
cachedCount(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-cachedCount(value: int | undefined): this--><!--Device-WaterFlowAttribute-cachedCount(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## cachedCount

```TypeScript
cachedCount(count: int | undefined, show: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-cachedCount(count: int | undefined, show: boolean | undefined): this--><!--Device-WaterFlowAttribute-cachedCount(count: int | undefined, show: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | int \| undefined | 是 |  |
| show | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## columnsGap

```TypeScript
columnsGap(value: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-columnsGap(value: Length | undefined): this--><!--Device-WaterFlowAttribute-columnsGap(value: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## columnsTemplate

```TypeScript
columnsTemplate(value: string | ItemFillPolicy | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-columnsTemplate(value: string | ItemFillPolicy | undefined): this--><!--Device-WaterFlowAttribute-columnsTemplate(value: string | ItemFillPolicy | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| [ItemFillPolicy](../../apis-arkui/arkts-apis/arkts-arkui-itemfillpolicy-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## itemConstraintSize

```TypeScript
itemConstraintSize(value: ConstraintSizeOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-itemConstraintSize(value: ConstraintSizeOptions | undefined): this--><!--Device-WaterFlowAttribute-itemConstraintSize(value: ConstraintSizeOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ConstraintSizeOptions](../../apis-arkui/arkts-apis/arkts-arkui-constraintsizeoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## layoutDirection

```TypeScript
layoutDirection(value: FlexDirection | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-layoutDirection(value: FlexDirection | undefined): this--><!--Device-WaterFlowAttribute-layoutDirection(value: FlexDirection | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FlexDirection](../../apis-arkui/arkts-apis/arkts-arkui-flexdirection-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDidScroll

```TypeScript
onDidScroll(handler: OnScrollCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-onDidScroll(handler: OnScrollCallback | undefined): this--><!--Device-WaterFlowAttribute-onDidScroll(handler: OnScrollCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnScrollCallback](../../apis-arkui/arkts-components/arkts-arkui-onscrollcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollFrameBegin

```TypeScript
onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this--><!--Device-WaterFlowAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](../../apis-arkui/arkts-components/arkts-arkui-onscrollframebegincallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollIndex

```TypeScript
onScrollIndex(event: ((first: int, last: int) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-onScrollIndex(event: ((first: int, last: int) => void) | undefined): this--><!--Device-WaterFlowAttribute-onScrollIndex(event: ((first: int, last: int) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((first: int, last: int) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onWillScroll

```TypeScript
onWillScroll(handler: OnWillScrollCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-onWillScroll(handler: OnWillScrollCallback | undefined): this--><!--Device-WaterFlowAttribute-onWillScroll(handler: OnWillScrollCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnWillScrollCallback](../../apis-arkui/arkts-components/arkts-arkui-onwillscrollcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## rowsGap

```TypeScript
rowsGap(value: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-rowsGap(value: Length | undefined): this--><!--Device-WaterFlowAttribute-rowsGap(value: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## rowsTemplate

```TypeScript
rowsTemplate(value: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-rowsTemplate(value: string | undefined): this--><!--Device-WaterFlowAttribute-rowsTemplate(value: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setWaterFlowOptions

```TypeScript
setWaterFlowOptions(options?: WaterFlowOptions): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-setWaterFlowOptions(options?: WaterFlowOptions): this--><!--Device-WaterFlowAttribute-setWaterFlowOptions(options?: WaterFlowOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [WaterFlowOptions](arkts-waterflow-waterflowoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## supportEmptyBranchInLazyLoading

```TypeScript
supportEmptyBranchInLazyLoading(supported: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-supportEmptyBranchInLazyLoading(supported: boolean | undefined): this--><!--Device-WaterFlowAttribute-supportEmptyBranchInLazyLoading(supported: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supported | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## syncLoad

```TypeScript
syncLoad(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-WaterFlowAttribute-syncLoad(enable: boolean | undefined): this--><!--Device-WaterFlowAttribute-syncLoad(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

动态设置WaterFlow组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WaterFlowAttribute-default--><!--Device-WaterFlowAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

