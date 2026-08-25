# GestureCollectInterceptCallback

```TypeScript
export type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,
    touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention
```

Defines the callback type used in onGestureCollectIntercept.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| recognizers | Array&lt;[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)&gt; | 是 |
| touchRecognizers | Array&lt;[TouchRecognizer](arkts-arkui-touchrecognizer-c.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [GestureCollectIntervention](arkts-arkui-gesturecollectintervention-e.md) |
