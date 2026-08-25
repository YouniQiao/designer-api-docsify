# GestureRecognizerJudgeBeginCallback

```TypeScript
declare type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>,
  touchRecognizers?: Array<TouchRecognizer>) => GestureJudgeResult
```

自定义手势识别器判定回调类型。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [BaseGestureEvent](../arkts-apis/arkts-arkui-basegestureevent-i.md) | 是 |
| current | [GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md) | 是 |
| recognizers | Array&lt;[GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | 是 |
| touchRecognizers | Array&lt;[TouchRecognizer](../arkts-apis/arkts-arkui-touchrecognizer-c.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [GestureJudgeResult](../arkts-apis/arkts-arkui-gesturejudgeresult-e.md) |
