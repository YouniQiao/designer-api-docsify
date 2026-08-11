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

Registers a listener for wallpaper changes to receive notifications about the changes.

**Since:** 10

<!--Device-wallpaper-function on(    type: 'wallpaperChange',    callback: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void  ): void--><!--Device-wallpaper-function on(    type: 'wallpaperChange',    callback: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void  ): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'wallpaperChange' | Yes |
| callback | (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) =&gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
