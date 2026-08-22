# NodeContainer

## NodeContainer

```TypeScript
@ComponentBuilder
export declare function NodeContainer(
    controller: NodeController
): NodeContainerAttribute
```

Defines NodeContainer Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function NodeContainer(    controller: NodeController): NodeContainerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function NodeContainer(    controller: NodeController): NodeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [NodeController](../../apis-arkui/arkts-apis/arkts-arkui-nodecontroller-c.md) | Yes | instance of NodeController. |

**Return value:**

| Type | Description |
| --- | --- |
| [NodeContainerAttribute](arkts-nodecontainer-attribute.md) |  |


## NodeContainer

```TypeScript
@Builder
export declare function NodeContainer(
    style: CustomBuilderT<NodeContainerAttribute>
): NodeContainerAttribute
```

Defines NodeContainer Component. It requires calling setNodeContainerOptions at start of component attribute set-up, and it requires calling applyAttributesFinish at end of component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function NodeContainer(    style: CustomBuilderT<NodeContainerAttribute>): NodeContainerAttribute--><!--Device-unnamed-@Builderexport declare function NodeContainer(    style: CustomBuilderT<NodeContainerAttribute>): NodeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[NodeContainerAttribute](arkts-nodecontainer-attribute.md)&gt; | Yes | callback to set up NodeContainer's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [NodeContainerAttribute](arkts-nodecontainer-attribute.md) | The attribute of NodeContainer. |

