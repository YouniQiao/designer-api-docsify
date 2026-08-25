# ImageFrameNode

定义Image类型的FrameNode。

**继承/实现关系：** ImageFrameNode extends TypedFrameNode<ImageAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute
```

初始化Image类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | image.PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) |

## initialize

```TypeScript
abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute
```

初始化Image类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | image.PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) |

## initialize

```TypeScript
abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor, value: ImageAIOptions): ImageAttribute
```

初始化Image类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | image.PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | 是 |
| value | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) |
