# OnTabsContentWillChangeCallback

```TypeScript
export type OnTabsContentWillChangeCallback = (currentIndex: int, comingIndex: int) => boolean
```

自定义Tabs页面切换拦截事件能力，新页面即将显示时触发的回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| currentIndex | int | 是 |
| comingIndex | int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
