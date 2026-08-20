# TreeController

Implements a **TreeController** object, which can be bound to a tree view component to control the node information of the component. One **TreeController** object can be bound to only one tree view component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class TreeController--><!--Device-unnamed-export declare class TreeController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## addNode

```TypeScript
public addNode(nodeParam?: NodeParam): TreeController
```

Adds a child node to the selected node.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeController-public addNode(nodeParam?: NodeParam): TreeController--><!--Device-TreeController-public addNode(nodeParam?: NodeParam): TreeController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nodeParam | [NodeParam](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-treeview-nodeparam-i.md) | No | Node information. |

**Return value:**

| Type | Description |
| --- | --- |
| [TreeController](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-treeview-treecontroller-c.md) | Controller of the **TreeView** component. |

## buildDone

```TypeScript
public buildDone(): void
```

Builds a tree view. After a node is added, this API must be called to save the tree information.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeController-public buildDone(): void--><!--Device-TreeController-public buildDone(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modifyNode

```TypeScript
public modifyNode(): void
```

Modifies the selected node.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeController-public modifyNode(): void--><!--Device-TreeController-public modifyNode(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## refreshNode

```TypeScript
public refreshNode(parentId: int, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void
```

Refreshes the tree view. You can call this API to update the information about the current node.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeController-public refreshNode(parentId: int, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void--><!--Device-TreeController-public refreshNode(parentId: int, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parentId | int | Yes | ID of the parent node. <br>The value must be greater than or equal to -1. |
| parentSubTitle | ResourceStr | Yes | Secondary text of the parent node. |
| currentSubtitle | ResourceStr | Yes | Secondary text of the current node. |

## removeNode

```TypeScript
public removeNode(): void
```

Removes the selected node.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeController-public removeNode(): void--><!--Device-TreeController-public removeNode(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

