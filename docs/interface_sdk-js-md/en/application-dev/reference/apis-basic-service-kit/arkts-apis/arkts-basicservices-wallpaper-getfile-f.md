# getFile

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## getFile

```TypeScript
function getFile(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void
```

获取指定类型的壁纸文件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getFile(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void--><!--Device-wallpaper-function getFile(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |  |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |  |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: number) => {
    if (error) {
        console.error(`failed to getFile because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getFile: ${JSON.stringify(data)}`);
});
```


## getFile

```TypeScript
function getFile(wallpaperType: WallpaperType): Promise<number>
```

获取指定类型的壁纸文件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_WALLPAPER

<!--Device-wallpaper-function getFile(wallpaperType: WallpaperType): Promise<number>--><!--Device-wallpaper-function getFile(wallpaperType: WallpaperType): Promise<number>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | 调用成功则返回壁纸文件描述符ID，调用失败则返回error信息。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: number) => {
    console.info(`success to getFile: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getFile because: ${JSON.stringify(error)}`);
});
```

