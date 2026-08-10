# getPixelMap (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## getPixelMap

```TypeScript
function getPixelMap(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void
```

获取壁纸图片的像素图。

> **说明：**
> 
> 从 API version 7开始支持，从API version 9开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getPixelMap(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void--><!--Device-wallpaper-function getPixelMap(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes | 壁纸类型。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes | 回调函数，调用成功则返回壁纸图片的像素图对象，调用失败则返回error信息。 |

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

获取壁纸图片的像素图。

> **说明：**
> 
> 从 API version 7开始支持，从API version 9开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getPixelMap(wallpaperType: WallpaperType): Promise<image.PixelMap>--><!--Device-wallpaper-function getPixelMap(wallpaperType: WallpaperType): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes | 壁纸类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | 调用成功则返回壁纸图片的像素图对象，调用失败则返回error信息。 |

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

