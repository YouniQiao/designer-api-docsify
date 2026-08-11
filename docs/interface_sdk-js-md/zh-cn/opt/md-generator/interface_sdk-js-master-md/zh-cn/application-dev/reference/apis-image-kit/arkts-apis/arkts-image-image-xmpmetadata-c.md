# XMPMetadata

XMPMetadata instance.

**起始版本：** 26.0.0

<!--Device-image-class XMPMetadata--><!--Device-image-class XMPMetadata-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## enumerateTags

```TypeScript
public enumerateTags(
      callback: (path: string, tag: XMPTag) => boolean,
      rootPath?: string,
      options?: XMPEnumerateOptions
    ): void
```

Enumerate the XMP tags from specified path and uses a callback to return the result.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XMPMetadata-public enumerateTags(      callback: (path: string, tag: XMPTag) => boolean,      rootPath?: string,      options?: XMPEnumerateOptions    ): void--><!--Device-XMPMetadata-public enumerateTags(      callback: (path: string, tag: XMPTag) => boolean,      rootPath?: string,      options?: XMPEnumerateOptions    ): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (path: string, tag: XMPTag) =&gt; boolean | 是 |
| rootPath | string | 否 |
| options | [XMPEnumerateOptions](arkts-image-image-xmpenumerateoptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## getBlob

```TypeScript
public getBlob(): Promise<ArrayBuffer>
```

Obtains the XMP metadata as a blob.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XMPMetadata-public getBlob(): Promise<ArrayBuffer>--><!--Device-XMPMetadata-public getBlob(): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;ArrayBuffer&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

## getTag

```TypeScript
public getTag(path: string): Promise<XMPTag | null>
```

Get a single XMP tag from specified path.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XMPMetadata-public getTag(path: string): Promise<XMPTag | null>--><!--Device-XMPMetadata-public getTag(path: string): Promise<XMPTag | null>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;XMPTag \| null&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## getTags

```TypeScript
public getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>
```

Get all XMP tags from specified path.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XMPMetadata-public getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>--><!--Device-XMPMetadata-public getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rootPath | string | 否 |
| options | [XMPEnumerateOptions](arkts-image-image-xmpenumerateoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Record&lt;string, XMPTag&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## registerXMPNamespace

```TypeScript
public registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>
```

Register a new namespace according to the xml namespace and prefix.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XMPMetadata-public registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>--><!--Device-XMPMetadata-public registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| xmpNamespace | [XMPNamespace](arkts-image-image-xmpnamespace-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## removeTag

```TypeScript
public removeTag(path: string): Promise<void>
```

Remove the XMP tag from specified path.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XMPMetadata-public removeTag(path: string): Promise<void>--><!--Device-XMPMetadata-public removeTag(path: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## setBlob

```TypeScript
public setBlob(buffer: ArrayBuffer): Promise<void>
```

Set a blob into the XMP metadata.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XMPMetadata-public setBlob(buffer: ArrayBuffer): Promise<void>--><!--Device-XMPMetadata-public setBlob(buffer: ArrayBuffer): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## setValue

```TypeScript
public setValue(path: string, type: XMPTagType, value?: string): Promise<void>
```

Set the XMP type and value of the XMP tag in the specified path.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-XMPMetadata-public setValue(path: string, type: XMPTagType, value?: string): Promise<void>--><!--Device-XMPMetadata-public setValue(path: string, type: XMPTagType, value?: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| type | [XMPTagType](arkts-image-image-xmptagtype-e.md) | 是 |
| value | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../errorcode-image.md#7600206-无效参数) |
