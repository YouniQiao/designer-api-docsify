# OnTabsContentWillChangeCallback

```TypeScript
declare type OnTabsContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean
```

自定义Tabs页面切换拦截事件能力，新页面即将显示时触发的回调。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type OnTabsContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean--><!--Device-unnamed-declare type OnTabsContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| currentIndex | number | 是 |
| comingIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
