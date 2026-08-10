# SceneLoadParams (System API)

加载场景的参数

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface SceneLoadParams--><!--Device-unnamed-export interface SceneLoadParams-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## offset

```TypeScript
offset?: long
```

3D模型数据在资源文件中的起始偏移量，单位为字节。系统将从资源文件的该偏移位置定位并读取glb模型数据。例如，当glb模型嵌在MP4容器文件中时，可将此参数设置为glb数据在MP4文件中的起始字节位置，使系统能够正确提取并加载模型。取值必须大于或等于0。默认值为0，表示模型数据从文件起始位置开始。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Default:** { 0 }

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SceneLoadParams-offset?: long--><!--Device-SceneLoadParams-offset?: long-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

