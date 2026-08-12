# symlink

## symlink

```TypeScript
declare function symlink(target: string, srcPath: string): Promise<void>
```

Creates a symbolic link based on the file path. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [symlink](arkts-corefile-file-fs-symlink-f.md#symlink)

<!--Device-unnamed-declare function symlink(target: string, srcPath: string): Promise<void>--><!--Device-unnamed-declare function symlink(target: string, srcPath: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | string | Yes |
| srcPath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## symlink

```TypeScript
declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void
```

Creates a symbolic link based on the file path. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [symlink](arkts-corefile-file-fs-symlink-f.md#symlink)

<!--Device-unnamed-declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | string | Yes |
| srcPath | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
