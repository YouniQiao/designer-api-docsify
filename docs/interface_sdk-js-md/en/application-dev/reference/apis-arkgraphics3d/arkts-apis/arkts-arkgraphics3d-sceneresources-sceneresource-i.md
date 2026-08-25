# SceneResource

Describes a resource in a scene.@interface SceneResource

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## destroy

```TypeScript
destroy(): void
```

Destroys the scene resource and releases all associated resources or references. Once released, the resource can no longer be used or accessed.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## name

```TypeScript
name: string
```

Name. There is no special format requirement.

**Type:** string

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## resourceType

```TypeScript
readonly resourceType: SceneResourceType
```

Scene resource type. The default value is undefined.

**Type:** [SceneResourceType](arkts-arkgraphics3d-sceneresources-sceneresourcetype-e.md)

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## uri

```TypeScript
readonly uri?: ResourceStr
```

Resource to load. The default value is undefined.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D
