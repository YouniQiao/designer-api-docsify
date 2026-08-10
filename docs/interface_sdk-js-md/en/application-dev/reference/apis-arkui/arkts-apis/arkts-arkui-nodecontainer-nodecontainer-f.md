# NodeContainer

## NodeContainer

```TypeScript
export declare function NodeContainer(
    controller: NodeController
): NodeContainerAttribute
```

创建NodeContainer组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function NodeContainer(    controller: NodeController): NodeContainerAttribute--><!--Device-unnamed-export declare function NodeContainer(    controller: NodeController): NodeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [NodeController](arkts-arkui-nodecontroller-c.md) | Yes | 一个NodeController对象，其用于控制NodeContainer中的节点的上树和下树，反映NodeContainer容器的生命周期。 |

**Return value:**

| Type | Description |
| --- | --- |
| [NodeContainerAttribute](../arkts-components/arkts-arkui-nodecontainer-attribute.md) |  |


## NodeContainer

```TypeScript
export declare function NodeContainer(
    style: CustomBuilderT<NodeContainerAttribute>
): NodeContainerAttribute
```

定义NodeContainer组件。需要在组件属性设置开始时调用setNodeContainerOptions，并在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function NodeContainer(    style: CustomBuilderT<NodeContainerAttribute>): NodeContainerAttribute--><!--Device-unnamed-export declare function NodeContainer(    style: CustomBuilderT<NodeContainerAttribute>): NodeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;NodeContainerAttribute&gt; | Yes | 用于设置NodeContainer属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [NodeContainerAttribute](../arkts-components/arkts-arkui-nodecontainer-attribute.md) | NodeContainer属性实例。 |

