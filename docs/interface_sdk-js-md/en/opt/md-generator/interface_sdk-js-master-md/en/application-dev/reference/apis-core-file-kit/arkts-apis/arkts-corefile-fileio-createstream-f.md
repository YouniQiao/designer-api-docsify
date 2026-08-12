# createStream

## createStream

```TypeScript
declare function createStream(path: string, mode: string): Promise<Stream>
```

Creates a stream based on the file path. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createStream](arkts-corefile-file-fs-createstream-f.md#createStream)

<!--Device-unnamed-declare function createStream(path: string, mode: string): Promise<Stream>--><!--Device-unnamed-declare function createStream(path: string, mode: string): Promise<Stream>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Stream](arkts-corefile-fileio-stream-depr-i.md)&gt; |


## createStream

```TypeScript
declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void
```

Creates a stream based on the file path. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createStream](arkts-corefile-file-fs-createstream-f.md#createStream)

<!--Device-unnamed-declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void--><!--Device-unnamed-declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stream](arkts-corefile-fileio-stream-depr-i.md)&gt; | Yes |
