# getPixelMap (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## getPixelMap

```TypeScript
function getPixelMap(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void
```

Obtains the default pixel map of a wallpaper of the specified type. Returns the default pixel map.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getPixelMap(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void--><!--Device-wallpaper-function getPixelMap(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

wallpaper.getPixelMap(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: image.PixelMap) => {
  if (error) {
    console.error(`failed to getPixelMap. Code: ${error.code}, Message: ${error.message}`);
    return;
  }
  console.info(`success to getPixelMap : ${JSON.stringify(data.getImageInfoSync())}`);
});
```


## getPixelMap

```TypeScript
function getPixelMap(wallpaperType: WallpaperType): Promise<image.PixelMap>
```

Obtains the default pixel map of a wallpaper of the specified type. Returns the default pixel map.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getPixelMap(wallpaperType: WallpaperType): Promise<image.PixelMap>--><!--Device-wallpaper-function getPixelMap(wallpaperType: WallpaperType): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;image.PixelMap&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

wallpaper.getPixelMap(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: image.PixelMap) => {
  console.info(`success to getPixelMap : ${JSON.stringify(data.getImageInfoSync())}`);
}).catch((error: BusinessError) => {
  console.error(`failed to getPixelMap. Code: ${error.code}, Message: ${error.message}`);
});
```
