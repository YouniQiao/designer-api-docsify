# TextPickerEnterSelectedAreaCallback

```TypeScript
export type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: int | int[]) => void
```

定义触发onEnterSelectedArea事件的回调类型。在多列联动场景中，不建议使用该回调，由于该回调标识的是滑动过程中选项进入分割线区域内的节点，而跟随变化的选项并不涉及滑动，因此， 回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| string[] | 是 |
| index | int \| int[] | 是 |
