# TextFrameNode

定义Text类型的FrameNode。

**继承/实现关系：** TextFrameNode extends TypedFrameNode<TextAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(content?: string | Resource, value?: TextOptions): TextAttribute
```

初始化Text类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 否 |
| value | [TextOptions](../arkts-components/arkts-arkui-textoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](../arkts-components/arkts-arkui-text-attribute.md) |
