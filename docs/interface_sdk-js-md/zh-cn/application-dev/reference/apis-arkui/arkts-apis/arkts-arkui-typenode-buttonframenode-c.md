# ButtonFrameNode

定义Button类型的FrameNode。

**继承/实现关系：** ButtonFrameNode extends TypedFrameNode<ButtonAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(): ButtonAttribute
```

初始化Button类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |

## initialize

```TypeScript
abstract initialize(value: ButtonOptions): ButtonAttribute
```

初始化Button类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ButtonOptions](arkts-arkui-button-buttonoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |

## initialize

```TypeScript
abstract initialize(label: ResourceStr, options?: ButtonOptions): ButtonAttribute
```

初始化Button类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| label | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 |
| options | [ButtonOptions](arkts-arkui-button-buttonoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |
