# DistortionComponent

Defines DistortionComponent.

## DistortionComponent

```TypeScript
DistortionComponent(options?: DistortionComponentOptions)
```

Creates a DistortionComponent with content.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistortionComponentInterface-(options?: DistortionComponentOptions): DistortionComponentAttribute--><!--Device-DistortionComponentInterface-(options?: DistortionComponentOptions): DistortionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DistortionComponentOptions](arkts-arkui-distortioncomponentoptions-i-sys.md) | No | DistortionComponent Options. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [DistortionComponentOptions](arkts-arkui-distortioncomponentoptions-i-sys.md) | Defines the DistortionComponent constructor options. |
| [DistortionParam](arkts-arkui-distortionparam-i-sys.md) | Defines the spatial distortion parameters. > **NOTE：**> > - The coordinates of the four corners of the component can be set as follows: top-left corner: { x:0, y:0 }, top-right > corner: { x:1, y:0 }, bottom-left corner: { x:0, y:1 }, bottom-right corner: { x:1, y:1 }. > > - For example, if the **bottomLeft** attribute is set to **{ x:0.5, y:0.5 }**, the bottom-left corner is deformed to the > position of the component center, and the corresponding distortion effect is generated. > > - When setting the coordinates of the four corners, ensure they follow spatial logic. For example, if **topLeft** > is **{ x:0, y:0.7 }** and **bottomLeft** is **{ x:0, y:0.2 }**, the top-left corner is lower than the bottom-left corner, which > violates the spatial logic and may cause rendering exceptions. |

### Types

| Name | Description |
| --- | --- |
| [Vector2](arkts-arkui-vector2-t-sys.md) | Defines the two-dimensional vector, which contains the x and y coordinates and indicates the position relationship. |
| [Vector4](arkts-arkui-vector4-t-sys.md) | Defines the four-dimensional vector, which contains x, y, z, and w coordinates that indicate the barrel distortion degree. |

