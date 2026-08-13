# on_colorChange

## Modules to Import

```TypeScript
import { wallpaper } from '@kit.BasicServicesKit';
```

## on_colorChange

```TypeScript
function on(type: 'colorChange', callback: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void
```

Registers a listener for wallpaper color changes to receive notifications about the changes.

**Since:** 7

**Deprecated since:** 9

<!--Device-wallpaper-function on(type: 'colorChange', callback: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void--><!--Device-wallpaper-function on(type: 'colorChange', callback: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'colorChange' | Yes |
| callback | (colors: Array&lt;[RgbaColor](arkts-basicservices-wallpaper-rgbacolor-i.md)&gt;, wallpaperType: WallpaperType) =&gt; void | Yes |

## Examples

```TypeScript
try {
    let listener = (colors: Array<wallpaper.RgbaColor>, wallpaperType: wallpaper.WallpaperType): void => {
        console.info(`wallpaper color changed.`);
    };
    wallpaper.on('colorChange', listener);
} catch (error) {
    console.error(`failed to on because: ${JSON.stringify(error)}`);
}
```
