# setCustomWallpaper (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## setCustomWallpaper

```TypeScript
function setCustomWallpaper(source: string, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void
```

将指定的zip资源包设置为桌面或锁屏的壁纸资源，仅当com.ohos.sceneboard存在时，支持使用该接口。且具有ohos.permission.GET_WALLPAPER权限的应用可以访问/data/wallpaper/目录获取设置的资源。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_WALLPAPER

<!--Device-wallpaper-function setCustomWallpaper(source: string, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void--><!--Device-wallpaper-function setCustomWallpaper(source: string, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | string | Yes | 指定的zip资源包。 |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes | 壁纸类型。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，设置壁纸成功，error为undefined，否则返回error信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 201 | permission denied. |
| 202 | permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let wallpaperPath = "/data/storage/el2/base/haps/entry/files/test.zip";
try {
    wallpaper.setCustomWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
        if (error) {
            console.error(`failed to setCustomWallpaper. Code: ${error.code}, Message: ${error.message}`);
            return;
        }
        console.info(`success to setCustomWallpaper.`);
    });
} catch (error) {
    console.error(`failed to setCustomWallpaper. Code: ${error.code}, Message: ${error.message}`);
}
```


## setCustomWallpaper

```TypeScript
function setCustomWallpaper(source: string, wallpaperType: WallpaperType): Promise<void>
```

将指定的zip资源包设置为桌面或锁屏的壁纸资源，仅当com.ohos.sceneboard存在时，支持使用该接口。且具有ohos.permission.GET_WALLPAPER权限的应用可以访问/data/wallpaper/目录获取设置的资源。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_WALLPAPER

<!--Device-wallpaper-function setCustomWallpaper(source: string, wallpaperType: WallpaperType): Promise<void>--><!--Device-wallpaper-function setCustomWallpaper(source: string, wallpaperType: WallpaperType): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | string | Yes | 指定的zip资源包。 |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes | 壁纸类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 201 | permission denied. |
| 202 | permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let wallpaperPath = "/data/storage/el2/base/haps/entry/files/test.zip";
try {
    wallpaper.setCustomWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
        console.info(`success to setCustomWallpaper.`);
    }).catch((error: BusinessError) => {
        console.error(`failed to setCustomWallpaper. Code: ${error.code}, Message: ${error.message}`);
    });
} catch (error) {
    console.error(`failed to setCustomWallpaper. Code: ${error.code}, Message: ${error.message}`);
}
```

