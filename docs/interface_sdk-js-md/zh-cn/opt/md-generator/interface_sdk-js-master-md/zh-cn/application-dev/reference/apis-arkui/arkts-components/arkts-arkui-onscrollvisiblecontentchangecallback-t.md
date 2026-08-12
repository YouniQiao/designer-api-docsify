# OnScrollVisibleContentChangeCallback

```TypeScript
declare type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void
```

有子组件划入或划出List显示区域时触发。

API版本26.0.0开始，List从有子组件变成空的List时，上报的start和end参数的index成员为-1，itemGroupArea和itemIndexInGroup成员为undefined。API版本26.0.0以前，List从有子组件变成空的List时，上报的start和end参数会保留上次有子组件时的值。

start和end的index同时返回0，代表List内只有一个子组件。

> **说明：**
> 
> 从API version 14开始，该接口支持在[attributeModifier](CommonMethod#attributeModifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void--><!--Device-unnamed-declare type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | [VisibleListContentInfo](arkts-arkui-visiblelistcontentinfo-i.md) | 是 |
| end | [VisibleListContentInfo](arkts-arkui-visiblelistcontentinfo-i.md) | 是 |
