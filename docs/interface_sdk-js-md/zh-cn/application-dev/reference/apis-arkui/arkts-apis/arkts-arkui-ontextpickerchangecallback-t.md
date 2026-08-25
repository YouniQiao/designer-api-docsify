# OnTextPickerChangeCallback

```TypeScript
export type OnTextPickerChangeCallback = (selectItem: string | string[], index: int | int[]) => void
```

滑动选中TextPicker文本内容后，触发该回调。当显示文本或图片加文本列表时，选中项的文本值为选中项中的文本值，当显示图片列表时， 选中项的文本值为空。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| selectItem | string \| string[] | 是 |
| index | int \| int[] | 是 |
