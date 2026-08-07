# RenderContext

Render context defines the context for all rendering resources. Resources within the same render context may be shared between scenes created within the same render context.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RenderContext--><!--Device-unnamed-export interface RenderContext-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## getRenderResourceFactory

```TypeScript
getRenderResourceFactory() : RenderResourceFactory
```

Get resource factory.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RenderContext-getRenderResourceFactory() : RenderResourceFactory--><!--Device-RenderContext-getRenderResourceFactory() : RenderResourceFactory-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  RenderResourceFactory instance |

## loadPlugin

```TypeScript
loadPlugin(name: string): Promise<boolean>
```

Loads a plugin by name. The API locates and loads the corresponding plugin resource using the provided plugin name.It uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RenderContext-loadPlugin(name: string): Promise<boolean>--><!--Device-RenderContext-loadPlugin(name: string): Promise<boolean>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the plugin to load, which must be a system predefined or registered and available plugin name, and follow the naming conventions. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; |  Promise used to return a Boolean value, indicating whether the plugin is loaded. The value true means that the plugin is loaded, and false means the opposite. |

## registerResourcePath

```TypeScript
registerResourcePath(protocol: string, uri: string): boolean
```

Registers the directory path and retrieval name for asset files, such as shaders.It allows the system to find and replace the path descriptions of related files within the shaders using the retrieval name.This ensures that the correct paths for assets and their associated files are located and loaded properly.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RenderContext-registerResourcePath(protocol: string, uri: string): boolean--><!--Device-RenderContext-registerResourcePath(protocol: string, uri: string): boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| protocol | string | Yes | Path retrieval name to be registered, used as the prefix identifier for file paths associated internally in the shader. Must be a non-empty retrieval name that is not predefined or registered by the system. |
| uri | string | Yes | Directory path of the assets to be registered, which corresponds to the retrieval name. When the shader is loaded, the retrieval name prefix in the path is replaced with this directory. It must be the path to the folder containing the asset files. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  Result indicating whether the registration is successful. true if successful, and false otherwise. The possible cause of a registration failure is that the retrieval name has been registered or an input parameter is invalid. |

