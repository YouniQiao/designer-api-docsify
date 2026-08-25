# TextInputAttribute

除支持通用属性，还支持以下属性：

> **说明：**&gt;
> 默认情况下，通用属性padding的默认值为：
{&nbsp;top: '8vp',&nbsp;right: '16vp',&nbsp;bottom: '8vp',&nbsp;left: '16vp'}

> 输入框开启下划线模式时，通用属性padding的默认值为：
{&nbsp;top: '12vp',&nbsp;right: '0vp',&nbsp;bottom: '12vp',&nbsp;left: '0vp'}

> 当输入框设置padding为0时，可设置
> borderRadius为0避免光标被截断。当光标
> 在文本框边缘显示异常时，请检查是否是padding、borderRadius属性影响造成。&gt;
> 从API version 10开始，单行输入框可设置.width('auto')使组件宽度自适应文本宽度，自适应时组件宽度受constraintSize属性以及父容器传递的最大最小宽度限制，其余使用方式参考
> [尺寸设置](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md)。

**继承/实现关系：** TextInputAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## voiceButton

```TypeScript
default voiceButton(options: VoiceButtonOptions | undefined): this
```

设置语音按键选项。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [VoiceButtonOptions](arkts-arkui-textcommon-voicebuttonoptions-i-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |
