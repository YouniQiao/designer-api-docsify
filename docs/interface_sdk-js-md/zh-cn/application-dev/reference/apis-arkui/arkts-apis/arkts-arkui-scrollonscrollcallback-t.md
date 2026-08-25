# ScrollOnScrollCallback

```TypeScript
export type ScrollOnScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState) => void
```

Scroll滚动时触发的回调。  
> **说明：**
> 若通过[onScrollFrameBegin](arkts-arkui-scroll-scrollattribute-i.md#onscrollframebegin)事件和[scrollBy](arkts-arkui-scroll-scroller-c.md#scrollby)方法实现容器嵌套滚动，需设置子滚动节点的
> EdgeEffect为None。如Scroll嵌套List滚动时，List组件的edgeEffect
> 属性需设置为EdgeEffect.None。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| xOffset | double | 是 |
| yOffset | double | 是 |
| scrollState | [ScrollState](../arkts-components/arkts-arkui-scrollstate-e.md) | 是 |
