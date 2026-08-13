# FetchResult

FetchResult provides APIs to manage the file retrieval result.

**Since:** 23

**Deprecated since:** -1

<!--Device-photoAccessHelper-interface FetchResult--><!--Device-photoAccessHelper-interface FetchResult-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## getRangeObjects

```TypeScript
getRangeObjects(index: number, offset: number): Promise<T[]>
```

Obtains the file asset array of a specified length (second parameter) from the specified index (first parameter) in the result set. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-FetchResult-getRangeObjects(index: int, offset: int): Promise<T[]>--><!--Device-FetchResult-getRangeObjects(index: int, offset: int): Promise<T[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |
