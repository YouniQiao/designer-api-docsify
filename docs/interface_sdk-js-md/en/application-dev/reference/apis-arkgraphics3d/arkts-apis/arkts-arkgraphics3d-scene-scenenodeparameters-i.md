# SceneNodeParameters

Describes the scene node parameters, which are used to provide the name and path in the scene node tree.

**Since:** 23

<!--Device-unnamed-export interface SceneNodeParameters--><!--Device-unnamed-export interface SceneNodeParameters-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## name

```TypeScript
name: string
```

Name of the scene node. It is customizable.

**Type:** string

**Since:** 23

<!--Device-SceneNodeParameters-name: string--><!--Device-SceneNodeParameters-name: string-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## path

```TypeScript
path?: string
```

Path in the scene node tree. It specifies the position of the created camera, light, or node in the scene node tree. Each layer is separated by a slash (/). If not provided, it is set as a child node of the root node. The default value is undefined.

**Type:** string

**Since:** 23

<!--Device-SceneNodeParameters-path?: string--><!--Device-SceneNodeParameters-path?: string-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

