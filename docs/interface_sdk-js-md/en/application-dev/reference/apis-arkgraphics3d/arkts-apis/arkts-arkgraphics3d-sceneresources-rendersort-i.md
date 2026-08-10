# RenderSort

渲染排序层。在渲染槽中，层可以定义排序层顺序。可用值为0-63（0最先，63最后）。默认id值为32。典型用法：1. 将渲染排序层设置为对使用深度测试但未写入深度的对象进行渲染。2. 始终首先渲染角色和/或相机对象以剔除大部分视图。3. 对平面层进行排序。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RenderSort--><!--Device-unnamed-export interface RenderSort-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderSortLayer

```TypeScript
renderSortLayer?: int
```

用于在渲染槽中对子网格进行排序的排序层.有效值为0-63.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 32 默认渲染排序层id。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RenderSort-renderSortLayer?: int--><!--Device-RenderSort-renderSortLayer?: int-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderSortLayerOrder

```TypeScript
renderSortLayerOrder?: int
```

排序层内描述精细顺序的排序层顺序.有效值为0-255.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 0 默认渲染排序层顺序。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RenderSort-renderSortLayerOrder?: int--><!--Device-RenderSort-renderSortLayerOrder?: int-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

