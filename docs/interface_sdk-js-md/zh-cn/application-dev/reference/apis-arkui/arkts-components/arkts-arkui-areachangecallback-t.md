# AreaChangeCallback

```TypeScript
declare type AreaChangeCallback = (oldValue: Area, newValue: Area) => void
```

组件区域变化事件的回调类型。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oldValue | [Area](../arkts-apis/arkts-arkui-area-i.md) | 是 |
| newValue | [Area](../arkts-apis/arkts-arkui-area-i.md) | 是 |
