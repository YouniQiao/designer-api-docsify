# RenderNode

## Summary

### Classes

| Name | Description |
| --- | --- |
| [RenderNode](arkts-arkui-rendernode-c.md) | The **RenderNode** module provides APIs for creating a RenderNode in custom drawing settings with C APIs. &gt; **NOTE：**&gt; &gt; - Avoid modifying RenderNodes in BuilderNode. The FrameNode associated &gt; with BuilderNode is designed solely for mounting the BuilderNode as a child component. Modifying attributes or &gt; operations on the FrameNode's child nodes or their corresponding RenderNodes may lead to undefined behavior, &gt; including display, event handling, and stability issues. &gt; &gt; - RenderNode objects do not support JSON serialization. |

