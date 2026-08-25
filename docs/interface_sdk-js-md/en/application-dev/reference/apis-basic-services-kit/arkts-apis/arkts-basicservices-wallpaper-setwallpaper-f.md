# setWallpaper

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## setWallpaper

```TypeScript
function setWallpaper(
    source: string | image.PixelMap,
    wallpaperType: WallpaperType,
    callback: AsyncCallback<void>
  ): void
```

Sets a wallpaper of the specified type based on the uri path from a JPEG or PNG file or the pixel map of a PNG file.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.SET_WALLPAPER

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | string \| image.PixelMap | Yes |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## setWallpaper

```TypeScript
function setWallpaper(source: string | image.PixelMap, wallpaperType: WallpaperType): Promise<void>
```

Sets a wallpaper of the specified type based on the uri path from a JPEG or PNG file or the pixel map of a PNG file.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.SET_WALLPAPER

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | string \| image.PixelMap | Yes |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
