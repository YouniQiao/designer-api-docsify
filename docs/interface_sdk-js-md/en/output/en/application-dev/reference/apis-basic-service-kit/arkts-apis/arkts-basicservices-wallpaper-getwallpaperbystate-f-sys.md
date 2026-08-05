# getWallpaperByState (System API)

## getWallpaperByState

```TypeScript
function getWallpaperByState(wallpaperType: WallpaperType, foldState: FoldState, rotateState: RotateState): Promise<image.PixelMap>
```

Obtains the default pixel map of a wallpaper of the specified device type. Returns the default pixel map. Only the static wallpaper set by using setAllWallpapers can be obtained.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getWallpaperByState(wallpaperType: WallpaperType, foldState: FoldState, rotateState: RotateState): Promise<image.PixelMap>--><!--Device-wallpaper-function getWallpaperByState(wallpaperType: WallpaperType, foldState: FoldState, rotateState: RotateState): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wallpaperType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | indicates the wallpaper type. |
| foldState | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | indicates the folding status for wallpaper. |
| rotateState | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | indicates the rotation status for wallpaper. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | parameter error. Possible causes:1.Mandatory parameters are left unspecified.2.The type must be WallpaperType, parameter range must be WALLPAPER\_\_\_ESCAPED\_UNDERSCORE\_\_\_LOCKSCREEN or WALLPAPER\_\_\_ESCAPED\_UNDERSCORE\_\_\_SYSTEM.3.The type must be FoldState, parameter range must be NORMAL or UNFOLD\_\_\_ESCAPED\_UNDERSCORE\_\_\_ONCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_STATE or UNFOLD\_\_\_ESCAPED\_UNDERSCORE\_\_\_TWICE\_\_\_ESCAPED\_UNDERSCORE\_\_\_STATE.4.The type must be RotateState, parameter range must be PORTRAIT or LANDSCAPE. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { wallpaper } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

wallpaper.getWallpaperByState(wallpaper.WallpaperType.WALLPAPER_SYSTEM,wallpaper.FoldState.NORMAL,wallpaper.RotateState.PORTRAIT).then((data:image.PixelMap) => {
  console.info(`success to getWallpaperByState: ${JSON.stringify(data.getImageInfoSync())}`);
}).catch((error: BusinessError) => {
  console.error(`failed to getWallpaperByState. Code: ${error.code}, Message: ${error.message}`);
});
```

