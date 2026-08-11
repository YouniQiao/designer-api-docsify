# rmdir

## rmdir

```TypeScript
declare function rmdir(path: string): Promise<void>
```

Removes a directory. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:rmdir](arkts-corefile-fileio-rmdir-f.md#rmdir)

<!--Device-unnamed-declare function rmdir(path: string): Promise<void>--><!--Device-unnamed-declare function rmdir(path: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |


## rmdir

```TypeScript
declare function rmdir(path: string, callback: AsyncCallback<void>): void
```

Removes a directory. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:rmdir](arkts-corefile-fileio-rmdir-f.md#rmdir)

<!--Device-unnamed-declare function rmdir(path: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function rmdir(path: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
