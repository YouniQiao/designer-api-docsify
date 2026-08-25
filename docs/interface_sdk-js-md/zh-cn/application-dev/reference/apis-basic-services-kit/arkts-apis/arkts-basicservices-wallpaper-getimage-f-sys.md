# getImage（系统接口）

## 导入模块

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## getImage

```TypeScript
function getImage(wallpaperType: WallpaperType, callback: AsyncCallback<image.PixelMap>): void
```

获取壁纸图片的像素图，且只能获取使用setImage设置的静态壁纸。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_WALLPAPER

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## getImage

```TypeScript
function getImage(wallpaperType: WallpaperType): Promise<image.PixelMap>
```

获取壁纸图片的像素图，且只能获取使用setImage设置的静态壁纸。使用promise异步回调。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
