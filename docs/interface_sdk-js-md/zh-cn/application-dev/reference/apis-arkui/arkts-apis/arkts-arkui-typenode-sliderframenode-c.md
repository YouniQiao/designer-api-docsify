# SliderFrameNode

定义Slider类型的FrameNode。

**继承/实现关系：** SliderFrameNode extends TypedFrameNode<SliderAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(options?: SliderOptions): SliderAttribute
```

初始化Slider类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SliderOptions](../arkts-components/arkts-arkui-slideroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](../arkts-components/arkts-arkui-slider-attribute.md) |
