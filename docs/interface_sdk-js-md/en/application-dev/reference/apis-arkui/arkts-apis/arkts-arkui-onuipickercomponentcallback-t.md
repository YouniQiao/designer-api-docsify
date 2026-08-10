# OnUIPickerComponentCallback

```TypeScript
export declare type OnUIPickerComponentCallback = (selectedIndex: int) => void
```

定义[onChange](onChange)和[onScrollStop](onScrollStop)事件的回调类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type OnUIPickerComponentCallback = (selectedIndex: int) => void--><!--Device-unnamed-export declare type OnUIPickerComponentCallback = (selectedIndex: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectedIndex | int | Yes | 当前选中项的索引值。</br>取值范围：[0, 子组件的个数-1]内的整数。 |

