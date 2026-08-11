# PhotoAsset

PhotoAsset provides APIs for encapsulating file asset attributes.

**Since:** 10

<!--Device-photoAccessHelper-interface PhotoAsset--><!--Device-photoAccessHelper-interface PhotoAsset-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## clone

```TypeScript
clone(title: string): Promise<PhotoAsset>
```

Clones a media asset. The file name can be set, but the file type cannot be changed. This API uses a promise to return the result.

**Since:** 14

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAsset-clone(title: string): Promise<PhotoAsset>--><!--Device-PhotoAsset-clone(title: string): Promise<PhotoAsset>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| title | string | Yes | Title of the cloned asset. The title must meet the following requirements: &lt;br&gt;- It must not contain a file name extension. &lt;br&gt;- The string length ranges from 1 to 255. (The asset file name is in the format of title + file name extension.) &lt;br&gt;- It must not contain any invalid characters, which are:\ / : ? " ' ` &lt; &gt; \|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;PhotoAsset&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## close

```TypeScript
close(fd: number, callback: AsyncCallback<void>): void
```

Closes the current file. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** @ohos.file.fs:fileIo.close

<!--Device-PhotoAsset-close(fd: number, callback: AsyncCallback<void>): void--><!--Device-PhotoAsset-close(fd: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## close

```TypeScript
close(fd: number): Promise<void>
```

Closes the current file. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** @ohos.file.fs:fileIo.close

<!--Device-PhotoAsset-close(fd: number): Promise<void>--><!--Device-PhotoAsset-close(fd: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## commitModify

```TypeScript
commitModify(callback: AsyncCallback<void>): void
```

Commits the modification on the file metadata to the database. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoAsset-commitModify(callback: AsyncCallback<void>): void--><!--Device-PhotoAsset-commitModify(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000001 |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## commitModify

```TypeScript
commitModify(): Promise<void>
```

Commits the modification on the file metadata to the database. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoAsset-commitModify(): Promise<void>--><!--Device-PhotoAsset-commitModify(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000001 |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## get

```TypeScript
get(member: string): MemberType
```

Obtains a **PhotoAsset** member parameter.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PhotoAsset-get(member: string): MemberType--><!--Device-PhotoAsset-get(member: string): MemberType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| member | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MemberType](arkts-medialibrary-photoaccesshelper-membertype-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000014 |

## getReadOnlyFd

```TypeScript
getReadOnlyFd(callback: AsyncCallback<number>): void
```

Opens this file in read-only mode. This API uses an asynchronous callback to return the result.

The returned FD must be closed when it is not required.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** @ohos.file.fs:fileIo.open

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAsset-getReadOnlyFd(callback: AsyncCallback<number>): void--><!--Device-PhotoAsset-getReadOnlyFd(callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## getReadOnlyFd

```TypeScript
getReadOnlyFd(): Promise<number>
```

Opens this file in read-only mode. This API uses a promise to return the result.

The returned FD must be closed when it is not required.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** @ohos.file.fs:fileIo.open

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAsset-getReadOnlyFd(): Promise<number>--><!--Device-PhotoAsset-getReadOnlyFd(): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## getThumbnail

```TypeScript
getThumbnail(callback: AsyncCallback<image.PixelMap>): void
```

Obtains the thumbnail of a file. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PhotoAsset-getThumbnail(callback: AsyncCallback<image.PixelMap>): void--><!--Device-PhotoAsset-getThumbnail(callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| 14000011 |

## getThumbnail

```TypeScript
getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void
```

Obtains the file thumbnail of the given size. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PhotoAsset-getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void--><!--Device-PhotoAsset-getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | image.Size | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| 14000011 |

## getThumbnail

```TypeScript
getThumbnail(size?: image.Size): Promise<image.PixelMap>
```

Obtains the file thumbnail of the given size. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PhotoAsset-getThumbnail(size?: image.Size): Promise<image.PixelMap>--><!--Device-PhotoAsset-getThumbnail(size?: image.Size): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | image.Size | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;image.PixelMap&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| 14000011 |

## set

```TypeScript
set(member: string, value: string): void
```

Sets a **PhotoAsset** member parameter.

**Since:** 10

<!--Device-PhotoAsset-set(member: string, value: string): void--><!--Device-PhotoAsset-set(member: string, value: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| member | string | Yes |
| value | string | Yes | Value of the member parameter to set. Only the value of [PhotoKeys](arkts-medialibrary-photoaccesshelper-photokeys-e.md).TITLE can be changed. The title must meet the following requirements: &lt;br&gt;- It must not contain a file name extension. &lt;br&gt;- The string length ranges from 1 to 255. (The asset file name is in the format of title + file name extension.) &lt;br&gt;- It must not contain any invalid characters, which are:\ / : ? " ' ` &lt; &gt; \|

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000014 |

## displayName

```TypeScript
readonly displayName: string
```

File name, including the file name extension, to display. The string length ranges from 1 to 255.

**Type:** string

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PhotoAsset-readonly displayName: string--><!--Device-PhotoAsset-readonly displayName: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoType

```TypeScript
readonly photoType: PhotoType
```

Type of the file.

**Type:** [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md)

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PhotoAsset-readonly photoType: PhotoType--><!--Device-PhotoAsset-readonly photoType: PhotoType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## uri

```TypeScript
readonly uri: string
```

Media asset URI, for example, **file://media/Photo/1/IMG_datetime_0001/displayName.jpg**. For details, see   
[Media File URI](../../../file-management/user-file-uri-intro.md#media-file-uri).

**Type:** string

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoAsset-readonly uri: string--><!--Device-PhotoAsset-readonly uri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
