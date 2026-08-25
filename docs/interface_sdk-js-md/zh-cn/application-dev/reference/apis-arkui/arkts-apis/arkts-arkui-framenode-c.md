# FrameNode

FrameNode表示组件树的实体节点，支持节点树操作、自定义绘制与布局、位置查询、动画等能力。[NodeController](arkts-arkui-nodecontroller-c.md)可通过 BuilderNode持有的FrameNode将其挂载到NodeContainer上， 也可通过FrameNode获取[RenderNode](arkts-arkui-rendernode-c.md)，挂载到其他FrameNode上。适用于需要通过代码动态创建和管理组件节点树的场景，可实现声明式组件无法直接满足的灵活 UI组合与自定义渲染需求。<!--RP2--><!--RP2End-->

> **说明：**&gt;
> - 当前不支持在预览器中使用FrameNode节点。&gt;
> - FrameNode节点暂不支持拖拽。&gt;
> - FrameNode对象不支持使用JSON序列化。&gt;
> - 在[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的场景中调用[FrameNode](#framenode)对象的接口时，建议使用
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)的[runScopedTask](arkts-arkui-arkui-uicontext-uicontext-c.md#runscopedtask)接口明确UI
> 上下文，参考[执行绑定UI实例的闭包](../../../ui/arkts-global-interface.md#执行绑定ui实例的闭包)示例。&gt;
> - FrameNode的接口中，仅[Optional](../arkts-components/arkts-arkui-optional-t.md)类型的必选参数支持传入null或undefined。

**起始版本：** 11

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addComponentContent

```TypeScript
addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent<T>): void
```

支持添加ComponentContent类型的组件内容。要求当前节点是一个可修改的节点，即[isModifiable](#ismodifiable)的返回值为true，否则抛出异常信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md)&lt;T&gt; \| [ReactiveComponentContent](arkts-arkui-componentcontent-reactivecomponentcontent-c.md)&lt;T&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |

## addSupportedUIStates

```TypeScript
addSupportedUIStates(uiStates: number, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void
```

设置组件支持的多态样式状态。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uiStates | number | 是 | 需要处理目标节点的UI状态。 可以通过位或计算同时指定多个状态，如：targetUIStates = UIState.PRESSED  \|
| statesChangeHandler | [UIStatesChangeHandler](arkts-arkui-uistateschangehandler-t.md) | 是 |
| excludeInner | boolean | 否 |

## adoptChild

```TypeScript
adoptChild(child: FrameNode): void
```

当前节点接纳目标节点为附属节点。当前FrameNode如果不可修改，抛出异常信息。被接纳的附属节点不能已有父节点。调用该接口实际上不会将目标节点添加为子节点，而是仅允许当前节点接收该附属节点的生命周期回调。使用场景：当需要监听某个 节点的生命周期回调但不希望改变其父子关系或组件树结构时，可通过该接口接纳其为附属节点。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [child](../arkts-components/arkts-arkui-nestedscrollinfo-i.md) | [FrameNode](arkts-arkui-framenode-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100025](../errorcode-node.md#100025-传入参数不符合要求) |
| [100026](../errorcode-node.md#100026-调用接口的实例对象已与后端实体节点解绑) |

## appendChild

```TypeScript
appendChild(node: FrameNode): void
```

在FrameNode最后一个子节点后添加新的子节点。当前FrameNode如果不可修改，抛出异常信息。[typeNode](arkts-arkui-typenode-n.md)在appendChild时会校验子组件类型或个数，不满足时抛出异常信息，限制 情况请查看[typeNode](arkts-arkui-typenode-n.md)描述。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100025](../errorcode-node.md#100025-传入参数不符合要求) |

## cancelAnimations

```TypeScript
cancelAnimations(properties: AnimationPropertyType[]): boolean
```

请求取消FrameNode上指定属性上的所有动画，该方法需在节点所处线程中调用，会阻塞当前线程以等待取消结果。如果动画成功取消，节点上的属性值会被恢复为取消时的显示值（即当前状态）。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| properties | [AnimationPropertyType](arkts-arkui-animationpropertytype-e.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## clearChildren

```TypeScript
clearChildren(): void
```

清除当前FrameNode的所有子节点。当前FrameNode如果不可修改，抛出异常信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |

## constructor

```TypeScript
constructor(uiContext: UIContext)
```

FrameNode的构造函数。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |

## convertPosition

```TypeScript
convertPosition(position: Position, targetNode: FrameNode): Position
```

将点的坐标从当前节点的坐标系转换为目标节点的坐标系。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | [Position](arkts-arkui-position-t.md) | 是 |
| targetNode | [FrameNode](arkts-arkui-framenode-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [100024](../errorcode-node.md#100024-节点没有公共祖先节点) |
| [100025](../errorcode-node.md#100025-传入参数不符合要求) |

## convertPositionFromWindow

```TypeScript
convertPositionFromWindow(positionByWindow: Position): Position
```

将点的坐标从当前节点所在窗口的坐标系转换为当前节点的坐标系。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| positionByWindow | [Position](arkts-arkui-position-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [100026](../errorcode-node.md#100026-调用接口的实例对象已与后端实体节点解绑) |
| [100028](../errorcode-node.md#100028-当前节点不在主节点树上) |

## convertPositionToWindow

```TypeScript
convertPositionToWindow(positionByLocal: Position): Position
```

将点的坐标从当前节点的坐标系转换为当前节点所在窗口的坐标系。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| positionByLocal | [Position](arkts-arkui-position-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [100026](../errorcode-node.md#100026-调用接口的实例对象已与后端实体节点解绑) |
| [100028](../errorcode-node.md#100028-当前节点不在主节点树上) |

## createAnimation

```TypeScript
createAnimation(property: AnimationPropertyType, startValue: Optional<number[]>, endValue: number[], param: AnimateParam): boolean
```

创建FrameNode上属性的动画。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| property | [AnimationPropertyType](arkts-arkui-animationpropertytype-e.md) | 是 |
| startValue | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number[]&gt; | 是 |
| endValue | number[] | 是 |
| param | [AnimateParam](../arkts-components/arkts-arkui-animateparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## createFrameNodes

```TypeScript
static createFrameNodes(uiContext: UIContext, count: number): FrameNode[]
```

批量创建指定数量的FrameNode，返回FrameNode数组。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| count | number | 是 |

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md)[] |

## dispose

```TypeScript
dispose(): void
```

立即解除当前FrameNode对象对实体FrameNode节点的引用关系。

> **说明：**&gt;
> - FrameNode对象调用dispose后，由于不对应任何实体FrameNode节点，在调用部分查询接口([getMeasuredSize](#getmeasuredsize)、
> [getLayoutPosition](#getlayoutposition))的时候会导致应用出现jscrash。&gt;
> - 通过[getUniqueId](#getuniqueid)可以判断当前FrameNode是否对应一个实体FrameNode节点。当UniqueID大于0时表示该对象对应一个实体
> FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## disposeTree

```TypeScript
disposeTree(): void
```

下树并递归释放当前节点为根的子树。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getChild

```TypeScript
getChild(index: number): FrameNode | null
```

获取当前节点指定位置的子节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) \| null |

## getChild

```TypeScript
getChild(index: number, expandMode?: ExpandMode): FrameNode | null
```

获取当前节点指定位置的子节点，支持指定子节点展开模式。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| expandMode | [ExpandMode](arkts-arkui-framenode-expandmode-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) \| null |

## getChildrenCount

```TypeScript
getChildrenCount(): number
```

获取当前FrameNode的子节点数量。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getChildrenCount

```TypeScript
getChildrenCount(countMode?: ChildrenCountMode): number
```

根据指定的计数模式获取当前FrameNode的子节点数量。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| countMode | [ChildrenCountMode](arkts-arkui-framenode-childrencountmode-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## getCrossLanguageOptions

```TypeScript
getCrossLanguageOptions(): CrossLanguageOptions
```

获取当前FrameNode的跨ArkTS语言访问选项。例如ArkTS语言创建的节点，返回该节点是否可通过非ArkTS语言进行属性设置和跨语言组件树操作，从API版本26.0.0开始支持获取是否可通过非ArkTS语言进行组件树操作。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [CrossLanguageOptions](arkts-arkui-framenode-crosslanguageoptions-i.md) |

## getCustomProperty

```TypeScript
getCustomProperty(name: string): Object | undefined
```

通过名称获取组件的自定义属性。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Object \| undefined |

## getFirstChild

```TypeScript
getFirstChild(): FrameNode | null
```

获取当前FrameNode的第一个子节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) \| null |

## getFirstChildIndexWithoutExpand

```TypeScript
getFirstChildIndexWithoutExpand(): number
```

获取当前节点第一个在主节点树上的子节点的序列号。子节点序列号按所有子节点计算。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getFrameNodeById

```TypeScript
getFrameNodeById(id: string): FrameNode | null
```

以当前节点为根节点，逐层查找所有子节点，返回第一个匹配指定id的节点。查找顺序为：先查找直接子节点，再查找二级子节点，依此类推，找到后立即返回。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) \| null |

## getFrameNodeByUniqueId

```TypeScript
getFrameNodeByUniqueId(id: number): FrameNode | null
```

以当前节点为根节点，查找并返回指定UniqueID（系统分配的节点唯一标识，该标识可通过[getUniqueId](#getuniqueid)接口获取）的子节点。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) \| null |

## getGlobalPositionOnDisplay

```TypeScript
getGlobalPositionOnDisplay(): Position
```

获取FrameNode相对于全局屏幕的位置偏移，单位为VP。与[getPositionToScreen](#getpositiontoscreen)的坐标系参考不同，请根据实际场景选择使用。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getId

```TypeScript
getId(): string
```

获取用户设置的节点ID（通用属性设置的组件标识）。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

## getInspectorInfo

```TypeScript
getInspectorInfo(): Object
```

获取节点的结构信息，该信息和DevEco Studio内置<!--RP1-->ArkUI Inspector<!--RP1End-->工具里面的一致。

> **说明：**&gt;
> getInspectorInfo接口用于获取所有节点的信息，作为调试接口使用，频繁调用会导致性能下降。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| Object |

## getInteractionEventBindingInfo

```TypeScript
getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined
```

获取目标节点的事件绑定信息，如果该组件节点上没有绑定要查询的交互事件类型时，返回 undefined。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventType | [EventQueryType](arkts-arkui-eventquerytype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [InteractionEventBindingInfo](arkts-arkui-framenode-interactioneventbindinginfo-i.md) \| undefined |

## getLastChildIndexWithoutExpand

```TypeScript
getLastChildIndexWithoutExpand(): number
```

获取当前节点最后一个在主节点树上的子节点的序列号。子节点序列号按所有子节点计算。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getLayoutPosition

```TypeScript
getLayoutPosition(): Position
```

获取FrameNode布局后相对于父组件的位置偏移，单位为PX。该偏移是父容器对该节点进行布局之后的结果，因此布局之后生效的offset属性和不参与布局的position属性不影响该偏移值。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getMeasuredSize

```TypeScript
getMeasuredSize(): Size
```

获取FrameNode测量后的大小，单位为PX。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| Size |

## getNextSibling

```TypeScript
getNextSibling(): FrameNode | null
```

获取当前FrameNode的下一个同级节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) \| null |

## getNodePropertyValue

```TypeScript
getNodePropertyValue(property: AnimationPropertyType): number[]
```

获取FrameNode上的属性值。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| property | [AnimationPropertyType](arkts-arkui-animationpropertytype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number[] |

## getNodeType

```TypeScript
getNodeType(): string
```

获取节点的类型。系统组件类型为组件名称，例如，按钮组件Button的类型为Button。而对于自定义组件，若其有渲染内容，则其类型为 __Common__。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

## getOpacity

```TypeScript
getOpacity(): number
```

获取节点的不透明度，最小值为0，最大值为1。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getParent

```TypeScript
getParent(): FrameNode | null
```

获取当前FrameNode的父节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) \| null |

## getPositionToParent

```TypeScript
getPositionToParent(): Position
```

获取FrameNode相对于父组件的位置偏移，单位为VP。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToParentWithTransform

```TypeScript
getPositionToParentWithTransform(): Position
```

获取FrameNode相对于父组件带有绘制属性的位置偏移，单位为VP，绘制属性比如transform、 translate等，返回的坐标是组件布局时左上角变换后的坐标。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToScreen

```TypeScript
getPositionToScreen(): Position
```

获取FrameNode相对于屏幕的位置偏移，单位为VP。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToScreenWithTransform

```TypeScript
getPositionToScreenWithTransform(): Position
```

获取FrameNode相对于屏幕带有绘制属性的位置偏移，单位为VP，绘制属性比如transform、 translate等，返回的坐标是组件布局时左上角变换后的坐标。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToWindow

```TypeScript
getPositionToWindow(): Position
```

获取FrameNode相对于窗口的位置偏移，单位为VP。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToWindowWithTransform

```TypeScript
getPositionToWindowWithTransform(): Position
```

获取FrameNode相对于窗口带有绘制属性的位置偏移，单位为VP，绘制属性比如transform、 translate等，返回的坐标是组件布局时左上角变换后的坐标。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPreviousSibling

```TypeScript
getPreviousSibling(): FrameNode | null
```

获取当前FrameNode的上一个同级节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) \| null |

## getRenderNode

```TypeScript
getRenderNode(): RenderNode | null
```

获取FrameNode中持有的[RenderNode](arkts-arkui-rendernode-c.md)。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) \| null |

## getUniqueId

```TypeScript
getUniqueId(): number
```

获取系统分配的节点唯一标识（UniqueID）。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getUserConfigBorderWidth

```TypeScript
getUserConfigBorderWidth(): Edges<LengthMetrics>
```

获取用户设置的边框宽度。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Edges](arkts-arkui-graphics-edges-i.md)&lt;[LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)&gt; |

## getUserConfigMargin

```TypeScript
getUserConfigMargin(): Edges<LengthMetrics>
```

获取用户设置的外边距。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Edges](arkts-arkui-graphics-edges-i.md)&lt;[LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)&gt; |

## getUserConfigPadding

```TypeScript
getUserConfigPadding(): Edges<LengthMetrics>
```

获取用户设置的内边距。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Edges](arkts-arkui-graphics-edges-i.md)&lt;[LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)&gt; |

## getUserConfigSize

```TypeScript
getUserConfigSize(): SizeT<LengthMetrics>
```

获取用户设置的宽高。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [SizeT](arkts-arkui-graphics-sizet-i.md)&lt;[LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)&gt; |

## insertChildAfter

```TypeScript
insertChildAfter(child: FrameNode, sibling: FrameNode | null): void
```

在FrameNode指定子节点之后添加新的子节点。当前FrameNode如果不可修改，抛出异常信息。[typeNode](arkts-arkui-typenode-n.md)在insertChildAfter时会校验子组件类型或个数，不满足时抛出异常信 息，限制情况请查看[typeNode](arkts-arkui-typenode-n.md)描述。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [child](../arkts-components/arkts-arkui-nestedscrollinfo-i.md) | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| sibling | [FrameNode](arkts-arkui-framenode-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100025](../errorcode-node.md#100025-传入参数不符合要求) |

## invalidate

```TypeScript
invalidate(): void
```

该方法会触发FrameNode自绘制内容的重新渲染，即重新调用[onDraw](#ondraw)方法进行自绘制。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## invalidateAttributes

```TypeScript
invalidateAttributes(): void
```

在当前帧触发节点属性更新。当前节点的属性在构建阶段后被修改，这些改动不会立即生效，而是延迟到下一帧统一处理。此功能强制当前帧内即时节点更新，确保同步应用渲染效果。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## isAttached

```TypeScript
isAttached(): boolean
```

获取节点是否被挂载到主节点树上。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isClipToFrame

```TypeScript
isClipToFrame(): boolean
```

获取节点是否剪裁到组件区域。当调用[dispose](#dispose)解除对实体FrameNode节点的引用关系之后，返回值为true。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isDisposed

```TypeScript
isDisposed(): boolean
```

查询当前FrameNode对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用该节点的其他接口可能会出现crash、返回默认值的情况。由于业务需求，可能存在节 点在dispose后仍被调用接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isInRenderState

```TypeScript
isInRenderState(): boolean
```

获取节点是否处于渲染状态，如果一个节点的对应RenderNode在渲染树上，则处于渲染状态。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isModifiable

```TypeScript
isModifiable(): boolean
```

判断当前节点是否可修改。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isOnMainTree

```TypeScript
isOnMainTree(): boolean
```

查询节点是否被挂载到主节点树上。与[isAttached](#isattached)均用于判断节点是否挂载到主节点树上，区别在于本接口在节点已调用 [dispose](#dispose)解除引用时会抛出错误码100026，开发者可根据是否需要节点dispose时的错误码校验（即抛出错误码100026）来选择使用本接口或 [isAttached](#isattached)接口。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [100026](../errorcode-node.md#100026-调用接口的实例对象已与后端实体节点解绑) |

## isTransferred

```TypeScript
isTransferred(): boolean
```

判断FrameNode是否通过transfer.transferStatic或者transfer.transferDynamic方法创建。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isVisible

```TypeScript
isVisible(): boolean
```

获取节点是否可见。

> **说明：**&gt;
> 根据组件设置的visibility属性值判断该节点是否可见。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## layout

```TypeScript
layout(position: Position): void
```

调用FrameNode的布局方法，为FrameNode及其子节点指定布局位置，如果布局方法被重写，则调用重写的方法。建议在[onLayout](#onlayout)方法中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | [Position](arkts-arkui-position-t.md) | 是 |

## measure

```TypeScript
measure(constraint: LayoutConstraint): void
```

调用FrameNode的测量方法，根据父容器的布局约束，对FrameNode进行测量，计算出尺寸，如果测量方法被重写，则调用重写的方法。建议在[onMeasure](#onmeasure)方法中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| constraint | [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) | 是 |

## moveTo

```TypeScript
moveTo(targetParent: FrameNode, index?: number): void
```

将当前FrameNode移动到目标FrameNode的指定位置。当前FrameNode如果不可修改，抛出异常信息。targetParent为[typeNode](arkts-arkui-typenode-n.md)时会校验子组件类型或个数，不满足时抛出 异常信息，限制情况请查看[typeNode](arkts-arkui-typenode-n.md)描述。

> **说明：**&gt;
> 当前仅支持以下类型的[TypedFrameNode](arkts-arkui-framenode-typedframenode-i.md)进行移动操作：[Stack](arkts-arkui-typenode-stack-t.md)、
> [XComponent](arkts-arkui-typenode-xcomponent-t.md)。对于其他类型的节点，移动操作不会生效。&gt;
> 当前仅支持根节点为以下类型组件的[BuilderNode](arkts-arkui-buildernode-c.md)进行移动操作：
> Stack、XComponent、
> EmbeddedComponent。对于其他类型的组件，移动操作不会生效。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetParent | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| index | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100027](../errorcode-node.md#100027-当前节点已被接纳为附属节点) |

## onDraw

```TypeScript
onDraw?(context: DrawContext): void
```

FrameNode的自绘制方法，该方法会重写默认绘制方法，在FrameNode进行内容绘制时被调用。该接口的[DrawContext](arkts-arkui-graphics-drawcontext-c.md)中的Canvas是用于记录指令的临时Canvas，并非节点的真实Canvas。使用请参见 [调整自定义绘制Canvas的变换矩阵](../../../ui/arkts-user-defined-arktsNode-frameNode.md#调整自定义绘制canvas的变换矩阵)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [DrawContext](arkts-arkui-graphics-drawcontext-c.md) | 是 |

## onLayout

```TypeScript
onLayout(position: Position): void
```

FrameNode的自定义布局方法，该方法会重写默认布局方法，在FrameNode进行布局时被调用，为FrameNode及其子节点指定位置。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | [Position](arkts-arkui-position-t.md) | 是 |

## onMeasure

```TypeScript
onMeasure(constraint: LayoutConstraint): void
```

FrameNode的自定义测量方法，该方法会重写默认测量方法，在FrameNode进行测量时被调用，测量FrameNode及其内容的大小。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| constraint | [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) | 是 |

## recycle

```TypeScript
recycle(): void
```

全局复用场景下，触发子组件回收，彻底释放FrameNode后端资源，以便于通过[reuse](#reuse)方法实现资源的重新复用，确保后端资源能够被有效回收并再次使用。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## removeAdoptedChild

```TypeScript
removeAdoptedChild(child: FrameNode): void
```

移除被接纳的目标附属节点。当前FrameNode如果不可修改，抛出异常信息。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [child](../arkts-components/arkts-arkui-nestedscrollinfo-i.md) | [FrameNode](arkts-arkui-framenode-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100025](../errorcode-node.md#100025-传入参数不符合要求) |
| [100026](../errorcode-node.md#100026-调用接口的实例对象已与后端实体节点解绑) |

## removeChild

```TypeScript
removeChild(node: FrameNode): void
```

从FrameNode中删除指定的子节点。当前FrameNode如果不可修改，抛出异常信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |

## removeSupportedUIStates

```TypeScript
removeSupportedUIStates(uiStates: number): void
```

删除组件当前注册的状态处理。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uiStates | number | 是 | 需要删除的UI状态。 可以通过位或计算同时指定删除多个状态，如：removeUIStates = UIState.PRESSED  \|

## reuse

```TypeScript
reuse(): void
```

全局复用场景下，触发子组件复用，实现FrameNode后端资源的复用，提升资源利用效率。为保证资源充足，可以在recycle之后使用。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## setCrossLanguageOptions

```TypeScript
setCrossLanguageOptions(options: CrossLanguageOptions): void
```

设置当前FrameNode的跨ArkTS语言访问选项。例如ArkTS语言创建的节点，设置该节点是否可通过非ArkTS语言进行属性设置，从API版本26.0.0开始支持设置是否可通过非ArkTS语言进行组件树操作。当前 FrameNode如果不可修改或不可设置跨ArkTS语言访问选项，抛出异常信息。

> **说明：**&gt;
> 当前仅支持[Scroll](arkts-arkui-typenode-scroll-t.md)、[Swiper](arkts-arkui-typenode-swiper-t.md)、[List](arkts-arkui-typenode-list-t.md)、
> [ListItem](arkts-arkui-typenode-listitem-t.md)、[ListItemGroup](arkts-arkui-typenode-listitemgroup-t.md)、
> [WaterFlow](arkts-arkui-typenode-waterflow-t.md)、[FlowItem](arkts-arkui-typenode-flowitem-t.md)、[Grid](arkts-arkui-typenode-grid-t.md)、
> [GridItem](arkts-arkui-typenode-griditem-t.md)、[TextInput](arkts-arkui-typenode-textinput-t.md)、[TextArea](arkts-arkui-typenode-textarea-t.md)、
> [Column](arkts-arkui-typenode-column-t.md)、[Row](arkts-arkui-typenode-row-t.md)、[Stack](arkts-arkui-typenode-stack-t.md)、
> [Flex](arkts-arkui-typenode-flex-t.md)、[RelativeContainer](arkts-arkui-typenode-relativecontainer-t.md)、
> [Progress](arkts-arkui-typenode-progress-t.md)、[LoadingProgress](arkts-arkui-typenode-loadingprogress-t.md)、
> [Image](arkts-arkui-typenode-image-t.md)、[Button](arkts-arkui-typenode-button-t.md)、[Checkbox](arkts-arkui-typenode-checkbox-t.md)、
> [Radio](arkts-arkui-typenode-radio-t.md)、[Slider](arkts-arkui-typenode-slider-t.md)、[Toggle](arkts-arkui-typenode-toggle-t.md)、
> [XComponent](arkts-arkui-typenode-xcomponent-t.md)类型的[TypedFrameNode](arkts-arkui-framenode-typedframenode-i.md)设置跨ArkTS语言访问选项。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CrossLanguageOptions](arkts-arkui-framenode-crosslanguageoptions-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100022](../errorcode-node.md#100022-framenode节点的组件类型不支持调整跨语言的通用属性设置权限) |

## setLayoutPosition

```TypeScript
setLayoutPosition(position: Position): void
```

设置FrameNode的布局后的位置，默认单位PX。建议在[onLayout](#onlayout)方法中调用，用于设置自定义布局的结果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | [Position](arkts-arkui-position-t.md) | 是 |

## setMeasuredSize

```TypeScript
setMeasuredSize(size: Size): void
```

设置FrameNode的测量后的尺寸，默认单位PX。若设置的宽高为负数，自动取零。建议在[onMeasure](#onmeasure)方法中调用，用于设置自定义测量的结果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | Size | 是 |

## setNeedsLayout

```TypeScript
setNeedsLayout(): void
```

该方法会将FrameNode标记为需要布局的状态，下一帧将会进行重新布局，触发[onMeasure](#onmeasure)和[onLayout](#onlayout)方 法的调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## commonAttribute

```TypeScript
get commonAttribute(): CommonAttribute
```

获取FrameNode中持有的CommonAttribute接口，用于设置通用属性和 通用事件。仅可以修改自定义节点的属性。

> **说明：**&gt;
> FrameNode的效果参考对齐方式为顶部起始端的Stack容器组件。&gt;
> FrameNode的属性支持情况参考
> [属性或事件对attributemodifier的支持情况](../../../ui/arkts-user-defined-extension-attributeModifier.md#属性或事件对attributemodifier的支持情况)。

**类型：** [CommonAttribute](../arkts-components/arkts-arkui-common-attribute.md)

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## commonEvent

```TypeScript
get commonEvent(): UICommonEvent
```

获取FrameNode中持有的UICommonEvent对象，用于设置基础事件。设置的基础事件与声明式定义的事件平行，参与事件竞争；设置的基础事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。LazyForEach场景下，由于存在节点的销毁重建，对于重建的节点需要重新设置事件回调才能保证监听事件正常响应。

**类型：** [UICommonEvent](../arkts-components/arkts-arkui-uicommonevent-i.md)

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## gestureEvent

```TypeScript
get gestureEvent(): UIGestureEvent
```

获取FrameNode中持有的UIGestureEvent对象，用于设置组件绑定的手势事件。通过gestureEvent接口设置的手势不会覆盖通过 绑定手势事件绑定的手势，两者同时设置了手势时，优先回调绑定手势事件设置的手势事件。LazyForEach场景下，由于存在节点的销毁重建，对于重建的节点需要重新设置手势事件回调才能保证监听事件正常响应。

**类型：** [UIGestureEvent](../arkts-components/arkts-arkui-uigestureevent-i.md)

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
