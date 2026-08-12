# restore（系统接口）

## restore

```TypeScript
function restore(wallpaperType: WallpaperType, callback: AsyncCallback<void>): void
```

移除指定类型的壁纸，恢复为默认显示的壁纸。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.SET_WALLPAPER

<!--Device-wallpaper-function restore(wallpaperType: WallpaperType, callback: AsyncCallback<void>): void--><!--Device-wallpaper-function restore(wallpaperType: WallpaperType, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.restore(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
    if (error) {
        console.error(`failed to restore. Code: ${error.code}, Message: ${error.message}`);
        return;
    }
    console.info(`success to restore.`);
});
```


## restore

```TypeScript
function restore(wallpaperType: WallpaperType): Promise<void>
```

移除指定类型的壁纸，恢复为默认显示的壁纸。使用promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.SET_WALLPAPER

<!--Device-wallpaper-function restore(wallpaperType: WallpaperType): Promise<void>--><!--Device-wallpaper-function restore(wallpaperType: WallpaperType): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
 
wallpaper.restore(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
    console.info(`success to restore.`);
  }).catch((error: BusinessError) => {
    console.error(`failed to restore. Code: ${error.code}, Message: ${error.message}`);
});
```
