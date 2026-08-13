# TextPickerEnterSelectedAreaCallback

```TypeScript
declare type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void
```

定义触发onEnterSelectedArea事件的回调类型。

**起始版本：** 18

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void--><!--Device-unnamed-declare type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| string[] | 是 |
| index | number \| number[] | 是 |
