# NodeController

NodeController用于实现自定义节点的创建、显示、更新等操作的管理，并负责将自定义节点挂载到[NodeContainer](node_container)上。

> **说明：**
> 
> - NodeController对象不支持使用JSON序列化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class NodeController--><!--Device-unnamed-export declare abstract class NodeController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToAppear

```TypeScript
aboutToAppear(): void
```

> **说明：**
> 
> 回调时机参考[onAppear](arkts-arkui-common-commonmethod-i.md#onappear)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-aboutToAppear(): void--><!--Device-NodeController-aboutToAppear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToDisappear

```TypeScript
aboutToDisappear(): void
```

> **说明：**
> 
> 回调时机参考[onDisAppear](arkts-arkui-common-commonmethod-i.md#ondisappear)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-aboutToDisappear(): void--><!--Device-NodeController-aboutToDisappear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToResize

```TypeScript
aboutToResize(size: Size): void
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-aboutToResize(size: Size): void--><!--Device-NodeController-aboutToResize(size: Size): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [Size](arkts-arkui-graphics-size-i.md) | Yes | 用于返回组件布局大小的宽和高，单位为vp。 |

## makeNode

```TypeScript
abstract makeNode(uiContext: UIContext): FrameNode | null
```

当实例绑定的[NodeContainer](node_container)创建的时候进行回调。回调方法将返回一个节点，将该节点挂载至[NodeContainer](node_container)。

或者可以通过NodeController的rebuild()方法进行回调的触发。

> **说明：**
> 
> [NodeContainer](node_container)不支持跨实例复用。如果出现跨实例复用[NodeContainer](node_container)，传入
> [NodeContainer](node_container)的[NodeController](arkts-arkui-nodecontroller-c.md)触发
> [makeNode](arkts-arkui-nodecontroller-c.md#makenode)回调方法时，入参中的[UIContext](arkts-arkui-uicontext.md)对象可能为undefined，此时需要开发者
> 判断入参中的[UIContext](arkts-arkui-uicontext.md)对象是否为undefined，防止后续使用此入参时出现
> [UIContext无效的JS异常](../../../ui/arkts-wrong-uicontext-debug.md#定位uicontext错误问题)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-abstract makeNode(uiContext: UIContext): FrameNode | null--><!--Device-NodeController-abstract makeNode(uiContext: UIContext): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 回调该方法的时候，绑定[NodeContainer](node_container)的UI上下文。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](arkts-arkui-framenode-c.md) | Returns a FrameNode or null. |

## onAttach

```TypeScript
onAttach(): void
```

> **说明：**
> 
> 回调时机参考[onAttach](arkts-arkui-common-commonmethod-i.md#onattach)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onAttach(): void--><!--Device-NodeController-onAttach(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onBind

```TypeScript
onBind(containerId: long): void
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onBind(containerId: long): void--><!--Device-NodeController-onBind(containerId: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | long | Yes | 回调该方法时，NodeController与NodeContainerId对应的[NodeContainer](node_container)绑定完成。 |

## onDetach

```TypeScript
onDetach(): void
```

> **说明：**
> 
> 回调时机参考[onDetach](arkts-arkui-common-commonmethod-i.md#ondetach)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onDetach(): void--><!--Device-NodeController-onDetach(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTouchEvent

```TypeScript
onTouchEvent(event: TouchEvent): void
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onTouchEvent(event: TouchEvent): void--><!--Device-NodeController-onTouchEvent(event: TouchEvent): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [TouchEvent](../arkts-components/arkts-arkui-touchevent-i.md) | Yes | 触摸事件。 |

## onUnbind

```TypeScript
onUnbind(containerId: long): void
```

OnUnbind方法。解除NodeController与NodeContainer的绑定时执行。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onUnbind(containerId: long): void--><!--Device-NodeController-onUnbind(containerId: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | long | Yes | 回调该方法时，NodeController与NodeContainerId对应的[NodeContainer](node_container)解绑完成。 |

## onWillBind

```TypeScript
onWillBind(containerId: long): void
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onWillBind(containerId: long): void--><!--Device-NodeController-onWillBind(containerId: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | long | Yes | 回调该方法时，NodeController与NodeContainerId对应的[NodeContainer](node_container)即将绑定。 |

## onWillUnbind

```TypeScript
onWillUnbind(containerId: long): void
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onWillUnbind(containerId: long): void--><!--Device-NodeController-onWillUnbind(containerId: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | long | Yes | 回调该方法时，NodeController与NodeContainerId对应的[NodeContainer](node_container)即将解绑。 |

## rebuild

```TypeScript
rebuild(): void
```

调用此接口通知[NodeContainer](node_container)组件重新回调[makeNode](arkts-arkui-nodecontroller-c.md#makenode)方法，更改子节点。

> **说明：**
> > 由于rebuild方法为应用主动调用的方法，且该操作与UI相关。需要开发者自行保证调用该接口时UI上下文有效，即与绑定的NodeContainer保持UI上下文一致。
> 
> 监听回调等[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)时，可以通过[UIContext](arkts-arkui-uicontext.md)的
> [runScopedTask](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#runscopedtask)方法明确调用时的UI上下文。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-rebuild(): void--><!--Device-NodeController-rebuild(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

