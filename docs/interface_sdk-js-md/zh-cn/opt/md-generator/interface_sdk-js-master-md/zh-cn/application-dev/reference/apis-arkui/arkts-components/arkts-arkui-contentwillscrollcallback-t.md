# ContentWillScrollCallback

```TypeScript
declare type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean
```

Swiper即将滑动前触发的回调，返回值表示是否允许此次滑动。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本15开始，该接口支持在ArkTS卡片中使用。

<!--Device-unnamed-declare type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean--><!--Device-unnamed-declare type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | [SwiperContentWillScrollResult](arkts-arkui-swipercontentwillscrollresult-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
