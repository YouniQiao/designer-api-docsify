# SceneResourceFactory

The scene resource factory.

**Inheritance/Implementation:** SceneResourceFactory extends [RenderResourceFactory](arkts-arkgraphics3d-scene-renderresourcefactory-i.md#RenderResourceFactory)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface SceneResourceFactory--><!--Device-unnamed-export interface SceneResourceFactory-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## createCamera

```TypeScript
createCamera(params: SceneNodeParameters): Promise<Camera>
```

Create a camera.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SceneResourceFactory-createCamera(params: SceneNodeParameters): Promise<Camera>--><!--Device-SceneResourceFactory-createCamera(params: SceneNodeParameters): Promise<Camera>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](arkts-arkgraphics3d-scene-scenenodeparameters-i.md) | Yes | the param of creating a camera |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Camera](arkts-arkgraphics3d-scenenodes-camera-i.md)&gt; | promise a camera |

## Examples

```TypeScript
import { SceneNodeParameters, Camera, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function createCameraPromise(): Promise<Camera> {
  return new Promise((resolve, reject) => {
    // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let sceneCameraParameter: SceneNodeParameters = { name: "camera1" };
      // Create a camera.
      let camera: Camera = await sceneFactory.createCamera(sceneCameraParameter);
      resolve(camera);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

## createCamera

```TypeScript
createCamera(params: SceneNodeParameters, cameraParams: CameraParameters): Promise<Camera>
```

Create a camera.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SceneResourceFactory-createCamera(params: SceneNodeParameters, cameraParams: CameraParameters): Promise<Camera>--><!--Device-SceneResourceFactory-createCamera(params: SceneNodeParameters, cameraParams: CameraParameters): Promise<Camera>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](arkts-arkgraphics3d-scene-scenenodeparameters-i.md) | Yes | the param of creating a camera |
| cameraParams | [CameraParameters](arkts-arkgraphics3d-scene-cameraparameters-i.md) | Yes | camera specific extra parameters |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Camera](arkts-arkgraphics3d-scenenodes-camera-i.md)&gt; | promise a camera |

## Examples

```TypeScript
import { SceneNodeParameters, Camera, SceneResourceFactory, Scene, CameraParameters,
  RenderingPipelineType } from '@kit.ArkGraphics3D';

function createCameraPromise(): Promise<Camera> {
  return new Promise((resolve, reject) => {
    // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let nodeParameter: SceneNodeParameters = { name: "camera1" };
      let camParameter: CameraParameters = {renderingPipeline: RenderingPipelineType.FORWARD};
      // Create a camera.
      let camera: Camera = await sceneFactory.createCamera(nodeParameter, camParameter);
      resolve(camera);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

## createEffect

```TypeScript
createEffect(params: EffectParameters): Promise<Effect>
```

Create an effect.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SceneResourceFactory-createEffect(params: EffectParameters): Promise<Effect>--><!--Device-SceneResourceFactory-createEffect(params: EffectParameters): Promise<Effect>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [EffectParameters](arkts-arkgraphics3d-scene-effectparameters-i.md) | Yes | the params of creating an effect. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Effect](arkts-arkgraphics3d-sceneresources-effect-i.md)&gt; | promise an effect. |

## Examples

```TypeScript
import { SceneResourceFactory, Scene, Effect, EffectParameters } from '@kit.ArkGraphics3D';

function createEffect() : Promise<Effect> {
  return new Promise((resolve, reject) => {
    let scene: Promise<Scene> = Scene.load();
    scene.then(async (result: Scene | undefined) => {
      if (!result) {
        return;
      }
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      // Effect ID, which is in the format of 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', for example, 'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'.
      let params: EffectParameters = {effectId: "e68a7f45-2d21-4a0d-9aef-7d9c825d3f12"}
      let effect: Effect = await sceneFactory.createEffect(params);
      resolve(effect);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

## createEnvironment

```TypeScript
createEnvironment(params: SceneResourceParameters): Promise<Environment>
```

Create an environment.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SceneResourceFactory-createEnvironment(params: SceneResourceParameters): Promise<Environment>--><!--Device-SceneResourceFactory-createEnvironment(params: SceneResourceParameters): Promise<Environment>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [SceneResourceParameters](arkts-arkgraphics3d-scene-sceneresourceparameters-i.md) | Yes | the param of creating an environment object |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Environment](arkts-arkgraphics3d-sceneresources-environment-i.md)&gt; | promise an environment |

## Examples

```TypeScript
import { Environment, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function createEnvironmentPromise(): Promise<Environment> {
  return new Promise((resolve, reject) => {
    // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      // Load environment map resources. The path and file name can be customized based on the specific project resources.
      let sceneEnvironmentParameter: SceneResourceParameters = { name: "env", uri: $rawfile("KTX/quarry_02_2k_radiance.ktx") };
      // Create an environment.
      let env: Environment = await sceneFactory.createEnvironment(sceneEnvironmentParameter);
      resolve(env);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

## createGeometry

```TypeScript
createGeometry(params: SceneNodeParameters, mesh:MeshResource): Promise<Geometry>
```

Create a geometry node.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SceneResourceFactory-createGeometry(params: SceneNodeParameters, mesh:MeshResource): Promise<Geometry>--><!--Device-SceneResourceFactory-createGeometry(params: SceneNodeParameters, mesh:MeshResource): Promise<Geometry>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](arkts-arkgraphics3d-scene-scenenodeparameters-i.md) | Yes | the param of creating a geometry |
| mesh | [MeshResource](arkts-arkgraphics3d-sceneresources-meshresource-i.md) | Yes | resource - The mesh data for the geometry |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Geometry](arkts-arkgraphics3d-scenenodes-geometry-i.md)&gt; | promise a geometry |

## Examples

```TypeScript
import { SceneResourceFactory, Scene, Geometry, CubeGeometry } from '@kit.ArkGraphics3D';

function createGeometryPromise() : Promise<Geometry> {
  return new Promise((resolve, reject) => {
    let scene: Promise<Scene> = Scene.load();
    scene.then(async (result: Scene | undefined) => {
      if (!result) {
        return;
      }
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let cubeGeom = new CubeGeometry();
      cubeGeom.size = { x: 1, y: 1, z: 1 };
      let meshRes = await sceneFactory.createMesh({ name: "MeshName" }, cubeGeom);
      console.info("TEST createGeometryPromise");
      let geometry: Geometry = await sceneFactory.createGeometry({ name: "GeometryName" }, meshRes);
      resolve(geometry);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

## createLight

```TypeScript
createLight(params: SceneNodeParameters, lightType: LightType): Promise<Light>
```

Create a light.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SceneResourceFactory-createLight(params: SceneNodeParameters, lightType: LightType): Promise<Light>--><!--Device-SceneResourceFactory-createLight(params: SceneNodeParameters, lightType: LightType): Promise<Light>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](arkts-arkgraphics3d-scene-scenenodeparameters-i.md) | Yes | the param of creating a light |
| lightType | [LightType](arkts-arkgraphics3d-scenenodes-lighttype-e.md) | Yes | the type of the light |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Light](arkts-arkgraphics3d-scenenodes-light-i.md)&gt; | promise a light |

## Examples

```TypeScript
import { SceneNodeParameters, LightType, Light, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function createLightPromise() : Promise<Light> {
  return new Promise((resolve, reject) => {
    // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let sceneLightParameter: SceneNodeParameters = { name: "light" };
      // Create directional light.
      let light: Light = await sceneFactory.createLight(sceneLightParameter, LightType.DIRECTIONAL);
      resolve(light);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

## createMaterial

```TypeScript
createMaterial(params: SceneResourceParameters, materialType: MaterialType): Promise<Material>
```

Create a material.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SceneResourceFactory-createMaterial(params: SceneResourceParameters, materialType: MaterialType): Promise<Material>--><!--Device-SceneResourceFactory-createMaterial(params: SceneResourceParameters, materialType: MaterialType): Promise<Material>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [SceneResourceParameters](arkts-arkgraphics3d-scene-sceneresourceparameters-i.md) | Yes | the param of creating a material |
| materialType | [MaterialType](arkts-arkgraphics3d-sceneresources-materialtype-e.md) | Yes | the type of the material |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Material](arkts-arkgraphics3d-sceneresources-material-i.md)&gt; | promise a material |

## Examples

```TypeScript
import { MaterialType, Material, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function createMaterialPromise() : Promise<Material> {
  return new Promise((resolve, reject) => {
    // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let sceneMaterialParameter: SceneResourceParameters = { name: "material" };
      // Create a material.
      let material: Material = await sceneFactory.createMaterial(sceneMaterialParameter, MaterialType.SHADER);
      resolve(material);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

## createNode

```TypeScript
createNode(params: SceneNodeParameters): Promise<Node>
```

Create a node.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SceneResourceFactory-createNode(params: SceneNodeParameters): Promise<Node>--><!--Device-SceneResourceFactory-createNode(params: SceneNodeParameters): Promise<Node>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [SceneNodeParameters](arkts-arkgraphics3d-scene-scenenodeparameters-i.md) | Yes | the param of creating a node |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Node](arkts-arkgraphics3d-scenenodes-node-i.md)&gt; | promise a node |

## Examples

```TypeScript
import { SceneNodeParameters, SceneResourceFactory, Scene, Node } from '@kit.ArkGraphics3D';

function createNodePromise(): Promise<Node> {
  return new Promise((resolve, reject) => {
    // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let sceneNodeParameter: SceneNodeParameters = { name: "empty_node",
        path:"/rootNode_/empty_node" };
      // Create a node.
      let node: Node = await sceneFactory.createNode(sceneNodeParameter);
      resolve(node);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

