# OnScrollVisibleContentChangeCallback

```TypeScript
export type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void
```

有子组件划入或划出List显示区域时触发。List从有子组件变成空的List时，上报的start和end参数会保留上次有子组件时的值。start和end的index同时返回0，代表List内只有一个子组件。

> **说明：**&gt;
> 从API version 14开始，该接口支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | [VisibleListContentInfo](arkts-arkui-list-visiblelistcontentinfo-i.md) | 是 |
| end | [VisibleListContentInfo](arkts-arkui-list-visiblelistcontentinfo-i.md) | 是 |
