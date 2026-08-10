# CallbackParamV2

节点回调参数接口，用于传递节点事件回调的参数信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface CallbackParamV2--><!--Device-unnamed-export interface CallbackParamV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { TreeListenerManagerV2, NodeParamV2, CallbackParamV2, TreeControllerV2, TreeViewV2, TreeListenerV2 } from 'kits/@kit.ArkUI';
```

## childIndex

```TypeScript
childIndex?: int
```

返回子索引。

取值范围：大于等于-1。

默认值：-1

仅在节点移动事件中有效，表示移动后的位置索引。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CallbackParamV2-childIndex?: int--><!--Device-CallbackParamV2-childIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## currentNodeId

```TypeScript
currentNodeId: int
```

返回当前子节点id。

取值范围：大于等于0。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CallbackParamV2-currentNodeId: int--><!--Device-CallbackParamV2-currentNodeId: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## parentNodeId

```TypeScript
parentNodeId?: int
```

返回当前父节点id。

取值范围：大于等于-1。

默认值：-1

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CallbackParamV2-parentNodeId?: int--><!--Device-CallbackParamV2-parentNodeId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

