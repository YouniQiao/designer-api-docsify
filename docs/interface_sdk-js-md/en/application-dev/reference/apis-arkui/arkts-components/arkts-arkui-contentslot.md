# ContentSlot

用于渲染Native侧使用C-API创建的组件，并通过Content管理器管理这些组件。

支持混合模式开发，当容器是ArkTS组件，子组件在Native侧创建时，推荐使用ContentSlot占位组件。

## ContentSlot

```TypeScript
ContentSlot(content: Content)
```

创建ContentSlot占位组件，用于渲染Content管理器中Native侧创建的组件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ContentSlotInterface-(content: Content): ContentSlotAttribute--><!--Device-ContentSlotInterface-(content: Content): ContentSlotAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [Content](arkts-arkui-content-t.md) | Yes | Content作为ContentSlot的管理器，通过Native侧提供的接口，可以注册并触发ContentSlot的上下树（即组件节点加入或移出组件渲染树）事件回调以及管 理ContentSlot的子组件。 |

## Summary

- [Content](arkts-arkui-contentslot-content-t.md)
