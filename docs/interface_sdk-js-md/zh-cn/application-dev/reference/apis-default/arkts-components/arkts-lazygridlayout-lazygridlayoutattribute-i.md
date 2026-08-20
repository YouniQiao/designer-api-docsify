# LazyGridLayoutAttribute

LazyGridLayout组件属性。

**继承/实现关系：** LazyGridLayoutAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface LazyGridLayoutAttribute--><!--Device-unnamed-export declare interface LazyGridLayoutAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## columnsGap

```TypeScript
columnsGap(value: LengthMetrics | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LazyGridLayoutAttribute-columnsGap(value: LengthMetrics | undefined): this--><!--Device-LazyGridLayoutAttribute-columnsGap(value: LengthMetrics | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](../arkts-apis/arkts-graphics-lengthmetrics-c.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## footer

```TypeScript
footer(builder: CustomBuilder | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LazyGridLayoutAttribute-footer(builder: CustomBuilder | undefined): this--><!--Device-LazyGridLayoutAttribute-footer(builder: CustomBuilder | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## header

```TypeScript
header(builder: CustomBuilder | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LazyGridLayoutAttribute-header(builder: CustomBuilder | undefined): this--><!--Device-LazyGridLayoutAttribute-header(builder: CustomBuilder | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onVisibleIndexesChange

```TypeScript
onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LazyGridLayoutAttribute-onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this--><!--Device-LazyGridLayoutAttribute-onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnVisibleIndexesChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-onvisibleindexeschangecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## rowsGap

```TypeScript
rowsGap(value: LengthMetrics | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LazyGridLayoutAttribute-rowsGap(value: LengthMetrics | undefined): this--><!--Device-LazyGridLayoutAttribute-rowsGap(value: LengthMetrics | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](../arkts-apis/arkts-graphics-lengthmetrics-c.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## sticky

```TypeScript
sticky(sticky: StickyStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LazyGridLayoutAttribute-sticky(sticky: StickyStyle | undefined): this--><!--Device-LazyGridLayoutAttribute-sticky(sticky: StickyStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sticky | [StickyStyle](../../apis-arkui/arkts-components/arkts-arkui-stickystyle-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

当可视区域内子组件的索引值发生变化时触发回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LazyGridLayoutAttribute-default--><!--Device-LazyGridLayoutAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

