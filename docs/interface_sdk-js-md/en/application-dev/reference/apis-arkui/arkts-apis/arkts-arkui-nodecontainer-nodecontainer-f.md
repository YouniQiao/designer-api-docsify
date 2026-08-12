# NodeContainer

## NodeContainer

```TypeScript
export declare function NodeContainer(
    controller: NodeController
): NodeContainerAttribute
```

Defines NodeContainer Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function NodeContainer(    controller: NodeController): NodeContainerAttribute--><!--Device-unnamed-export declare function NodeContainer(    controller: NodeController): NodeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [NodeController](arkts-arkui-nodecontroller-c.md) | Yes | instance of NodeController. |

**Return value:**

| Type | Description |
| --- | --- |
| [NodeContainerAttribute](arkts-arkui-nodecontainer-nodecontainerattribute-i.md) |  |


## NodeContainer

```TypeScript
export declare function NodeContainer(
    style: CustomBuilderT<NodeContainerAttribute>
): NodeContainerAttribute
```

Defines NodeContainer Component. It requires calling setNodeContainerOptions at start of component attribute set-up,and it requires calling applyAttributesFinish at end of component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function NodeContainer(    style: CustomBuilderT<NodeContainerAttribute>): NodeContainerAttribute--><!--Device-unnamed-export declare function NodeContainer(    style: CustomBuilderT<NodeContainerAttribute>): NodeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[NodeContainerAttribute](arkts-arkui-nodecontainer-nodecontainerattribute-i.md)&gt; | Yes | callback to set up NodeContainer's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [NodeContainerAttribute](arkts-arkui-nodecontainer-nodecontainerattribute-i.md) | The attribute of NodeContainer. |

