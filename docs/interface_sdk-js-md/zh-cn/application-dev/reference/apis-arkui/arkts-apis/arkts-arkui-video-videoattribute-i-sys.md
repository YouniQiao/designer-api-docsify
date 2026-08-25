# VideoAttribute

用于播放视频文件并控制其播放状态的组件。@extends CommonMethod @interface VideoAttribute

**继承/实现关系：** VideoAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## surfaceBackgroundColor

```TypeScript
default surfaceBackgroundColor(color: ColorMetrics | undefined): this
```

Set background color of the surface holden by Video(only support Color.Black and Color.Transparent).

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |
