# OnListScrollIndexCallback

```TypeScript
export type OnListScrollIndexCallback = (start: int, end: int, center: int) => void
```

List组件可见区域item变化事件的回调类型。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| end | int | 是 |
| center | int | 是 |
