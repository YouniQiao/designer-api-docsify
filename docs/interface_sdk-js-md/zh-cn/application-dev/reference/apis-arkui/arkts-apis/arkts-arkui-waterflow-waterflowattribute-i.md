# WaterFlowAttribute

除支持通用属性和滚动组件通用属性外，还支持 以下属性：

> **说明：**&gt;
> WaterFlow组件使用通用属性clip&lt;sup&gt;12+&lt;/sup&gt;和通用属性
> clip&lt;sup&gt;18+&lt;/sup&gt;时默认值都为true。&gt;
> WaterFlow组件内容裁剪模式ContentClipMode&lt;sup&gt;14+&lt;/sup&gt;枚举说明为ContentClipMode.CONTENT_ONLY，padding区域会
> 被裁剪不显示。

**继承/实现关系：** WaterFlowAttribute extends ScrollableCommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<WaterFlowAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置WaterFlow组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[WaterFlowAttribute](arkts-arkui-waterflow-waterflowattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## cachedCount

```TypeScript
default cachedCount(value: int | undefined): this
```

设置预加载的FlowItem数量。只在[LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)和开启了 [virtualScroll](../../../reference/apis-arkui/arkui-ts/ts-rendering-control-repeat.md#virtualscroll)开关的 [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)中生效，超出显示及缓存范围的FlowItem会被释放。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## cachedCount

```TypeScript
default cachedCount(count: int | undefined, show: boolean | undefined): this
```

设置预加载的FlowItem数量，并配置是否显示预加载节点。配合[clip或 clipContent属性可以显示出预加载节 点。只在[LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)和开启了 [virtualScroll](../../../reference/apis-arkui/arkui-ts/ts-rendering-control-repeat.md#virtualscroll)开关的 [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)中生效，超出显示及缓存范围的FlowItem会被释放。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | int \| undefined | 是 |
| show | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## columnsGap

```TypeScript
default columnsGap(value: Length | undefined): this
```

设置列与列的间距。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## columnsTemplate

```TypeScript
default columnsTemplate(value: string | ItemFillPolicy | undefined): this
```

设置当前瀑布流组件布局列的数量，不设置时默认1列。当value设置为string类型时，使用方法参考[columnsTemplate(value: string)](#columnstemplate)。当value设置为ItemFillPolicy类型时，将根据WaterFlow组件宽度对应[断点类型](../../../ui/arkts-layout-development-grid-layout.md#栅格容器断点)确 定列数。例如，ItemFillPolicy.BREAKPOINT_DEFAULT在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列，且每列均为1fr。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [ItemFillPolicy](arkts-arkui-itemfillpolicy-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## itemConstraintSize

```TypeScript
default itemConstraintSize(value: ConstraintSizeOptions | undefined): this
```

设置约束尺寸，子组件布局时，进行尺寸范围限制。使用方法参考[示例1](../../../reference/apis-arkui/arkui-ts/ts-container-waterflow.md#示例1使用基本瀑布流)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ConstraintSizeOptions](arkts-arkui-constraintsizeoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## layoutDirection

```TypeScript
default layoutDirection(value: FlexDirection | undefined): this
```

设置布局的主轴方向。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [FlexDirection](arkts-arkui-flexdirection-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDidScroll

```TypeScript
default onDidScroll(handler: OnScrollCallback | undefined): this
```

WaterFlow滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnScrollCallback](../arkts-components/arkts-arkui-onscrollcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollFrameBegin

```TypeScript
default onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this
```

该接口回调时，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，瀑布流将按照返回值的实际滑动量进行滑动。满足以下任一条件时触发该事件：
1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
2. WaterFlow惯性滚动。
3. 调用fling接口触发滚动。
不触发该事件的条件：
1. 调用除fling接口外的其他滚动控制接口。
2. 越界回弹。
3. 拖动滚动条。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnScrollFrameBeginCallback](../arkts-components/arkts-arkui-onscrollframebegincallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollIndex

```TypeScript
default onScrollIndex(event: ((first: int, last: int) => void) | undefined): this
```

当前瀑布流显示的起始位置/终止位置的子组件发生变化时触发。瀑布流初始化时会触发一次。瀑布流显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。

> **说明：**&gt;
> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((first: int, last: int) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onWillScroll

```TypeScript
default onWillScroll(handler: OnWillScrollCallback | undefined): this
```

滚动事件回调，WaterFlow滚动前触发。回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定滚动组件将要滚动的偏移。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnWillScrollCallback](../arkts-components/arkts-arkui-onwillscrollcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## rowsGap

```TypeScript
default rowsGap(value: Length | undefined): this
```

设置行与行的间距。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## rowsTemplate

```TypeScript
default rowsTemplate(value: string | undefined): this
```

设置当前瀑布流组件布局行的数量，不设置时默认1行。例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。可使用rowsTemplate('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支 持的单位包括px、vp、%或有效数字，默认单位为vp。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setWaterFlowOptions

```TypeScript
default setWaterFlowOptions(options?: WaterFlowOptions): this
```

设置WaterFlow选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [WaterFlowOptions](arkts-arkui-waterflow-waterflowoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [WaterFlowAttribute](arkts-arkui-waterflow-waterflowattribute-i.md) |

## supportEmptyBranchInLazyLoading

```TypeScript
default supportEmptyBranchInLazyLoading(supported: boolean | undefined): this
```

设置当前WaterFlow组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。未设置时不支持空分支节点。此属性初次赋值后不支持更新，所以赋值后无法在支持空分支、不 支持空分支行为之间切换。

> **说明：**&gt;
> 当通过[sections](../../../reference/apis-arkui/arkui-ts/ts-container-waterflow.md#waterflowoptions对象说明)参数设置了
> [WaterFlowSections](arkts-arkui-waterflow-waterflowsections-c.md)分组，或通过
> [layoutMode](../../../reference/apis-arkui/arkui-ts/ts-container-waterflow.md#waterflowoptions对象说明)设置
> [SLIDING_WINDOW](arkts-arkui-waterflow-waterflowlayoutmode-e.md)布局模式时，supportEmptyBranchInLazyLoading设为true、false、undefined或不设置
> supportEmptyBranchInLazyLoading，空分支后的FlowItem都会显示。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| supported | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## syncLoad

```TypeScript
default syncLoad(enable: boolean | undefined): this
```

设置是否同步加载WaterFlow区域内所有子组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
