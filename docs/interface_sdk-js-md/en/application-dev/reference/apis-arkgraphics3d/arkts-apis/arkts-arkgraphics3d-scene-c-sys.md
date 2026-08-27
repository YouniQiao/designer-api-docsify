# Scene

Describes a scene.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## load

```TypeScript
static load(uri: ResourceStr, param: SceneLoadParams):Promise<Scene>
```

Create a new scene from a SceneLoadParams.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | ResourceStr | Yes | the resource of creating a scene |
| param | [SceneLoadParams](arkts-arkgraphics3d-scene-sceneloadparams-i-sys.md) | Yes | the params for scene load |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Scene](arkts-arkgraphics3d-scene-c.md)&gt; | Promise used to return a scene |

**Examples**

Example 1: Load resources via rawfile (a relative path).

```TypeScript
import { Scene } from '@kit.ArkGraphics3D';

function loadModel(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then((result: Scene) => {
    console.info("Scene loaded, root node: " + result.root?.name);
  });
}
```

Example 2: Load via an absolute path (from /data/storage/el2/base/files in the application sandbox directory).

```TypeScript
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { Scene } from '@kit.ArkGraphics3D';

async function loadModelFromAbsolutePath(context: common.UIAbilityContext): Promise<void> {
  // Obtain the application sandbox directory. (Scene.load can read only files written by the application itself, not files written by hdc/adb push.)
  const appCtx = context.getApplicationContext();
  const filesDir = appCtx.filesDir; // /data/storage/el2/base/files

  // Read the model content from rawfile. (In practice, you can replace rawfile with data from other sources.)
  // Use a .glb file for easier copying and loading. If the file is in.gltf format, copy its .bin file and texture files to the same directory.
  const src = 'gltf/CubeWithFloor/glTF/AnimatedCube.glb';
  const load_uri = `${filesDir}/AnimatedCube.glb`;

  // Write the model file to the application sandbox directory to create a file accessible by Scene.load (absolute path).
  const rawData = await context.resourceManager.getRawFileContent(src);
  const file = fileIo.openSync(load_uri, fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.WRITE_ONLY);
  fileIo.writeSync(file.fd, rawData.buffer.slice(rawData.byteOffset, rawData.byteOffset + rawData.byteLength));
  fileIo.closeSync(file);

  // Load the model using the absolute path.
  Scene.load(load_uri).then((scene: Scene) => {
    // Handle the loaded scene.
  }).catch((err: Error) => {
    console.error(`Failed to load scene. Message: ${err.message}`);
  });
}
```
