# OnScrollVisibleContentChangeCallback

```TypeScript
export type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void
```

有子组件划入或划出List显示区域时触发。

List从有子组件变成空的List时，上报的start和end参数会保留上次有子组件时的值。

start和end的index同时返回0，代表List内只有一个子组件。

> **说明：**
> 
> 从API version 14开始，该接口支持在[attributeModifier](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void--><!--Device-unnamed-export type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | [VisibleListContentInfo](../arkts-components/arkts-arkui-visiblelistcontentinfo-i.md) | Yes | 1. 通过该参数获取List显示区域第一个子组件在List中的索引值。<br/>2. 如果当前List显示区域第一个子组件是ListItemGroup，可 以获取当前List显示区域第一个组件属于该ListItemGroup的哪一区域。<br/>3. 如果当前List显示区域第一个组件是ListItemGroup内的ListItem，可以获取该ListItem在 ListItemGroup内的索引值。 |
| end | [VisibleListContentInfo](../arkts-components/arkts-arkui-visiblelistcontentinfo-i.md) | Yes | 1. 通过该参数获取List显示区域最后一个子组件在List中的索引值。<br/>2. 如果当前List显示区域最后一个子组件是ListItemGroup，可 以获取当前List显示区域最后一个组件属于该ListItemGroup的哪一区域。<br/>3. 如果当前List显示区域最后一个组件是ListItemGroup内的ListItem，可以获取该ListItem在 ListItemGroup内的索引值。 |

