# Blender (System API)

```TypeScript
type Blender = BrightnessBlender | HdrBrightnessBlender | HdrDarkenBlender
```

混合器类型，用于描述混合效果。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiEffect-type Blender = BrightnessBlender | HdrBrightnessBlender | HdrDarkenBlender--><!--Device-uiEffect-type Blender = BrightnessBlender | HdrBrightnessBlender | HdrDarkenBlender-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

| Type | Description |
| --- | --- |
| BrightnessBlender | 提亮混合器 |
| HdrBrightnessBlender | 支持HDR的提亮混合器 [since 20] |
| HdrDarkenBlender | 支持HDR的压暗混合器 [since 26.0.0] |

