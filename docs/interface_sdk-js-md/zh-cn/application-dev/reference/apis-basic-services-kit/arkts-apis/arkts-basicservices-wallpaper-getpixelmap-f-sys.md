# getPixelMap（系统接口）

## 导入模块

```TypeScript
import { wallpaper } from '@kit.BasicServicesKit';
```

## getPixelMap

```TypeScript
function getPixelMap(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void
```

获取壁纸图片的像素图。

> **说明：**&gt;
> 从 API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**需要权限：** ohos.permission.GET_WALLPAPER

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

wallpaper.getPixelMap(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: image.PixelMap) => {
  if (error) {
    console.error(`Failed to getPixelMap. Code: ${error.code}, message: ${error.message}`);
    return;
  }
  console.info(`success to getPixelMap: ${JSON.stringify(data.getImageInfoSync())}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

wallpaper.getPixelMap(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: image.PixelMap) => {
  console.info(`success to getPixelMap : ${JSON.stringify(data.getImageInfoSync())}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to getPixelMap. Code: ${error.code}, Message: ${error.message}`);
});
```


## getPixelMap

```TypeScript
function getPixelMap(wallpaperType: WallpaperType): Promise<image.PixelMap>
```

获取壁纸图片的像素图。

> **说明：**&gt;
> 从 API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**需要权限：** ohos.permission.GET_WALLPAPER

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**示例**

参见 [getPixelMap](#getpixelmap)
