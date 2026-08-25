# XComponentFrameNode

定义XComponent 类型的FrameNode。

**继承/实现关系：** XComponentFrameNode extends TypedFrameNode<XComponentAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(value: XComponentParameters): XComponentAttribute
```

初始化XComponent类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [XComponentParameters](arkts-arkui-xcomponent-xcomponentparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md) |

## initialize

```TypeScript
abstract initialize(value: XComponentOptions): XComponentAttribute
```

初始化XComponent类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [XComponentOptions](../arkts-components/arkts-arkui-xcomponentoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md) |

## initialize

```TypeScript
abstract initialize(params: NativeXComponentParameters): XComponentAttribute
```

初始化XComponent类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [NativeXComponentParameters](arkts-arkui-xcomponent-nativexcomponentparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md) |
