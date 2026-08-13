# getColorsSync (System API)

## Modules to Import

```TypeScript
import { wallpaper } from '@kit.BasicServicesKit';
```

## getColorsSync

```TypeScript
function getColorsSync(wallpaperType: WallpaperType): Array<RgbaColor>
```

Obtains the wallpaper colors for the wallpaper of the specified type. Returns rgbaColor type of array callback function.

**Since:** 9

**Deprecated since:** 23

<!--Device-wallpaper-function getColorsSync(wallpaperType: WallpaperType): Array<RgbaColor>--><!--Device-wallpaper-function getColorsSync(wallpaperType: WallpaperType): Array<RgbaColor>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[RgbaColor](arkts-basicservices-wallpaper-rgbacolor-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
try {
    let colors = wallpaper.getColorsSync(wallpaper.WallpaperType.WALLPAPER_SYSTEM);
    console.info(`success to getColorsSync: ${JSON.stringify(colors)}`);
} catch (error) {
    console.error(`failed to getColorsSync. Code: ${error.code}, Message: ${error.message}`);
}
```
