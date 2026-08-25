# WaterFlow属性/事件

除支持通用属性和滚动组件通用属性外，还 支持以下属性：除支持通用事件和[滚动组件通用事件](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#事件)外，还 支持以下事件：

**继承/实现关系：** WaterFlowAttribute extends ScrollableCommonMethod<WaterFlowAttribute>

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## cachedCount

```TypeScript
cachedCount(value: number)
```

设置预加载的FlowItem数量。只在[LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)和开启了 virtualScroll开关的 [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)中生效，超出显示及缓存范围的FlowItem会被释放。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## cachedCount

```TypeScript
cachedCount(count: number, show: boolean)
```

设置预加载的FlowItem数量，并配置是否显示预加载节点。配合[clip或 clipContent属性可以显示出预加载节点。只在[LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)和开启了virtualScroll开关的 [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)中生效，超出显示及缓存范围的FlowItem会被释放。

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为14。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | number | 是 |
| show | boolean | 是 |

## columnsGap

```TypeScript
columnsGap(value: Length)
```

设置列与列的间距。使用分组布局时，各分组可通过SectionOptions.columnsGap单独设置列间距覆盖此值。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## columnsTemplate

```TypeScript
columnsTemplate(value: string)
```

设置当前瀑布流组件布局列的数量，不设置时默认1列。当[layoutDirection](#layoutdirection)设置为横向布局（FlexDirection.Row或 FlexDirection.RowReverse）时，columnsTemplate不生效，由[rowsTemplate](#rowstemplate)控制布局。使用 [sections](arkts-arkui-waterflowoptions-i.md)分组混合布局时，此属性会被忽略。例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。可使用columnsTemplate('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度， 支持的单位包括px、vp、%或有效数字，默认单位为vp，使用方法参见 [示例2](../../../reference/apis-arkui/arkui-ts/ts-container-waterflow.md#示例2自动计算列数)。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

## columnsTemplate

```TypeScript
columnsTemplate(value: string | ItemFillPolicy)
```

设置当前瀑布流组件布局列的数量，不设置时默认1列。当[layoutDirection](#layoutdirection)设置为横向布局（FlexDirection.Row或 FlexDirection.RowReverse）时，columnsTemplate不生效，由[rowsTemplate](#rowstemplate)控制布局。使用 [sections](arkts-arkui-waterflowoptions-i.md)分组混合布局时，此属性会被忽略。当value设置为string类型时，使用方法参考[columnsTemplate(value: string)](#columnstemplate)。当value设置为ItemFillPolicy类型时，将根据WaterFlow组件宽度对应[断点类型](../../../ui/arkts-layout-development-grid-layout.md#栅格容器断点)确定列 数。例如，将ItemFillPolicy的fillType属性设置为PresetFillType.BREAKPOINT_DEFAULT时，在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区 间时显示5列，且每列均为1fr。

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为22。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [ItemFillPolicy](../arkts-apis/arkts-arkui-itemfillpolicy-i.md) | 是 |

## enableScrollInteraction

```TypeScript
enableScrollInteraction(value: boolean)
```

设置是否支持滚动手势。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## friction

```TypeScript
friction(value: number | Resource)
```

设置摩擦系数，手动滑动滚动区域时生效，仅影响惯性滚动过程，对嵌套滚动时惯性向父组件传递的联动效果有间接影响。适用于需要调整瀑布流滑动惯性效果的场景。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## itemConstraintSize

```TypeScript
itemConstraintSize(value: ConstraintSizeOptions)
```

设置约束尺寸，用于在子组件布局时限制其尺寸范围。使用方法参考[示例1](../../../reference/apis-arkui/arkui-ts/ts-container-waterflow.md#示例1使用基本瀑布流)。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ConstraintSizeOptions](../arkts-apis/arkts-arkui-constraintsizeoptions-i.md) | 是 |

## layoutDirection

```TypeScript
layoutDirection(value: FlexDirection)
```

设置布局的主轴方向。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [FlexDirection](../arkts-apis/arkts-arkui-flexdirection-e.md) | 是 |

## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions)
```

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。使用方法参考 [嵌套滚动实现方式二](../../../reference/apis-arkui/arkui-ts/ts-container-scroll.md#示例3嵌套滚动实现方式二)。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NestedScrollOptions](../arkts-apis/arkts-arkui-common-nestedscrolloptions-i.md) | 是 |

## onReachEnd

```TypeScript
onReachEnd(event: () => void)
```

瀑布流内容到达末尾位置时触发。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

## onReachStart

```TypeScript
onReachStart(event: () => void)
```

瀑布流内容到达起始位置时触发。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

## onScrollFrameBegin

```TypeScript
onScrollFrameBegin(event: OnScrollFrameBeginCallback)
```

该接口回调时，事件参数传入即将发生的滑动量。事件处理函数可根据应用场景计算实际需要的滑动量，并返回该值。瀑布流将按照返回的实际滑动量进行滑动。适用于需要自定义滚动行为的场景，例如按比例调整单帧滑动量，或在特定条件下阻止本帧滑动。满足以下任一条件时触发该事件：
1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
2. WaterFlow惯性滚动。
3. 调用fling接口触发滚动。
不触发该事件的条件：
1. 调用除fling接口外的其他滚动控制接口。
2. 越界回弹。
3. 拖动滚动条。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnScrollFrameBeginCallback](arkts-arkui-onscrollframebegincallback-t.md) | 是 |

## onScrollIndex

```TypeScript
onScrollIndex(event: (first: number, last: number) => void)
```

当前瀑布流显示的起始位置/终止位置的子组件发生变化时触发。瀑布流初始化时会触发一次。瀑布流显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。

> **说明：**&gt;
> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (first: number, last: number) = & gt; void | 是 |

## rowsGap

```TypeScript
rowsGap(value: Length)
```

设置行与行的间距。使用分组布局时，各分组可通过SectionOptions.rowsGap单独设置行间距覆盖此值。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## rowsTemplate

```TypeScript
rowsTemplate(value: string)
```

设置当前瀑布流组件布局行的数量，不设置时默认1行。当[layoutDirection](#layoutdirection)设置为纵向布局（FlexDirection.Column或 FlexDirection.ColumnReverse）或不设置时，rowsTemplate不生效，由 [columnsTemplate](#columnstemplate)控制布局。使用[sections](arkts-arkui-waterflowoptions-i.md) 分组混合布局时，此属性会被忽略。例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。可使用rowsTemplate('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的 单位包括px、vp、%或有效数字，默认单位为vp。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

## supportEmptyBranchInLazyLoading

```TypeScript
supportEmptyBranchInLazyLoading(supported: boolean | undefined)
```

设置当前WaterFlow组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。未设置时不支持空分支节点。此属性初次赋值后不支持更新，所以赋值后无法在支持空分支、不支持 空分支行为之间切换。

> **说明：**&gt;
> 当通过[sections](arkts-arkui-waterflowoptions-i.md)参数设置了[WaterFlowSections](arkts-arkui-waterflowsections-c.md)分组，或通过
> [layoutMode](arkts-arkui-waterflowoptions-i.md)设置[SLIDING_WINDOW](arkts-arkui-waterflowlayoutmode-e.md)布局模式时，无论
> supportEmptyBranchInLazyLoading设为何值或未设置，空分支后的FlowItem都会显示。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| supported | boolean \| undefined | 是 |

## syncLoad

```TypeScript
syncLoad(enable: boolean)
```

设置是否同步加载WaterFlow区域内所有子组件。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
