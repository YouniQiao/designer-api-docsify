# init

## Modules to Import

```TypeScript
```

## init

```TypeScript
function init(options: [
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double,
        double
    ]): Matrix4Transit
```

Constructor of Matrix, which can create a fourth-order matrix based on the input parameters. The matrix is column-first.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-matrix4-function init(options: [        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double    ]): Matrix4Transit--><!--Device-matrix4-function init(options: [        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double,        double    ]): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double,         double     ] | Yes | options indicates a fourth-order matrix The default value： [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1] Fourth-order matrix notes: m00 { double } -The x-axis scale value, the identity matrix defaults to 1. m01 { double } -The second value, the rotation and skew of the xyz axis affects this value. m02 { double } -The third value, the rotation of the xyz axis affects this value. m03 { double } -The fourth value, the perspective projection affects this value. m10 { double } -The fifth value, the rotation and skew of the xyz axis affects this value. m11 { double } -The y-axis scales the value, and the identity matrix defaults to 1. m12 { double } -The 7th value, the rotation of the xyz axis affects this value. m13 { double } -The 8th value, the perspective projection affects this value. m20 { double } -The 9th value, the rotation of the xyz axis affects this value. m21 { double } -The 10th value, xyz axis rotation affects this value. m22 { double } -The z-axis scale value, the identity matrix defaults to 1. m23 { double } -The 12th value, the perspective projection affects this value. m30 { double } -The x-axis translation value in px, the identity matrix defaults to 0. m31 { double } -Y-axis translation value, in px, the identity matrix defaults to 0. m32 { double } -The z-axis translation value in px, the identity matrix defaults to 0. m33 { double } -It takes effect in homogeneous coordinates to produce a perspective projection effect. |

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Return to Matrix4Transit |

