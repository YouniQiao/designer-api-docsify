# getWallpaperByState (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## getWallpaperByState

```TypeScript
function getWallpaperByState(wallpaperType: WallpaperType, foldState: FoldState, rotateState: RotateState): Promise<image.PixelMap>
```

Obtains the default pixel map of a wallpaper of the specified device type. Returns the default pixel map.Only the static wallpaper set by using setAllWallpapers can be obtained.

**Since:** 14

**Required permissions:** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getWallpaperByState(wallpaperType: WallpaperType, foldState: FoldState, rotateState: RotateState): Promise<image.PixelMap>--><!--Device-wallpaper-function getWallpaperByState(wallpaperType: WallpaperType, foldState: FoldState, rotateState: RotateState): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |
| foldState | [FoldState](arkts-basicservices-wallpaper-foldstate-e-sys.md) | Yes |
| rotateState | [RotateState](arkts-basicservices-wallpaper-rotatestate-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;image.PixelMap&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
