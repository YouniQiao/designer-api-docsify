# TextPickerScrollStopCallback

```TypeScript
export type TextPickerScrollStopCallback = (value: string | string[], index: int | int[]) => void
```

定义触发onScrollStop事件的回调类型。当显示文本或图片加文本列表时，value值为选中项中的文本值，当显示图片列表时，value值为空。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| string[] | 是 |
| index | int \| int[] | 是 |
