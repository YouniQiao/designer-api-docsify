# BadgeFrameNode

定义Badge类型的FrameNode。

**继承/实现关系：** BadgeFrameNode extends TypedFrameNode<BadgeAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(value: BadgeParamWithNumber): BadgeAttribute
```

初始化Badge类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BadgeParamWithNumber](arkts-arkui-badge-badgeparamwithnumber-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BadgeAttribute](../arkts-components/arkts-arkui-badge-attribute.md) |

## initialize

```TypeScript
abstract initialize(value: BadgeParamWithString): BadgeAttribute
```

初始化Badge类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BadgeParamWithString](../arkts-components/arkts-arkui-badgeparamwithstring-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BadgeAttribute](../arkts-components/arkts-arkui-badge-attribute.md) |
