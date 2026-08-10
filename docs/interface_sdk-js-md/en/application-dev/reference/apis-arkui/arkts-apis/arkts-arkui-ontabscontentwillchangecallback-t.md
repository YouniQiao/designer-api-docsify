# OnTabsContentWillChangeCallback

```TypeScript
export type OnTabsContentWillChangeCallback = (currentIndex: int, comingIndex: int) => boolean
```

自定义Tabs页面切换拦截事件能力，新页面即将显示时触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTabsContentWillChangeCallback = (currentIndex: int, comingIndex: int) => boolean--><!--Device-unnamed-export type OnTabsContentWillChangeCallback = (currentIndex: int, comingIndex: int) => boolean-End-->

**System capability:** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| currentIndex | int | Yes | 当前显示页面的index索引，索引从0开始计算。 取值范围为全体整数 取值限定为整数。 |
| comingIndex | int | Yes | 将要显示的新页面的index索引。 取值范围为全体整数 取值限定为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - |

