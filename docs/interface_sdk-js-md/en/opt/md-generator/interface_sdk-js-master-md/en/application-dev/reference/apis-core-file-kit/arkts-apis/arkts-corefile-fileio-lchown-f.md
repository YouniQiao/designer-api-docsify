# lchown

## lchown

```TypeScript
declare function lchown(path: string, uid: number, gid: number): Promise<void>
```

Changes the file owner (owner of the symbolic link, not the file referred to by the symbolic link) based on the file path. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

<!--Device-unnamed-declare function lchown(path: string, uid: number, gid: number): Promise<void>--><!--Device-unnamed-declare function lchown(path: string, uid: number, gid: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| uid | number | Yes |
| gid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## lchown

```TypeScript
declare function lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void
```

Changes the file owner (owner of the symbolic link, not the file referred to by the symbolic link) based on a file path. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

<!--Device-unnamed-declare function lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| uid | number | Yes |
| gid | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
