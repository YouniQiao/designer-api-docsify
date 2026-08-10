# on (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## on('wallpaperChange')

```TypeScript
function on(
    type: 'wallpaperChange',
    callback: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void
  ): void
```

订阅壁纸变化通知事件。不支持多线程并发调用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-wallpaper-function on(    type: 'wallpaperChange',    callback: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void  ): void--><!--Device-wallpaper-function on(    type: 'wallpaperChange',    callback: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void  ): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'wallpaperChange' | Yes | 事件回调类型。支持的事件为'wallpaperChange'，完成壁纸切换后触发该事件。 |
| callback | (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) =&gt; void | Yes | 壁纸变化触发该回调方法，返回壁纸类型和壁纸资源类型。&lt;br/&gt;- wallpaperType：壁纸类型。&lt;br/&gt;- resourceType：壁纸资源类型。&lt;br/&gt; - uri：壁纸资源地址。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 202 | permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
try {
    let listener = (wallpaperType: wallpaper.WallpaperType, resourceType: wallpaper.WallpaperResourceType): void => {
        console.info(`wallpaper color changed.`);
    };
    wallpaper.on('wallpaperChange', listener);
} catch (error) {
    console.error(`failed to on. Code: ${error.code}, Message: ${error.message}`);
}
```

