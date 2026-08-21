# CallbackParam

Declare CallbackParam

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface CallbackParam--><!--Device-unnamed-export interface CallbackParam-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { CallbackParam, NodeParam, TreeController, TreeListenType, TreeListener, TreeListenerManager, TreeView } from '@kit.ArkUI';
import { CallbackParamV2, NodeParamV2, TreeControllerV2, TreeListenerV2, TreeListenerManagerV2, TreeViewV2 } from '@kit.ArkUI';
```

## childIndex

```TypeScript
childIndex?: int
```

返回子节点在父节点下的索引位置，用于标识子节点在父节点的子节点列表中的位置。

取值范围：大于等于-1，-1表示无效索引或无子节点。

默认值：-1

**类型：** int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CallbackParam-childIndex?: int--><!--Device-CallbackParam-childIndex?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## currentNodeId

```TypeScript
currentNodeId: int
```

返回当前子节点id。

取值范围：大于等于0。

**类型：** int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CallbackParam-currentNodeId: int--><!--Device-CallbackParam-currentNodeId: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## parentNodeId

```TypeScript
parentNodeId?: int
```

返回当前父节点id。

取值范围：大于等于-1。

默认值：-1

**类型：** int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CallbackParam-parentNodeId?: int--><!--Device-CallbackParam-parentNodeId?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

