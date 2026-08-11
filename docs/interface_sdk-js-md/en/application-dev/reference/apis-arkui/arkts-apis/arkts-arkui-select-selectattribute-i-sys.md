# SelectAttribute

Defines the Select component attributes.

**Inheritance/Implementation:** SelectAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SelectAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SelectAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## menuDistortionMode

```TypeScript
default menuDistortionMode(mode: DistortionMode | undefined): this
```

Sets the distortion animation mode of the select with the new material.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuDistortionMode(mode: DistortionMode | undefined): this--><!--Device-SelectAttribute-default menuDistortionMode(mode: DistortionMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [DistortionMode](../arkts-components/arkts-arkui-distortionmode-e-sys.md) \| undefined | Yes | Animation mode. The default value is DistortionMode.DISTORTION_AUTO. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

## menuEdgeLightMode

```TypeScript
default menuEdgeLightMode(mode: EdgeLightMode | undefined): this
```

Sets the edgelight animation mode of the select with the new material.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectAttribute-default menuEdgeLightMode(mode: EdgeLightMode | undefined): this--><!--Device-SelectAttribute-default menuEdgeLightMode(mode: EdgeLightMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [EdgeLightMode](../arkts-components/arkts-arkui-edgelightmode-e-sys.md) \| undefined | Yes | Animation mode. The default value is EdgeLightMode.EDGELIGHT_DISABLED. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the select. |

