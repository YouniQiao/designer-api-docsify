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

Unregisters a listener for wallpaper changes.

**Since:** 10

<!--Device-wallpaper-function off(    type: 'wallpaperChange',    callback?: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void  ): void--><!--Device-wallpaper-function off(    type: 'wallpaperChange',    callback?: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void  ): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'wallpaperChange' | Yes |
| callback | (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) =&gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
