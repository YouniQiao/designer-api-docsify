# TreeControllerV2

树视图组件的控制器，可以将此对象绑定至树视图组件，然后通过它控制树的节点信息，同一个控制器不可以控制多个树视图组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class TreeControllerV2--><!--Device-unnamed-export declare class TreeControllerV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { TreeListenerManagerV2, NodeParamV2, CallbackParamV2, TreeControllerV2, TreeViewV2, TreeListenerV2 } from 'kits/@kit.ArkUI';
```

## addNode

```TypeScript
addNode(nodeParam?: NodeParamV2): TreeControllerV2
```

点击某个节点后，调用该方法可以触发新增子节点。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeControllerV2-addNode(nodeParam?: NodeParamV2): TreeControllerV2--><!--Device-TreeControllerV2-addNode(nodeParam?: NodeParamV2): TreeControllerV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nodeParam | [NodeParamV2](arkts-arkui-arkui-advanced-treeviewv2-nodeparamv2-i.md) | No | 节点信息，用于指定新增节点的属性。如果不传该参数，在当前选中的节点下添加一个标题为"新建文件夹"的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TreeControllerV2](arkts-arkui-arkui-advanced-treeviewv2-treecontrollerv2-c.md) | 树视图组件的控制器。 |

## buildDone

```TypeScript
buildDone(): void
```

建立树视图。节点增加完毕后，必须调用该方法，触发树信息的保存。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeControllerV2-buildDone(): void--><!--Device-TreeControllerV2-buildDone(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modifyNode

```TypeScript
modifyNode(): void
```

点击某个节点后，调用该方法可以触发修改该节点，该节点进入编辑态。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeControllerV2-modifyNode(): void--><!--Device-TreeControllerV2-modifyNode(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## refreshNode

```TypeScript
refreshNode(parentId: int, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void
```

更新树视图。调用该方法，更新当前节点的信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeControllerV2-refreshNode(parentId: int, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void--><!--Device-TreeControllerV2-refreshNode(parentId: int, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parentId | int | Yes | 父节点Id。&lt;br /&gt;取值范围：大于等于-1。 |
| parentSubTitle | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes | 父节点副标题。 |
| currentSubtitle | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes | 当前节点副标题。 |

## removeNode

```TypeScript
removeNode(): void
```

点击某个节点后，调用该方法可以触发删除该节点。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeControllerV2-removeNode(): void--><!--Device-TreeControllerV2-removeNode(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

