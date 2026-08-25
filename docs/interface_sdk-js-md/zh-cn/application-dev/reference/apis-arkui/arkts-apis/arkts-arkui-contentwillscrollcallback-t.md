# ContentWillScrollCallback

```TypeScript
export type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean
```

Swiper即将滑动前触发的回调，返回值表示是否允许此次滑动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | [SwiperContentWillScrollResult](arkts-arkui-swiper-swipercontentwillscrollresult-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
