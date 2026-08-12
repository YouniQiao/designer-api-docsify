# ContainerReaderAttribute

除支持[通用属性](common)外，还支持以下属性：

**继承/实现关系：** ContainerReaderAttribute extends [CommonMethod<ContainerReaderAttribute>](CommonMethod<ContainerReaderAttribute>)

**起始版本：** 26.0.0

<!--Device-unnamed-export declare class ContainerReaderAttribute extends CommonMethod<ContainerReaderAttribute>--><!--Device-unnamed-export declare class ContainerReaderAttribute extends CommonMethod<ContainerReaderAttribute>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## breakpointConfig

```TypeScript
breakpointConfig(value?: BreakpointOptions): ContainerReaderAttribute
```

设置断点配置选项，定义触发不同布局行为的尺寸阈值。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-ContainerReaderAttribute-breakpointConfig(value?: BreakpointOptions): ContainerReaderAttribute--><!--Device-ContainerReaderAttribute-breakpointConfig(value?: BreakpointOptions): ContainerReaderAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BreakpointOptions](arkts-arkui-arkui-components-containerreader-breakpointoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md) |
