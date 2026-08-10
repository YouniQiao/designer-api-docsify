# OnSelectCallback

```TypeScript
export type OnSelectCallback = (index: int, selectStr: string) => void
```

Select组件选择项的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnSelectCallback = (index: int, selectStr: string) => void--><!--Device-unnamed-export type OnSelectCallback = (index: int, selectStr: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 选中的项的索引。 |
| selectStr | string | Yes | 选中的项的文本内容。 |

