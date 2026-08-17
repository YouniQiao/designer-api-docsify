# Blender (System API)

```TypeScript
type Blender = BrightnessBlender | HdrBrightnessBlender | HdrDarkenBlender
```

Blender type, used to describe the blending effect.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiEffect-type Blender = BrightnessBlender | HdrBrightnessBlender | HdrDarkenBlender--><!--Device-uiEffect-type Blender = BrightnessBlender | HdrBrightnessBlender | HdrDarkenBlender-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

| Type | Description |
| --- | --- |
| BrightnessBlender | Brightness blender |
| HdrBrightnessBlender | HDR-enabled brightness blender [since 20] |
| HdrDarkenBlender | HDR-adaptive darken blender [since 26.0.0] |

