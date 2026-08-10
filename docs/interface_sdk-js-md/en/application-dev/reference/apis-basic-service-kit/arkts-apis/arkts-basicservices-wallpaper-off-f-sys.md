# off (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## off('wallpaperChange')

```TypeScript
function off(
    type: 'wallpaperChange',
    callback?: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void
  ): void
```

取消订阅壁纸变化通知事件。不支持多线程并发调用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-wallpaper-function off(    type: 'wallpaperChange',    callback?: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void  ): void--><!--Device-wallpaper-function off(    type: 'wallpaperChange',    callback?: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void  ): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'wallpaperChange' | Yes | 事件回调类型。支持的事件为'wallpaperChange'，完成壁纸切换后触发该事件。 |
| callback | (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) =&gt; void | No | 表示要取消的壁纸变化回调，不填写该参数则取消订阅该type对应的所有回调。&lt;br/&gt;- wallpaperType：壁纸类型。&lt;br/&gt;- resourceType：壁 纸资源类型。&lt;br/&gt;- uri：壁纸资源地址。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 202 | permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
let listener = (wallpaperType: wallpaper.WallpaperType, resourceType: wallpaper.WallpaperResourceType): void => {
    console.info(`wallpaper color changed.`);
};
try {
    wallpaper.on('wallpaperChange', listener);
} catch (error) {
    console.error(`failed to on. Code: ${error.code}, Message: ${error.message}`);
}

try {
    // Unsubscribe from the listener.
    wallpaper.off('wallpaperChange', listener);
} catch (error) {
    console.error(`failed to off. Code: ${error.code}, Message: ${error.message}`);
}

try {
    // Unsubscribe from all callbacks of the 'wallpaperChange' event type.
    wallpaper.off('wallpaperChange');
} catch (error) {
    console.error(`failed to off. Code: ${error.code}, Message: ${error.message}`);
}
```

