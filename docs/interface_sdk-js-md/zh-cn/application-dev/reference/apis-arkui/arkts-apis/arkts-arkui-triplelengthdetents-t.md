# TripleLengthDetents

```TypeScript
export type TripleLengthDetents = [
    (SheetSize | Length),
    SheetSize | Length | undefined,
    SheetSize | Length | undefined
]
```

定义了三个高度的挡位。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**属性类型：** [
    (SheetSize | Length),
    SheetSize | [Length](arkts-arkui-length-t.md) | undefined,
    SheetSize | [Length](arkts-arkui-length-t.md) | undefined
]
