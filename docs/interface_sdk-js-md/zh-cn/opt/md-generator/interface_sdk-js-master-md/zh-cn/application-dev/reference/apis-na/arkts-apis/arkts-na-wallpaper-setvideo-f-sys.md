# setVideo（系统接口）

## setVideo

```TypeScript
function setVideo(source: string, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void
```

将视频资源设置为桌面或锁屏的动态壁纸。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_WALLPAPER

<!--Device-wallpaper-function setVideo(source: string, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void--><!--Device-wallpaper-function setVideo(source: string, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | string | 是 |
| wallpaperType | [WallpaperType](arkts-na-wallpaper-wallpapertype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let wallpaperPath = "/data/storage/el2/base/haps/entry/files/test.mp4";
try {
    wallpaper.setVideo(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
        if (error) {
            console.error(`failed to setVideo. Code: ${error.code}, Message: ${error.message}`);
            return;
        }
        console.info(`success to setVideo.`);
    });
} catch (error) {
    console.error(`failed to setVideo. Code: ${error.code}, Message: ${error.message}`);
}
```


## setVideo

```TypeScript
function setVideo(source: string, wallpaperType: WallpaperType): Promise<void>
```

将视频资源设置为桌面或锁屏的动态壁纸。使用promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_WALLPAPER

<!--Device-wallpaper-function setVideo(source: string, wallpaperType: WallpaperType): Promise<void>--><!--Device-wallpaper-function setVideo(source: string, wallpaperType: WallpaperType): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | string | 是 |
| wallpaperType | [WallpaperType](arkts-na-wallpaper-wallpapertype-e.md) | 是 |

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

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let wallpaperPath = "/data/storage/el2/base/haps/entry/files/test.mp4";
try {
    wallpaper.setVideo(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
        console.info(`success to setVideo.`);
    }).catch((error: BusinessError) => {
        console.error(`failed to setVideo. Code: ${error.code}, Message: ${error.message}`);
    });
} catch (error) {
    console.error(`failed to setVideo. Code: ${error.code}, Message: ${error.message}`);
}
```
