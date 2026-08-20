# BuilderNode

## Summary

### Classes

| Name | Description |
| --- | --- |
| [BuilderNode](arkts-arkui-buildernode-c.md) | The **BuilderNode** module provides APIs for a BuilderNode – a custom node that can be used to mount built-in components. A BuilderNode can be used only as a leaf node. For details, see [BuilderNode Development](../../../ui/arkts-user-defined-arktsNode-builderNode.md). For best practices, see [Dynamic Component Creation: Dynamically Adding, Updating, and Deleting Components](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-ui-dynamic-operations#section153921947151012). |
| [ReactiveBuilderNode](arkts-arkui-buildernode-reactivebuildernode-c.md) | *ReactiveBuilderNode** uses the stateless UI method [@Builder](../../../ui/state-management/arkts-builder.md) to generate a component tree and holds the root node of the component tree. A ReactiveBuilderNode cannot be defined as a state variable. FrameNode held in **ReactiveBuilderNode** is used only to mount the ReactiveBuilderNode as a child node to another FrameNode. Undefined behavior may occur if you set attributes or perform operations on subnodes of the FrameNode held by the ReactiveBuilderNode. Therefore, after you have obtained a RenderNode through the [getFrameNode](../../apis-default/arkts-apis/arkts-buildernode-c.md#getframenode) method of the ReactiveBuilderNode and the [getRenderNode](../../apis-default/arkts-apis/arkts-framenode-c.md#getrendernode) method of the FrameNode, avoid setting the attributes or operating the subnodes through APIs of [RenderNode](../../apis-default/arkts-apis/arkts-rendernode-c.md). |

### Interfaces

| Name | Description |
| --- | --- |
| [BuildOptions](arkts-arkui-buildernode-buildoptions-i.md) | Defines the optional build options. |
| [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | Provides optional parameters for creating a BuilderNode. |

### Enums

| Name | Description |
| --- | --- |
| [NodeRenderType](arkts-arkui-buildernode-noderendertype-e.md) | Enumerates the node rendering types. |

### Types

| Name | Description |
| --- | --- |
| [InputEventType](arkts-arkui-inputeventtype-t.md) | Defines the type of input event to be dispatched. For details, see [postInputEvent](../../apis-default/arkts-apis/arkts-buildernode-c.md#postinputevent). |

