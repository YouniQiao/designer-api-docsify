# Text

Text组件用于显示文本内容，支持设置字体样式、文本对齐、行高、装饰线等属性，支持图文混排、文本选择、文本识别等功能，适用于需要展示文本信息的各类应用场景。

## 子组件 可以包含Span、ImageSpan、SymbolSpan和 ContainerSpan子组件。 > **说明：** > > 使用[子组件](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#子组件)实现 > [图文混排](../../../ui/arkts-text-image-layout.md)场景。

## Text

```TypeScript
Text(content?: string | Resource, value?: TextOptions)
```

定义文本组件构造函数。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-TextInterface-(content?: string | Resource, value?: TextOptions): TextAttribute--><!--Device-TextInterface-(content?: string | Resource, value?: TextOptions): TextAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 否 |
| value | [TextOptions](arkts-arkui-textoptions-i.md) | 否 |

## 汇总

- [TextMarqueeOptions](arkts-arkui-textmarqueeoptions-i.md)
- [TextOptions](arkts-arkui-textoptions-i.md)
- [TextOverflowOptions](arkts-arkui-textoverflowoptions-i.md)
- [MarqueeStartPolicy](arkts-arkui-marqueestartpolicy-e.md)
- [MarqueeState](arkts-arkui-marqueestate-e.md)
- [MarqueeUpdatePolicy](arkts-arkui-marqueeupdatepolicy-e.md)
- [TextResponseType](arkts-arkui-textresponsetype-e.md)
- [TextSpanType](arkts-arkui-textspantype-e.md)
