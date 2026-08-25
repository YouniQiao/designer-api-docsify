# FileAsset (System API)

Provides APIs for encapsulating file asset attributes.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [PhotoAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## close

```TypeScript
close(fd: number, callback: AsyncCallback<void>): void
```

Closes a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** close

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## close

```TypeScript
close(fd: number): Promise<void>
```

Closes this file. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** close

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## commitModify

```TypeScript
commitModify(callback: AsyncCallback<void>): void
```

Commits the modification on the file metadata to the database. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [commitModify](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#commitmodify)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## commitModify

```TypeScript
commitModify(): Promise<void>
```

Commits the modification on the file metadata to the database. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [commitModify](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#commitmodify)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## favorite

```TypeScript
favorite(isFavorite: boolean, callback: AsyncCallback<void>): void
```

Favorites or unfavorites a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [setFavorite](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#setfavorite)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isFavorite | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## favorite

```TypeScript
favorite(isFavorite: boolean): Promise<void>
```

Favorites or unfavorites this file asset. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [setFavorite](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#setfavorite)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isFavorite | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## get

```TypeScript
get(member: string): MemberType
```

Obtains the value of a **FileAsset** parameter.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [get](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#get)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| member | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MemberType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-membertype-t.md) |

## getExif

```TypeScript
getExif(callback: AsyncCallback<string>): void
```

Obtains the EXIF data from a JPG image and returns a JSON string. This API uses an asynchronous callback to return the result.For details about the EXIF tags, see [image.PropertyKey](../../apis-image-kit/arkts-apis/arkts-image-image-propertykey-e.md).  
| Key Value | Description | | --------------------------------------- | ----------------- | | BitsPerSample | Number of bits per sample.| | [Orientation](../../apis-arkui/arkts-apis/arkts-arkui-window-orientation-e.md) | Image orientation.| | ImageLength | Image length.| | ImageWidth | Image width.| | GPSLatitude | GPS latitude of the image.| | GPSLongitude | GPS longitude of the image.| | GPSLatitudeRef | Longitude reference, for example, W or E.| | GPSLongitudeRef | Latitude reference, for example, N or S.| | DateTimeOriginal | Shooting time.| | ExposureTime | Exposure time.| | [SceneType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-scenetype-e.md) | Scene type.| | ISOSpeedRatings | ISO sensitivity or speed.| | FNumber | f-number.| | DateTime | Modification time.| | GPSTimeStamp | GPS timestamp.| | GPSDateStamp | GPS date stamp.| | ImageDescription | Image description.| | Make | Manufacturer.| | MakeNote | Manufacturer.| | [Model](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-model-i.md) | Model.| | PhotoMode | Photo mode.| | SensitivityType | Sensitivity type.| | StandardOutputSensitivity | Standard output sensitivity.| | RecommendedExposureIndex | Recommended exposure index.| | ApertureValue | Aperture value.| | MeteringMode | Metering mode.| | [LightSource](../../apis-arkui/arkts-components/arkts-arkui-lightsource-i-sys.md) | Light source.| | [Flash](../../apis-camera-kit/arkts-apis/arkts-camera-camera-flash-i.md) | Flash status.| | FocalLength | Focal length.| | UserComment | User comments.| | PixelXDimension | Pixel X dimension.| | PixelYDimension | Pixel Y dimension.| | [WhiteBalance](../../apis-camera-kit/arkts-apis/arkts-camera-camera-whitebalance-i.md) | White balance.| | FocalLengthIn35mmFilm | Focal length in 35 mm film.| | ExposureBiasValue |

> **NOTE：**&gt;
> This API returns a JSON string that contains EXIF tags. The complete Exif information consists of all_exif and
> [ImageVideoKey](arkts-corefile-userfilemanager-imagevideokey-e-sys.md).USER_COMMENT. The two fields need to be passed to
> **fetchColumns**.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getExif](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i-sys.md#getexif)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getExif

```TypeScript
getExif(): Promise<string>
```

Obtains the EXIF data from a JPG image and returns a JSON string. This API uses a promise to return the result.For details about the EXIF tags, see [image.PropertyKey](../../apis-image-kit/arkts-apis/arkts-image-image-propertykey-e.md).  
| Key Value | Description | | --------------------------------------- | ----------------- | | BitsPerSample | Number of bits per sample.| | [Orientation](../../apis-arkui/arkts-apis/arkts-arkui-window-orientation-e.md) | Image orientation.| | ImageLength | Image length.| | ImageWidth | Image width.| | GPSLatitude | GPS latitude of the image.| | GPSLongitude | GPS longitude of the image.| | GPSLatitudeRef | Longitude reference, for example, W or E.| | GPSLongitudeRef | Latitude reference, for example, N or S.| | DateTimeOriginal | Shooting time.| | ExposureTime | Exposure time.| | [SceneType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-scenetype-e.md) | Scene type.| | ISOSpeedRatings | ISO sensitivity or speed.| | FNumber | f-number.| | DateTime | Modification time.| | GPSTimeStamp | GPS timestamp.| | GPSDateStamp | GPS date stamp.| | ImageDescription | Image description.| | Make | Manufacturer.| | MakeNote | Manufacturer.| | [Model](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-model-i.md) | Model.| | PhotoMode | Photo mode.| | SensitivityType | Sensitivity type.| | StandardOutputSensitivity | Standard output sensitivity.| | RecommendedExposureIndex | Recommended exposure index.| | ApertureValue | Aperture value.| | MeteringMode | Metering mode.| | [LightSource](../../apis-arkui/arkts-components/arkts-arkui-lightsource-i-sys.md) | Light source.| | [Flash](../../apis-camera-kit/arkts-apis/arkts-camera-camera-flash-i.md) | Flash status.| | FocalLength | Focal length.| | UserComment | User comments.| | PixelXDimension | Pixel X dimension.| | PixelYDimension | Pixel Y dimension.| | [WhiteBalance](../../apis-camera-kit/arkts-apis/arkts-camera-camera-whitebalance-i.md) | White balance.| | FocalLengthIn35mmFilm | Focal length in 35 mm film.| | ExposureBiasValue |

> **NOTE：**&gt;
> This API returns a JSON string that contains EXIF tags. The complete Exif information consists of all_exif and
> [ImageVideoKey](arkts-corefile-userfilemanager-imagevideokey-e-sys.md).USER_COMMENT. The two fields need to be passed to
> **fetchColumns**.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getExif](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i-sys.md#getexif)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getThumbnail

```TypeScript
getThumbnail(callback: AsyncCallback<image.PixelMap>): void
```

Obtains the thumbnail of a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getThumbnail](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#getthumbnail)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO or ohos.permission.READ_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

## getThumbnail

```TypeScript
getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void
```

Obtains the file thumbnail of the given size. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getThumbnail](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#getthumbnail)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO or ohos.permission.READ_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | image.Size | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

## getThumbnail

```TypeScript
getThumbnail(size?: image.Size): Promise<image.PixelMap>
```

Obtains the file thumbnail of the given size. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getThumbnail](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#getthumbnail)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO or ohos.permission.READ_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | image.Size | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

## open

```TypeScript
open(mode: string, callback: AsyncCallback<number>): void
```

Opens this file asset. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The write operations are mutually exclusive. After a write operation is complete, you must call **close** to
> close the file.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** open

**Required permissions:** ohos.permission.READ_IMAGEVIDEO or ohos.permission.READ_AUDIO or ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## open

```TypeScript
open(mode: string): Promise<number>
```

Opens this file asset. This API uses a promise to return the result.

> **NOTE：**&gt;
> The write operations are mutually exclusive. After a write operation is complete, you must call **close** to
> close the file.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** open

**Required permissions:** ohos.permission.READ_IMAGEVIDEO or ohos.permission.READ_AUDIO or ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## set

```TypeScript
set(member: string, value: string): void
```

Sets a **FileAsset** parameter.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [set](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#set)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| member | string | Yes |
| value | string | Yes |

## setHidden

```TypeScript
setHidden(hiddenState: boolean, callback: AsyncCallback<void>): void
```

Sets a file to hidden state. This API uses an asynchronous callback to return the result.The private files set to hidden state are located in the private album (in hidden state) and are not open to third-party applications. After obtaining private files from the private album, users can set **hiddenState** to **false** to remove them from the private album.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [setHidden](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c-sys.md#sethidden)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hiddenState | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900020 |

## setHidden

```TypeScript
setHidden(hiddenState: boolean): Promise<void>
```

Sets this file asset to the hidden state. This API uses a promise to return the result.The private files set to hidden state are located in the private album (in hidden state) and are not open to third-party applications. After obtaining private files from the private album, users can set **hiddenState** to **false** to remove them from the private album.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [setHidden](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c-sys.md#sethidden)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hiddenState | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900020 |

## setUserComment

```TypeScript
setUserComment(userComment: string, callback: AsyncCallback<void>): void
```

Sets user comment information of an image or video. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can only be used to set user comment information of an image or video.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [setUserComment](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c-sys.md#setusercomment)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userComment | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setUserComment

```TypeScript
setUserComment(userComment: string): Promise<void>
```

Sets user comment information of an image or video. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can only be used to set user comment information of an image or video.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [setUserComment](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c-sys.md#setusercomment)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userComment | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## displayName

```TypeScript
displayName: string
```

File name, including the file name extension, to display.

**Type:** string

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [displayName](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#displayname)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## fileType

```TypeScript
readonly fileType: FileType
```

Type of the file.

**Type:** [FileType](arkts-corefile-userfilemanager-filetype-e-sys.md)

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [photoType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#phototype)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## uri

```TypeScript
readonly uri: string
```

Media asset URI, for example, **file://media/Photo/1/IMG_datetime_0001/displayName.jpg**. For details, see [Media File URI](../../../file-management/user-file-uri-intro.md#media-file-uri).

**Type:** string

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [uri](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoasset-i.md#uri)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.
