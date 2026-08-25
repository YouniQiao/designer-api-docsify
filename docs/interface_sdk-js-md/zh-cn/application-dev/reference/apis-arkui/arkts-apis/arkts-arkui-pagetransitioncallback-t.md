# PageTransitionCallback

```TypeScript
export type PageTransitionCallback = (type: RouteType, progress: double) => void
```

页面转场事件回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [RouteType](arkts-arkui-pagetransition-routetype-e.md) | 是 |
| progress | double | 是 |
