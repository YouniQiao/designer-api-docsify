# TreeListenerV2

树视图组件的监听器，可以将此对象绑定至树视图组件，然后通过它监听树视图的节点的变化，同一个树视图监听器不可以控制多个树视图组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class TreeListenerV2--><!--Device-unnamed-export declare class TreeListenerV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { TreeListenerManagerV2, NodeParamV2, CallbackParamV2, TreeControllerV2, TreeViewV2, TreeListenerV2 } from 'kits/@kit.ArkUI';
```

## offNodeAdd

```TypeScript
offNodeAdd(callback?: OnChangedCallback): void
```

取消节点添加事件监听。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-offNodeAdd(callback?: OnChangedCallback): void--><!--Device-TreeListenerV2-offNodeAdd(callback?: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | No |  |

## offNodeClick

```TypeScript
offNodeClick(callback?: OnChangedCallback): void
```

取消节点点击事件监听。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-offNodeClick(callback?: OnChangedCallback): void--><!--Device-TreeListenerV2-offNodeClick(callback?: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | No |  |

## offNodeDelete

```TypeScript
offNodeDelete(callback?: OnChangedCallback): void
```

取消节点删除事件监听。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-offNodeDelete(callback?: OnChangedCallback): void--><!--Device-TreeListenerV2-offNodeDelete(callback?: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | No |  |

## offNodeModify

```TypeScript
offNodeModify(callback?: OnChangedCallback): void
```

取消节点修改事件监听。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-offNodeModify(callback?: OnChangedCallback): void--><!--Device-TreeListenerV2-offNodeModify(callback?: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | No |  |

## offNodeMove

```TypeScript
offNodeMove(callback?: OnChangedCallback): void
```

取消节点移动事件监听。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-offNodeMove(callback?: OnChangedCallback): void--><!--Device-TreeListenerV2-offNodeMove(callback?: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | No |  |

## onNodeAdd

```TypeScript
onNodeAdd(callback: OnChangedCallback): void
```

注册节点添加事件监听，持续监听节点添加事件。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onNodeAdd(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onNodeAdd(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

## onNodeClick

```TypeScript
onNodeClick(callback: OnChangedCallback): void
```

注册节点点击事件监听，持续监听节点点击事件。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onNodeClick(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onNodeClick(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

## onNodeDelete

```TypeScript
onNodeDelete(callback: OnChangedCallback): void
```

注册节点删除事件监听，持续监听节点删除事件。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onNodeDelete(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onNodeDelete(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

## onNodeModify

```TypeScript
onNodeModify(callback: OnChangedCallback): void
```

注册节点修改事件监听，持续监听节点修改事件。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onNodeModify(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onNodeModify(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

## onNodeMove

```TypeScript
onNodeMove(callback: OnChangedCallback): void
```

注册节点移动事件监听，持续监听节点移动事件。节点移动通过拖拽操作触发。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onNodeMove(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onNodeMove(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

## onceNodeAdd

```TypeScript
onceNodeAdd(callback: OnChangedCallback): void
```

注册节点添加事件监听，监听一次后自动销毁。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onceNodeAdd(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onceNodeAdd(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

## onceNodeClick

```TypeScript
onceNodeClick(callback: OnChangedCallback): void
```

注册节点点击事件监听，监听一次后自动销毁。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onceNodeClick(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onceNodeClick(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

## onceNodeDelete

```TypeScript
onceNodeDelete(callback: OnChangedCallback): void
```

注册节点删除事件监听，监听一次后自动销毁。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onceNodeDelete(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onceNodeDelete(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

## onceNodeModify

```TypeScript
onceNodeModify(callback: OnChangedCallback): void
```

注册节点修改事件监听，监听一次后自动销毁。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onceNodeModify(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onceNodeModify(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

## onceNodeMove

```TypeScript
onceNodeMove(callback: OnChangedCallback): void
```

注册节点移动事件监听，监听一次后自动销毁。使用callback回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerV2-onceNodeMove(callback: OnChangedCallback): void--><!--Device-TreeListenerV2-onceNodeMove(callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | Yes |  |

