# SelectAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

**继承/实现关系：** SelectAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface SelectAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SelectAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## menuDistortionMode

```TypeScript
default menuDistortionMode(mode: DistortionMode | undefined): this
```

Sets the distortion animation mode of the select with the new material.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuDistortionMode(mode: DistortionMode | undefined): this--><!--Device-SelectAttribute-default menuDistortionMode(mode: DistortionMode | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [DistortionMode](../arkts-components/arkts-arkui-distortionmode-e-sys.md) \| undefined | 是 | Animation mode. The default value is DistortionMode.DISTORTION_AUTO. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## menuEdgeLightMode

```TypeScript
default menuEdgeLightMode(mode: EdgeLightMode | undefined): this
```

Sets the edgelight animation mode of the select with the new material.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuEdgeLightMode(mode: EdgeLightMode | undefined): this--><!--Device-SelectAttribute-default menuEdgeLightMode(mode: EdgeLightMode | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [EdgeLightMode](../arkts-components/arkts-arkui-edgelightmode-e-sys.md) \| undefined | 是 | Animation mode. The default value is EdgeLightMode.EDGELIGHT_DISABLED. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

