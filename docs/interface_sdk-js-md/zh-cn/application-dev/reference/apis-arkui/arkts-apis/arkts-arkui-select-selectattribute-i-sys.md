# SelectAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** SelectAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## menuDistortionMode

```TypeScript
default menuDistortionMode(mode: DistortionMode | undefined): this
```

Sets the distortion animation mode of the select with the new material.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [DistortionMode](../arkts-components/arkts-arkui-distortionmode-e-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## menuEdgeLightMode

```TypeScript
default menuEdgeLightMode(mode: EdgeLightMode | undefined): this
```

Sets the edgelight animation mode of the select with the new material.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [EdgeLightMode](../arkts-components/arkts-arkui-edgelightmode-e-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## menuSystemMaterial

```TypeScript
default menuSystemMaterial(material: SystemUiMaterial | undefined): this
```

Set system-styled materials for select's menu. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of select's menu.Device Behavior Differences:The effect of the same material may vary across different devices depending on their computing power.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| material | [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |
