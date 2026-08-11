# XMPMetadata

XMPMetadata instance.

**Since:** 26.0.0

<!--Device-image-class XMPMetadata--><!--Device-image-class XMPMetadata-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## enumerateTags

```TypeScript
public enumerateTags(
      callback: (path: string, tag: XMPTag) => boolean,
      rootPath?: string,
      options?: XMPEnumerateOptions
    ): void
```

Enumerate the XMP tags from specified path and uses a callback to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPMetadata-public enumerateTags(      callback: (path: string, tag: XMPTag) => boolean,      rootPath?: string,      options?: XMPEnumerateOptions    ): void--><!--Device-XMPMetadata-public enumerateTags(      callback: (path: string, tag: XMPTag) => boolean,      rootPath?: string,      options?: XMPEnumerateOptions    ): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (path: string, tag: XMPTag) =&gt; boolean | Yes |
| rootPath | string | No |
| options | [XMPEnumerateOptions](arkts-image-image-xmpenumerateoptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |

## getBlob

```TypeScript
public getBlob(): Promise<ArrayBuffer>
```

Obtains the XMP metadata as a blob.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPMetadata-public getBlob(): Promise<ArrayBuffer>--><!--Device-XMPMetadata-public getBlob(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ArrayBuffer&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) |

## getTag

```TypeScript
public getTag(path: string): Promise<XMPTag | null>
```

Get a single XMP tag from specified path.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPMetadata-public getTag(path: string): Promise<XMPTag | null>--><!--Device-XMPMetadata-public getTag(path: string): Promise<XMPTag | null>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;XMPTag \| null&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |

## getTags

```TypeScript
public getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>
```

Get all XMP tags from specified path.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPMetadata-public getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>--><!--Device-XMPMetadata-public getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rootPath | string | No |
| options | [XMPEnumerateOptions](arkts-image-image-xmpenumerateoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Record&lt;string, XMPTag&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |

## registerXMPNamespace

```TypeScript
public registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>
```

Register a new namespace according to the xml namespace and prefix.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPMetadata-public registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>--><!--Device-XMPMetadata-public registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| xmpNamespace | [XMPNamespace](arkts-image-image-xmpnamespace-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |

## removeTag

```TypeScript
public removeTag(path: string): Promise<void>
```

Remove the XMP tag from specified path.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPMetadata-public removeTag(path: string): Promise<void>--><!--Device-XMPMetadata-public removeTag(path: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |

## setBlob

```TypeScript
public setBlob(buffer: ArrayBuffer): Promise<void>
```

Set a blob into the XMP metadata.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPMetadata-public setBlob(buffer: ArrayBuffer): Promise<void>--><!--Device-XMPMetadata-public setBlob(buffer: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |

## setValue

```TypeScript
public setValue(path: string, type: XMPTagType, value?: string): Promise<void>
```

Set the XMP type and value of the XMP tag in the specified path.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPMetadata-public setValue(path: string, type: XMPTagType, value?: string): Promise<void>--><!--Device-XMPMetadata-public setValue(path: string, type: XMPTagType, value?: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| type | [XMPTagType](arkts-image-image-xmptagtype-e.md) | Yes |
| value | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |
