# AbsAlbum

Defines the abstract interface of albums.

**Inheritance/Implementation:** AbsAlbum extends lang.ISendable

**Since:** 12

<!--Device-sendablePhotoAccessHelper-interface AbsAlbum--><!--Device-sendablePhotoAccessHelper-interface AbsAlbum-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { sendablePhotoAccessHelper } from 'sendablePhotoAccessHelper';
```

## getSharedPhotoAssets

```TypeScript
getSharedPhotoAssets(options: photoAccessHelper.FetchOptions): Array<SharedPhotoAsset>
```

Fetch shared photo assets in an album.

**Since:** 14

**Required permissions:** ohos.permission.ACCESS_MEDIALIB_THUMB_DB

<!--Device-AbsAlbum-getSharedPhotoAssets(options: photoAccessHelper.FetchOptions): Array<SharedPhotoAsset>--><!--Device-AbsAlbum-getSharedPhotoAssets(options: photoAccessHelper.FetchOptions): Array<SharedPhotoAsset>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | photoAccessHelper.FetchOptions | Yes | Fetch options. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;SharedPhotoAsset&gt; | Returns the shared photo assets |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |
| 14000011 | Internal system error |

