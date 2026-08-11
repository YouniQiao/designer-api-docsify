# fdatasync

## fdatasync

```TypeScript
declare function fdatasync(fd: number): Promise<void>
```

Synchronizes the data of a file. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:fdatasync](arkts-corefile-fileio-fdatasync-f.md#fdatasync)

<!--Device-unnamed-declare function fdatasync(fd: number): Promise<void>--><!--Device-unnamed-declare function fdatasync(fd: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |


## fdatasync

```TypeScript
declare function fdatasync(fd: number, callback: AsyncCallback<void>): void
```

Synchronizes the data of a file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:fdatasync](arkts-corefile-fileio-fdatasync-f.md#fdatasync)

<!--Device-unnamed-declare function fdatasync(fd: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function fdatasync(fd: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
