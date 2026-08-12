# getImage（系统接口）

## getImage

```TypeScript
function getImage(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void
```

获取壁纸图片的像素图，且只能获取使用setImage设置的静态壁纸。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getImage(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void--><!--Device-wallpaper-function getImage(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

wallpaper.getImage(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: image.PixelMap) => {
  if (error) {
    console.error(`failed to getImage. Code: ${error.code}, Message: ${error.message}`);
    return;
  }
  console.info(`success to getImage: ${JSON.stringify(data.getImageInfoSync())}`);
});
```


## getImage

```TypeScript
function getImage(wallpaperType: WallpaperType): Promise<image.PixelMap>
```

获取壁纸图片的像素图，且只能获取使用setImage设置的静态壁纸。使用promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getImage(wallpaperType: WallpaperType): Promise<image.PixelMap>--><!--Device-wallpaper-function getImage(wallpaperType: WallpaperType): Promise<image.PixelMap>-End-->

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

wallpaper.getImage(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: image.PixelMap) => {
  console.info(`success to getImage: ${JSON.stringify(data.getImageInfoSync())}`);
}).catch((error: BusinessError) => {
  console.error(`failed to getImage. Code: ${error.code}, Message: ${error.message}`);
});
```
