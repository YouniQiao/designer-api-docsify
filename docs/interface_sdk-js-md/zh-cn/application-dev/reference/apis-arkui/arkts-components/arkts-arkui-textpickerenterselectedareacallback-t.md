# TextPickerEnterSelectedAreaCallback

```TypeScript
declare type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void
```

定义触发onEnterSelectedArea事件的回调类型。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| string[] | 是 |
| index | number \| number[] | 是 |
