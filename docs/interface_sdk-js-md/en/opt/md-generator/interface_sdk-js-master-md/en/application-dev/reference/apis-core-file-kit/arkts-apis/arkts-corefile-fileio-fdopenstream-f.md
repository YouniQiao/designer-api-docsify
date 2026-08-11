# fdopenStream

## fdopenStream

```TypeScript
declare function fdopenStream(fd: number, mode: string): Promise<Stream>
```

Opens a stream based on the file descriptor. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:fdopenStream](arkts-corefile-fileio-fdopenstream-f.md#fdopenstream)

<!--Device-unnamed-declare function fdopenStream(fd: number, mode: string): Promise<Stream>--><!--Device-unnamed-declare function fdopenStream(fd: number, mode: string): Promise<Stream>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| mode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Stream&gt; |


## fdopenStream

```TypeScript
declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void
```

Opens a stream based on the file descriptor. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:fdopenStream](arkts-corefile-fileio-fdopenstream-f.md#fdopenstream)

<!--Device-unnamed-declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void--><!--Device-unnamed-declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| mode | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Stream&gt; | Yes |
