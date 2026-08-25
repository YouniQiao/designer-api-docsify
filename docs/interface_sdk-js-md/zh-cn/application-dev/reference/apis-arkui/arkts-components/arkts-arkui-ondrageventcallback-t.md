# OnDragEventCallback

```TypeScript
declare type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void
```

拖拽事件的回调函数。

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为15。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [DragEvent](arkts-arkui-dragevent-i.md) | 是 |
| extraParams | string | 否 |
