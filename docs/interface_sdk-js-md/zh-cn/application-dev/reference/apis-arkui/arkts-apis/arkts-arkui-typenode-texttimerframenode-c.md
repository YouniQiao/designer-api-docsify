# TextTimerFrameNode

定义TextTimer类型的FrameNode。

**继承/实现关系：** TextTimerFrameNode extends TypedFrameNode<TextTimerAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(options?: TextTimerOptions): TextTimerAttribute
```

初始化TextTimer类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TextTimerOptions](../arkts-components/arkts-arkui-texttimeroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |
