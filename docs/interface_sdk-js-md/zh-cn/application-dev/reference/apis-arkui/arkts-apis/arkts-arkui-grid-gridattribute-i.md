# GridAttribute

除支持通用属性和滚动组件通用属性外，还支持 以下属性：

> **说明：**&gt;
> Grid组件使用通用属性clip&lt;sup&gt;12+&lt;/sup&gt;和通用属性
> clip&lt;sup&gt;18+&lt;/sup&gt;时默认值都为true。&gt;
> 设置Grid的padding后，如果子组件部分位于Grid内容区且部分位于padding区域内，则会显示；如果子组件完全位于padding区域内，则不会显示。如下图所示，GridItem1显示，而GridItem2不显示。&gt;
> 

**继承/实现关系：** GridAttribute extends ScrollableCommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignItems

```TypeScript
default alignItems(alignment: GridItemAlignment | undefined): this
```

设置Grid中GridItem的对齐方式， 使用方法可以参考 [示例9](../../../reference/apis-arkui/arkui-ts/ts-container-grid.md#示例9以当前行最高的griditem的高度为其他griditem的高度)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alignment | [GridItemAlignment](arkts-arkui-grid-griditemalignment-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<GridAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置Grid组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[GridAttribute](arkts-arkui-grid-gridattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## cachedCount

```TypeScript
default cachedCount(value: int | undefined): this
```

设置预加载的GridItem的数量，只在[LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)和开启了 [virtualScroll](../../../reference/apis-arkui/arkui-ts/ts-rendering-control-repeat.md#virtualscroll)开关的 [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)中生效。<!--Del-->具体使用可参考 [减少应用白块说明](../../../performance/arkts-performance-improvement-recommendation.md#减少应用滑动白块)。<!--DelEnd-->设置缓存后会在Grid显示区域上下各缓存cachedCount*列数个GridItem。  
[LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)和开启了 [virtualScroll](../../../reference/apis-arkui/arkui-ts/ts-rendering-control-repeat.md#virtualscroll)开关的 [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)超出显示和缓存范围的GridItem会被释放。

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

设置预加载的GridItem数量，并配置是否显示预加载节点。设置缓存后会在Grid显示区域上下各缓存cachedCount*列数个GridItem。配合裁剪clip或内容裁剪 clipContent属性可以显示出预加载节 点。

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

## cellLength

```TypeScript
default cellLength(value: double | undefined): this
```

设置一行的高度或者一列的宽度。当layoutDirection是Row/RowReverse时，表示一行的高度。当layoutDirection是Column/ColumnReverse时，表示一列的宽度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## columnsGap

```TypeScript
default columnsGap(value: Length | undefined): this
```

设置列与列的间距。设置为小于0的值时，按默认值显示。

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

设置当前网格组件布局列的数量，不设置时默认1列。当value设置为string类型时，使用方法参考[columnsTemplate(value: string)](#columnstemplate)。当value设置为ItemFillPolicy类型时，将根据Grid组件宽度对应[断点类型](../../../ui/arkts-layout-development-grid-layout.md#栅格容器断点)确定列数。例如，ItemFillPolicy.BREAKPOINT_DEFAULT在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列，且每列均为1fr。

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

## edgeEffect

```TypeScript
default edgeEffect(value: EdgeEffect | undefined, options?: EdgeEffectOptions): this
```

设置边缘滑动效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | 是 |
| options | [EdgeEffectOptions](../arkts-components/arkts-arkui-edgeeffectoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## editMode

```TypeScript
default editMode(value: boolean | undefined): this
```

设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## editModeOptions

```TypeScript
default editModeOptions(options?: EditModeOptions): this
```

配置编辑模式选项参数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [EditModeOptions](../arkts-components/arkts-arkui-editmodeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## enableEditMode

```TypeScript
default enableEditMode(enabled: boolean | Bindable<boolean> | undefined): this
```

设置Grid是否启用编辑模式，启用编辑模式后可以在Grid组件内滑动多选GridItem。未通过该接口设置时，不启用编辑模式。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## enableScrollInteraction

```TypeScript
default enableScrollInteraction(value: boolean | undefined): this
```

设置是否支持滚动手势。

> **说明：**&gt;
> 组件无法通过鼠标按下拖动操作进行滚动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## focusWrapMode

```TypeScript
default focusWrapMode(mode: FocusWrapMode | undefined): this
```

设置交叉轴方向键走焦模式。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [FocusWrapMode](arkts-arkui-focuswrapmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## friction

```TypeScript
default friction(value: double | Resource | undefined): this
```

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## layoutDirection

```TypeScript
default layoutDirection(value: GridDirection | undefined): this
```

设置布局的主轴方向。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [GridDirection](arkts-arkui-grid-griddirection-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## maxCount

```TypeScript
default maxCount(value: int | undefined): this
```

设置可显示的最大行数或列数。设置为小于1的值时，按默认值显示。当layoutDirection是Row/RowReverse时，表示可显示的最大列数。当layoutDirection是Column/ColumnReverse时，表示可显示的最大行数。当maxCount小于minCount时，maxCount和minCount都按默认值处理。

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

## minCount

```TypeScript
default minCount(value: int | undefined): this
```

设置可显示的最小行数或列数。设置为小于1的值时，按默认值显示。当layoutDirection是Row/RowReverse时，表示可显示的最小列数。当layoutDirection是Column/ColumnReverse时，表示可显示的最小行数。当minCount大于maxCount时，minCount和maxCount都按默认值处理。

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

## multiSelectable

```TypeScript
default multiSelectable(value: boolean | undefined): this
```

设置是否开启鼠标框选。开启框选后，可以配合GridItem的selected属性和 onSelect事件获取GridItem的选中状态，还可以通过 多态样式设置GridItem的选中态样式（GridItem默认无选中态样式）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## nestedScroll

```TypeScript
default nestedScroll(value: NestedScrollOptions | undefined): this
```

设置嵌套滚动选项。设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。当组件内容大小小于组件自身，且[edgeEffect](#edgeeffect)的options为{ alwaysEnabled: false}时，组件自身滑动手势不会触发，嵌套滚动属性不会生效，如果其父滚动组件有滑动手势，则会触发父组件的滑动手势。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NestedScrollOptions](../arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDidScroll

```TypeScript
default onDidScroll(handler: OnScrollCallback | undefined): this
```

Grid滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。

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

## onEditModeChange

```TypeScript
default onEditModeChange(callback: Callback<boolean> | undefined): this
```

[enableEditMode](#enableeditmode)编辑模式状态变化时触发。使用callback异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onItemDragEnter

```TypeScript
default onItemDragEnter(event: ((event: ItemDragInfo) => void) | undefined): this
```

拖拽进入网格元素范围内时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: ItemDragInfo) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onItemDragLeave

```TypeScript
default onItemDragLeave(event: ((event: ItemDragInfo, itemIndex: int) => void) | undefined): this
```

拖拽离开网格元素时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: ItemDragInfo, itemIndex: int) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onItemDragMove

```TypeScript
default onItemDragMove(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int) => void) | undefined): this
```

拖拽在网格元素范围内移动时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: ItemDragInfo, itemIndex: int, insertIndex: int) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onItemDragStart

```TypeScript
default onItemDragStart(event: OnItemDragStartCallback | undefined): this
```

开始拖拽网格元素时触发。手指长按GridItem时触发该事件。由于拖拽检测也需要长按，且事件处理机制优先触发子组件事件，GridItem上绑定[LongPressGesture](arkts-arkui-longpressgestureinterface-i.md)时无法触发拖拽。如有长按和拖拽同时使用的需求 可以使用通用拖拽事件。拖拽浮起的网格元素可在应用窗口内移动，若需限制移动范围，可通过自定义手势实现，具体参考 [示例16（实现GridItem自定义拖拽）](../../../reference/apis-arkui/arkui-ts/ts-container-grid.md#示例16实现griditem自定义拖拽)。不支持拖动到Grid边缘时自动滚动，可使用通用拖拽实现，具体参考 [示例17（通过拖拽事件实现griditem拖拽）](../../../reference/apis-arkui/arkui-ts/ts-container-grid.md#示例17通过拖拽事件实现griditem拖拽)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnItemDragStartCallback](../arkts-components/arkts-arkui-onitemdragstartcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onItemDrop

```TypeScript
default onItemDrop(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int, isSuccess: boolean) => void) | undefined): this
```

绑定该事件的网格元素可作为拖拽释放目标，当GridItem停止拖拽时触发。当拖拽释放位置在网格元素之内时，isSuccess会返回true；在网格元素之外时，isSuccess会返回false。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: ItemDragInfo, itemIndex: int, insertIndex: int, isSuccess: boolean) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollBarUpdate

```TypeScript
default onScrollBarUpdate(event: ((index: int, offset: double) => ComputedBarAttribute) | undefined): this
```

在Grid每帧布局结束时触发，可通过该回调设置滚动条的位置及长度。该接口只用作设置Grid的滚动条位置，不建议开发者在此接口中做业务逻辑处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((index: int, offset: double) = & gt; ComputedBarAttribute) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollFrameBegin

```TypeScript
default onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this
```

该接口回调时，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，网格将按照返回值的实际滑动量进行滑动。满足以下任一条件时触发该事件：
1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
2. Grid惯性滚动。
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

当前网格显示的起始位置/终止位置的item发生变化时触发。网格初始化时会触发一次。Grid显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。

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

滚动事件回调，Grid滚动前触发。回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定滚动组件将要滚动的偏移。

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

设置行与行的间距。设置为小于0的值时，按默认值显示。

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

设置当前网格布局行的数量、固定行高或最小行高值，不设置时默认1行。例如，&nbsp;'1fr&nbsp;1fr&nbsp;2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。rowsTemplate('repeat(auto-fit, track-size)')是设置最小行高值为track-size，自动计算行数和实际行高。rowsTemplate('repeat(auto-fill, track-size)')是设置固定行高值为track-size，自动计算行数。rowsTemplate('repeat(auto-stretch, track-size)')是设置固定行高值为track-size，使用rowsGap为最小行间距，自动计算行数和实际行间距。其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为行高，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包括一个有效行高。auto-fit模式和auto-stretch模式只支持track-size为一个有效行高值，并且auto-stretch模式中的track-size只支持px、vp和有效数字，不支持%。auto-fill模式支持一个或多个有 效行高，如rowsTemplate('repeat(auto-fill, 20)')、rowsTemplate('repeat(auto-fill, 20 80px)')。设置为'0fr'，则这一行的行高为0，这一行GridItem不显示。设置为其他非法值，按固定1行处理。

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

## scrollBar

```TypeScript
default scrollBar(value: BarState | undefined): this
```

设置滚动条状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BarState](arkts-arkui-barstate-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarColor

```TypeScript
default scrollBarColor(color: Color | int | string | Resource | undefined): this
```

设置滚动条的颜色。与[scrollBarColor](#scrollbarcolor)相比， 参数名改为color，并开始支持Resource类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [Color](arkts-arkui-color-e.md) \| int \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarWidth

```TypeScript
default scrollBarWidth(value: double | string | undefined): this
```

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Grid组件主轴方向的高度，则滚动条的宽度会变为默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarWidth

```TypeScript
default scrollBarWidth(value: Resource | undefined): this
```

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Grid组件主轴方向的高度，则滚动条的宽度会变为4vp。支持Resource资源类型。未通过该接口设置时，设置滚动条的宽度为4vp。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setGridOptions

```TypeScript
default setGridOptions(scroller?: Scroller, layoutOptions?: GridLayoutOptions): this
```

设置网格选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 否 |
| layoutOptions | [GridLayoutOptions](arkts-arkui-grid-gridlayoutoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [GridAttribute](arkts-arkui-grid-gridattribute-i.md) |

## supportAnimation

```TypeScript
default supportAnimation(value: boolean | undefined): this
```

设置是否支持动画。当前支持GridItem拖拽动画。仅在滚动模式下（只设置rowsTemplate、columnsTemplate其中一个）支持动画。仅在大小规则的Grid中支持拖拽动画，跨行或跨列场景不支持。supportAnimation动画效果参考[示例5（Grid拖拽场景）](../../../reference/apis-arkui/arkui-ts/ts-container-grid.md#示例5grid拖拽场景)，其 他动画效果需要应用自定义拖拽实现。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## supportEmptyBranchInLazyLoading

```TypeScript
default supportEmptyBranchInLazyLoading(supported: boolean | undefined): this
```

设置当前Grid组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。未设置时不支持空分支节点。此属性初次赋值后不支持更新，所以赋值后无法在支持空分支、不支持空分支 行为之间切换。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

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

设置是否同步加载Grid区域内所有子组件。

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
