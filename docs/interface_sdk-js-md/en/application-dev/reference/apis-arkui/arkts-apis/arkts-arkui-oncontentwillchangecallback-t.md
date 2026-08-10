# OnContentWillChangeCallback

```TypeScript
export type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean
```

页面内容即将发生变化时触发的回调函数，用于拦截页面切换，开发者可通过返回值控制是否允许切换。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean--><!--Device-unnamed-export type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| currentIndex | number | Yes | 当前页签索引。 |
| comingIndex | number | Yes | 即将切换的页签索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - |

