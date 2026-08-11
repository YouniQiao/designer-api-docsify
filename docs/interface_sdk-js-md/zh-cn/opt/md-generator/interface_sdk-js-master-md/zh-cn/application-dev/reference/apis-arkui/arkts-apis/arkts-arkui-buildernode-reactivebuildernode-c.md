# ReactiveBuilderNode

ReactiveBuilderNode支持通过无状态的UI方法[@Builder](../../../ui/state-management/arkts-builder.md)生成组件树，并持有该组件树的根节点，不支持定义为状态变量。ReactiveBuilderNode中持有的[FrameNode](arkts-arkui-framenode-c.md)仅用于将此ReactiveBuilderNode作为子节点挂载到其他FrameNode上。对ReactiveBuilderNode持有的FrameNode进行属性设置与子节点操作可能会导致未定义行为，因此不建议通过ReactiveBuilderNode的  
[getFrameNode](arkts-arkui-buildernode-c.md#getframenode)方法和[FrameNode](arkts-arkui-framenode-c.md)节点的  
[getRenderNode](arkts-arkui-framenode-c.md#getrendernode)方法获取RenderNode，并通过  
[RenderNode](arkts-arkui-rendernode-c.md)的接口对其进行属性设置与子节点操作。

**起始版本：** 22

<!--Device-unnamed-export class ReactiveBuilderNode<Args extends Object[]>--><!--Device-unnamed-export class ReactiveBuilderNode<Args extends Object[]>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
build(builder: WrappedBuilder<Args>, config: BuildOptions, ...args: Args): void
```

依照传入的对象创建组件树，并持有组件树的根节点。无状态的UI方法[@Builder](../../../ui/state-management/arkts-builder.md)最多拥有一个根节点。

支持自定义组件。

> **说明：**
> 
> - @Builder进行创建和更新的规格参考[@Builder](../../../ui/state-management/arkts-builder.md)。
> 
> - @Builder嵌套使用的时候需要保证内外的@Builder方法的入参对象一致。
> 
> - 需要操作ReactiveBuilderNode中的对象时，需要保证其引用不被回收。当ReactiveBuilderNode对象被虚拟机回收之后，它的[FrameNode](arkts-arkui-framenode-c.md)、
> [RenderNode](arkts-arkui-rendernode-c.md)对象也会与后端节点解引用。即从ReactiveBuilderNode中获取的FrameNode对象不对应任何一个节点。
> 
> - ReactiveBuilderNode对象会持有实体节点的引用。如果不需要使用ReactiveBuilderNode前端对象管理后端节点，可以调用
> [dispose](arkts-arkui-buildernode-reactivebuildernode-c.md#dispose)接口，实现前后端对象的解绑。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-build(builder: WrappedBuilder<Args>, config: BuildOptions, ...args: Args): void--><!--Device-ReactiveBuilderNode-build(builder: WrappedBuilder<Args>, config: BuildOptions, ...args: Args): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [WrappedBuilder](../arkts-components/arkts-arkui-wrappedbuilder-c.md)&lt;Args&gt; | 是 |
| config | [BuildOptions](arkts-arkui-buildernode-buildoptions-i.md) | 是 |
| args | Args | 是 |

## constructor

```TypeScript
constructor(uiContext: UIContext, options?: RenderOptions)
```

用于构造ReactiveBuilderNode类。当将ReactiveBuilderNode生成的内容嵌入到其它[RenderNode](arkts-arkui-rendernode-c.md)中显示时，需要显式指定  
[RenderOptions](arkts-arkui-buildernode-renderoptions-i.md)中的[selfIdealSize](arkts-arkui-buildernode-renderoptions-i.md)，否则ReactiveBuilderNode内的节点默认父组件布局约束为  
[0, 0]。调用此接口，若不设置selfIdealSize则认为ReactiveBuilderNode中子树的根节点大小为[0, 0]。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-constructor(uiContext: UIContext, options?: RenderOptions)--><!--Device-ReactiveBuilderNode-constructor(uiContext: UIContext, options?: RenderOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| options | [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | 否 |

## dispose

```TypeScript
dispose(): void
```

立即释放当前ReactiveBuilderNode对象对[实体节点](../../../ui/arkts-user-defined-node.md#基本概念)的引用关系。关于ReactiveBuilderNode的解绑场景请参见  
[节点解绑](../../../ui/arkts-user-defined-arktsNode-builderNode.md#解除实体节点引用关系)。

> **说明：**
> 
> 当ReactiveBuilderNode对象调用dispose之后，会与后端实体节点解除引用关系。若前端对象ReactiveBuilderNode无法释放，容易导致内存泄漏。建议在不再需要对该
> ReactiveBuilderNode对象进行操作时，开发者主动调用dispose释放后端节点，以减少引用关系的复杂性，降低内存泄漏的风险。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-dispose(): void--><!--Device-ReactiveBuilderNode-dispose(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## flushState

```TypeScript
flushState(): void
```

根据绑定数据的变化刷新ReactiveBuilderNode的数据状态。当ReactiveBuilderNode中  
[WrappedBuilder](../../../ui/state-management/arkts-wrapBuilder.md)对象封装的builder函数中使用的绑定参数是由V1装饰器（如@Observed）装饰的类实例时，需要在此类数据变更后手动调用此方法以更新数据，当使用V2装饰器（如@ObservedV2）装饰的类实例时，支持自动更新，无需手动调用。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-flushState(): void--><!--Device-ReactiveBuilderNode-flushState(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getFrameNode

```TypeScript
getFrameNode(): FrameNode | null
```

获取ReactiveBuilderNode中的[FrameNode](arkts-arkui-framenode-c.md)。在ReactiveBuilderNode执行build操作之后，才会生成FrameNode。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-getFrameNode(): FrameNode | null--><!--Device-ReactiveBuilderNode-getFrameNode(): FrameNode | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |

## inheritFreezeOptions

```TypeScript
inheritFreezeOptions(enabled: boolean): void
```

设置当前ReactiveBuilderNode对象是否继承父组件中自定义组件的冻结策略。如果设置继承状态为false，则ReactiveBuilderNode对象的冻结策略为false。在这种情况下，节点在不活跃状态下不会被冻结。

> **说明：**
> 
> ReactiveBuilderNode设置inheritFreezeOptions为true，且父组件为自定义组件、BuilderNode、ComponentContent、ReactiveBuilderNode或
> ReactiveComponentContent时，会继承父组件的冻结策略。当子组件为自定义组件时，ReactiveBuilderNode的冻结策略不会传递给子组件。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-inheritFreezeOptions(enabled: boolean): void--><!--Device-ReactiveBuilderNode-inheritFreezeOptions(enabled: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

## isDisposed

```TypeScript
isDisposed(): boolean
```

查询当前ReactiveBuilderNode对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。由于业务需求，可能存在节点在dispose后仍被调用接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-isDisposed(): boolean--><!--Device-ReactiveBuilderNode-isDisposed(): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## postInputEvent

```TypeScript
postInputEvent(event: InputEventType): boolean
```

将输入事件分发到ReactiveBuilderNode管理的目标节点。适用于在自定义NodeContainer中将父组件接收的触摸、鼠标或轴事件转发给ReactiveBuilderNode内部组件，使内部组件能够响应相应交互的场景。

offsetA为builderNode相对于父组件的偏移，offsetB为命中位置相对于builderNode的偏移，offsetC为offsetA+offsetB，最终输入给postInputEvent当中。

![接口坐标换算示例图](../../../reference/apis-arkui/figures/postInputEvent-point.png)

> **说明：**
> 
> 传入的坐标值需要转换为px，坐标转换示例可以参考下面示例代码。
> 
> 鼠标左键点击事件将转换为触摸事件，转发时应注意不在外层同时绑定触摸事件与鼠标事件，否则可能导致坐标偏移。这是由于在事件转换过程中，事件的
> [SourceType](../../../reference/apis-arkui/arkui-ts/ts-gesture-settings.md#sourcetype枚举说明8)不会发生变化，规格可查看
> [onTouch](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#ontouch)。
> 
> 注入事件为轴事件[（AxisEvent）](../arkts-components/arkts-arkui-axisevent-i.md/arkts-arkui-axisevent-i.md)时，由于轴事件中缺少旋转轴信息，因此注入的事件无法触发
> [RotationGesture](../../apis-arkui/arkts-apis/arkts-arkui-gesture-i)。
> 
> 转发的事件会在被分发到的目标组件所在的子树里做触摸测试（TouchTest），并触发对应手势，原始事件也会触发当前组件所在组件树中的手势。不保证两类手势的竞争结果。
> 
> 如果是开发者构造的事件，必填字段必须赋值，比如触摸事件的touches字段、轴事件的scrollStep字段，同时要保证事件的完整，比如触摸事件的[TouchType](arkts-arkui-touchtype-e.md)中DOWN和UP字段都要
> 有，防止出现未定义行为。
> 
> [webview](../../apis-arkweb/arkts-apis/arkts-web-webview.md/arkts-web-webview.md)已经处理过坐标系变换，可以将事件直接下发。
> 
> postTouchEvent接口需要提供手势坐标相对于接收事件的目标节点内的局部坐标，postInputEvent接口需要提供手势坐标相对于接收事件的目标节点内的窗口坐标。
> 
> 不建议同一个事件转发多次。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-postInputEvent(event: InputEventType): boolean--><!--Device-ReactiveBuilderNode-postInputEvent(event: InputEventType): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [InputEventType](arkts-arkui-inputeventtype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## postInputEventWithStrategy

```TypeScript
postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean
```

将含有竞争策略的事件分发到目标UI组件节点。

接口调用前需要将event转化为对应的事件，并对event中的window参数的坐标进行转化：offsetA表示ReactiveBuilderNode相对于父组件的偏移量，offsetB为命中位置相对于ReactiveBuilderNode的偏移量，offsetC是offsetA与offsetB之和，最终作为event中的window参数，传递给postInputEventWithStrategy方法，具体请参考示例。

![接口坐标换算示例图](../../../reference/apis-arkui/figures/postInputEvent-point.png)

> **说明：**
> 
> - 传入的坐标值单位需要转换为px，坐标转换示例可以参考下面示例代码。
> 
> - 系统在处理鼠标左键点击事件时将转换为触摸事件，转发时应注意不在外层同时绑定触摸事件与鼠标事件，否则可能导致坐标偏移。这是由于在事件转换过程中，
> [SourceType](../../../reference/apis-arkui/arkui-ts/ts-gesture-settings.md#sourcetype枚举说明8)不会发生变化，规格可查看
> [onTouch](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#ontouch)。
> 
> - 注入事件为轴事件[AxisEvent](../arkts-components/arkts-arkui-axisevent-i.md/arkts-arkui-axisevent-i.md)时，由于轴事件中缺少旋转轴信息，因此注入的事件无法触发旋转手势
> [RotationGesture](../../apis-arkui/arkts-apis/arkts-arkui-gesture-i)。
> 
> - 转发的事件会在被分发到的目标组件及其子组件里做事件处理，并触发对应手势。可以通过入参控制当前组件和目标组件手势是否为竞争关系。
> 
> - 如果event转化为对应的事件后，该事件为开发者构造的事件，必填字段必须赋值，比如触摸事件的touches字段，轴事件的scrollStep字段。要保证事件的完整，比如触摸事件的
> [TouchType](arkts-arkui-touchtype-e.md)中必须同时包含DOWN和UP两个字段，防止出现程序异常或意外崩溃。
> 
> - [webview](../../apis-arkweb/arkts-apis/arkts-web-webview.md/arkts-web-webview.md)已经处理过坐标系变换，可以将事件直接下发。
> 
> - postTouchEvent接口需要提供手势坐标相对于接收事件的目标节点内的局部坐标，postInputEventWithStrategy接口需要提供手势坐标相对于接收事件的目标节点内的窗口坐标。
> 
> - 支持同一个事件转发多次。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean--><!--Device-ReactiveBuilderNode-postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [InputEventType](arkts-arkui-inputeventtype-t.md) | 是 |
| competitionStrategy | [CompetitionStrategy](arkts-arkui-competitionstrategy-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## postTouchEvent

```TypeScript
postTouchEvent(event: TouchEvent): boolean
```

将原始事件派发到某个ReactiveBuilderNode创建的FrameNode上。适用于在自定义NodeContainer中将父组件接收的触摸事件转发给ReactiveBuilderNode内部组件，使内部组件能够响应触摸交互的场景。

postTouchEvent是从组件树的中间节点往下分发，需要变换到父组件坐标系才能分发成功，参考下图。

offsetA为builderNode相对于父组件的偏移量，可以通过FrameNode中的[getPositionToParent](arkts-arkui-framenode-c.md#getpositiontoparent)获取。offsetB为触点相对于builderNode的偏移量，可以通过  
[TouchEvent](../../../reference/apis-arkui/arkui-ts/ts-universal-events-touch.md#touchevent对象说明)获取。offsetC为offsetA与offsetB的和，是传给postTouchEvent的最终结果。

![postTouchEvent](../../../reference/apis-arkui/figures/postTouchEvent.PNG)

> **说明：**
> 
> 传入的坐标值需要转换为px，如果builderNode有仿射变换，则需要再叠加仿射变换。
> 
> 在[webview](../../apis-arkweb/arkts-apis/arkts-web-webview.md/arkts-web-webview.md)中，内部已经处理过坐标系变换，可以将TouchEvent事件直接下发。
> 
> 同一时间戳，postTouchEvent只能调用一次。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-postTouchEvent(event: TouchEvent): boolean--><!--Device-ReactiveBuilderNode-postTouchEvent(event: TouchEvent): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [TouchEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-touchevent-touchevent-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## recycle

```TypeScript
recycle(): void
```

触发ReactiveBuilderNode中自定义组件的回收。自定义组件的回收是组件复用机制中的环节，具体信息请参见  
[@Reusable装饰器：V1组件复用](../../../ui/state-management/arkts-reusable.md)。从API版本26.0.0开始，ReactiveBuilderNode中的自定义组件支持V2组件复用，请参见[@ReusableV2装饰器：V2组件复用](../../../ui/state-management/arkts-new-reusableV2.md)。

ReactiveBuilderNode通过[reuse](arkts-arkui-buildernode-reactivebuildernode-c.md#reuse)和recycle完成其内外自定义组件之间的复用事件传递，具体使用场景请参见  
[BuilderNode调用reuse和recycle接口实现节点复用能力](../../../ui/arkts-user-defined-arktsNode-builderNode.md#buildernode调用reuse和recycle接口实现节点复用能力)。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-recycle(): void--><!--Device-ReactiveBuilderNode-recycle(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## reuse

```TypeScript
reuse(param?: Object): void
```

触发ReactiveBuilderNode中的自定义组件的复用。组件复用请参见[@Reusable装饰器：V1组件复用](../../../ui/state-management/arkts-reusable.md)。关于ReactiveBuilderNode的解绑场景请参见[节点解绑](../../../ui/arkts-user-defined-arktsNode-builderNode.md#解除实体节点引用关系)。从API版本26.0.0开始，ReactiveBuilderNode中的自定义组件支持V2组件复用，请参见  
[@ReusableV2装饰器：V2组件复用](../../../ui/state-management/arkts-new-reusableV2.md)。

ReactiveBuilderNode通过reuse和[recycle](arkts-arkui-buildernode-reactivebuildernode-c.md#recycle)完成其内外自定义组件之间的复用事件传递，具体使用场景请参见  
[BuilderNode调用reuse和recycle接口实现节点复用能力](../../../ui/arkts-user-defined-arktsNode-builderNode.md#buildernode调用reuse和recycle接口实现节点复用能力)。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-reuse(param?: Object): void--><!--Device-ReactiveBuilderNode-reuse(param?: Object): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | Object | 否 |

## updateConfiguration

```TypeScript
updateConfiguration(): void
```

传递系统环境变化事件，触发节点的全量更新。可用于通知对象更新，是否触发更新由应用当前的系统环境变化决定。系统环境变化的相关信息请参见  
[@ohos.app.ability.Configuration (环境变量)](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-configuration-configuration-i.md/arkts-ability-app-ability-configuration-configuration-i.md)。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ReactiveBuilderNode-updateConfiguration(): void--><!--Device-ReactiveBuilderNode-updateConfiguration(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
