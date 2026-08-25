# RenderContext

Defines the context of all rendering resources. Multiple scenes created within the same render context can share rendering resources.@interface RenderContext

**Since:** 20

**System capability:** SystemCapability.ArkUi.Graphics3D

## getRenderResourceFactory

```TypeScript
getRenderResourceFactory() : RenderResourceFactory
```

Obtains the rendering resource factory, which provides APIs for creating different rendering resources.

**Since:** 20

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderResourceFactory](arkts-arkgraphics3d-scene-renderresourcefactory-i.md) |

## loadPlugin

```TypeScript
loadPlugin(name: string): Promise<boolean>
```

Loads a plugin by name. The API locates and loads the corresponding plugin resource using the provided plugin name. It uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## registerResourcePath

```TypeScript
registerResourcePath(protocol: string, uri: string): boolean
```

Registers the directory path and retrieval name for asset files, such as shaders. It allows the system to find and replace the path descriptions of related files within the shaders using the retrieval name. This ensures that the correct paths for assets and their associated files are located and loaded properly.

**Since:** 20

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| protocol | string | Yes |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
