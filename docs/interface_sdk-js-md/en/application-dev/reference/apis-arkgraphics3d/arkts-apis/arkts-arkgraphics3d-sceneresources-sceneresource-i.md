# SceneResource

定义被其他3D资源扩展的场景资源.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface SceneResource--><!--Device-unnamed-export interface SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## destroy

```TypeScript
destroy(): void
```

销毁场景资源，释放所有关联的资源或引用，一旦被释放，资源就不能被再次使用或访问。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SceneResource-destroy(): void--><!--Device-SceneResource-destroy(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## name

```TypeScript
name: string
```

场景资源名称，没有特殊格式要求。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SceneResource-name: string--><!--Device-SceneResource-name: string-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## resourceType

```TypeScript
readonly resourceType: SceneResourceType
```

场景资源类型，默认值为undefined。

**Type:** [SceneResourceType](arkts-arkgraphics3d-sceneresources-sceneresourcetype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SceneResource-readonly resourceType: SceneResourceType--><!--Device-SceneResource-readonly resourceType: SceneResourceType-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## uri

```TypeScript
readonly uri?: ResourceStr
```

需要加载的场景资源URI，默认值为undefined。

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SceneResource-readonly uri?: ResourceStr--><!--Device-SceneResource-readonly uri?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

