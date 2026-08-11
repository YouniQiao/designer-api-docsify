# ftruncate

## ftruncate

```TypeScript
declare function ftruncate(fd: number, len?: number): Promise<void>
```

Truncates a file based on the file descriptor. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:truncate](arkts-corefile-fileio-truncate-f.md#truncate)

<!--Device-unnamed-declare function ftruncate(fd: number, len?: number): Promise<void>--><!--Device-unnamed-declare function ftruncate(fd: number, len?: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| len | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |


## ftruncate

```TypeScript
declare function ftruncate(fd: number, callback: AsyncCallback<void>): void
```

Truncates a file based on the file descriptor. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:truncate](arkts-corefile-fileio-truncate-f.md#truncate)

<!--Device-unnamed-declare function ftruncate(fd: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function ftruncate(fd: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## ftruncate

```TypeScript
declare function ftruncate(fd: number, len: number, callback: AsyncCallback<void>): void
```

Truncates a file based on the file descriptor. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:truncate](arkts-corefile-fileio-truncate-f.md#truncate)

<!--Device-unnamed-declare function ftruncate(fd: number, len: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function ftruncate(fd: number, len: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| len | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
