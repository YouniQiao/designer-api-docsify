# ToggleAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** ToggleAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of toggle.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this
```

定制Toggle内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[ToggleConfiguration](arkts-arkui-toggle-toggleconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: ((isOn: boolean) => void) | undefined): this
```

开关状态切换时触发该事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((isOn: boolean) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md) |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

设置组件在打开状态下的背景颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md) |

## switchPointColor

```TypeScript
default switchPointColor(color: ResourceColor | undefined): this
```

设置Switch类型的圆形滑块颜色。仅当type为ToggleType.Switch生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md) |

## switchStyle

```TypeScript
default switchStyle(value: SwitchStyle | undefined): this
```

设置Switch类型的样式。仅当type为ToggleType.Switch生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SwitchStyle](arkts-arkui-toggle-switchstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md) |
