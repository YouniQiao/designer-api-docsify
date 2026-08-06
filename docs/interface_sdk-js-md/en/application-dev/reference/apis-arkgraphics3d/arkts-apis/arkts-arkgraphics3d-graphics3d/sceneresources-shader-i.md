# Shader

Shader resource.

**Inheritance/Implementation:** Shader extends [SceneResource](sceneresources-sceneresource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Shader extends SceneResource--><!--Device-unnamed-export interface Shader extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## setShaderInputs

ArkTS-Dyn:
```TypeScript
setShaderInputs(inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>): void
```

ArkTS-Sta:
```TypeScript
setShaderInputs(inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>): void
```

Set shader inputs. Offers the same functionality for setting shader inputs as the property version,but with better performance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Shader-setShaderInputs(inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>): void--><!--Device-Shader-setShaderInputs(inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputs | ArkTS-Dyn: \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, number \| \_\_\_MD\_LINK\_USD\_1\_\_\_ \| \_\_\_MD\_LINK\_USD\_2\_\_\_ \| \_\_\_MD\_LINK\_USD\_3\_\_\_ \| \_\_\_MD\_LINK\_USD\_4\_\_\_&gt;  \_\_\_HTML\_TAG\_USD\_10\_\_\_ArkTS-Sta：\_\_\_MD\_LINK\_USD\_5\_\_\_&lt;string, double \| \_\_\_MD\_LINK\_USD\_6\_\_\_ \| \_\_\_MD\_LINK\_USD\_7\_\_\_ \| \_\_\_MD\_LINK\_USD\_8\_\_\_ \| \_\_\_MD\_LINK\_USD\_9\_\_\_&gt; | Yes | Inputs of the shader |

## inputs

```TypeScript
readonly inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>
```

Shader inputs.

**Type:** Record&lt;string, double \| Vec2 \| Vec3 \| Vec4 \| Image&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Shader-readonly inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>--><!--Device-Shader-readonly inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

