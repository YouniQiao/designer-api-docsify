# setVideo（系统接口）

## 导入模块

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## setVideo

```TypeScript
function setVideo(source: string, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void
```

将视频资源设置为桌面或锁屏的动态壁纸。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.SET_WALLPAPER

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | string | 是 |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## setVideo

```TypeScript
function setVideo(source: string, wallpaperType: WallpaperType): Promise<void>
```

将视频资源设置为桌面或锁屏的动态壁纸。使用promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.SET_WALLPAPER

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | string | 是 |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
