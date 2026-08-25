# Scene

Describes a scene.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## load

```TypeScript
static load(uri: ResourceStr, param: SceneLoadParams):Promise<Scene>
```

Create a new scene from a SceneLoadParams.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |
| param | [SceneLoadParams](arkts-arkgraphics3d-scene-sceneloadparams-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Scene](arkts-arkgraphics3d-scene-c.md)&gt; |

**Examples**

Example 1: Load resources via rawfile (a relative path).

```TypeScript
import { Scene } from '@kit.ArkGraphics3D';

function loadModel(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {});
}
```

Example 2: Load via an absolute path (from /data/storage/el2/base/files in the application sandbox directory).

```TypeScript
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { Scene } from '@kit.ArkGraphics3D';

async loadModelFromAbsolutePath(): Promise<void> {
  // Obtain the application sandbox directory. (Scene.load can read only files written by the application itself, not files written by hdc/adb push.)
  const uiCtx = this.getUIContext().getHostContext() as common.UIAbilityContext;
  const appCtx = uiCtx.getApplicationContext();
  const filesDir = appCtx.filesDir; // /data/storage/el2/base/files

  // Read the model content from rawfile. (In practice, you can replace rawfile with data from other sources.)
  // Use a .glb file for easier copying and loading. If the file is in.gltf format, copy its .bin file and texture files to the same directory.
  const src = 'gltf/CubeWithFloor/glTF/AnimatedCube.glb';
  const load_uri = `${filesDir}/AnimatedCube.glb`;

  // Write the model file to the application sandbox directory to create a file accessible by Scene.load (absolute path).
  const rawData = await uiCtx.resourceManager.getRawFileContent(src);
  const file = fileIo.openSync(load_uri, fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.WRITE_ONLY);
  fileIo.writeSync(file.fd, rawData.buffer.slice(rawData.byteOffset, rawData.byteOffset + rawData.byteLength));
  fileIo.closeSync(file);

  // Load the model using the absolute path.
  Scene.load(load_uri).then((scene: Scene) => {
    // Handle the loaded scene.
  }).catch((error: string) => {
    console.error('Scene load failed: ' + error);
  });
}
```
