# getWallpaperByState（系统接口）

## 导入模块

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## getWallpaperByState

```TypeScript
function getWallpaperByState(wallpaperType: WallpaperType, foldState: FoldState, rotateState: RotateState): Promise<image.PixelMap>
```

获取指定壁纸类型、折展态、横竖屏的壁纸图片的像素图，如果指定的壁纸不存在，会逐步降级匹配，unfolded-land -&gt; unfolded-port -&gt;normal-port。使用promise异步回调。

**起始版本：** 14

**需要权限：** ohos.permission.GET_WALLPAPER

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |
| [foldState](arkts-basicservices-wallpaper-wallpaperinfo-i-sys.md) | [FoldState](arkts-basicservices-wallpaper-foldstate-e-sys.md) | 是 |
| [rotateState](arkts-basicservices-wallpaper-wallpaperinfo-i-sys.md) | [RotateState](arkts-basicservices-wallpaper-rotatestate-e-sys.md) | 是 |

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
