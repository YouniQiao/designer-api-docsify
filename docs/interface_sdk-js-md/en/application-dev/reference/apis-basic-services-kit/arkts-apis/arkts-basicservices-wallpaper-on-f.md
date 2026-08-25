# on

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## on('colorChange')

```TypeScript
function on(type: 'colorChange', callback: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void
```

Registers a listener for wallpaper color changes to receive notifications about the changes.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'colorChange' | Yes |
| callback | (colors: Array&lt;[RgbaColor](arkts-basicservices-wallpaper-rgbacolor-i.md)&gt;, wallpaperType: WallpaperType) =&gt; void | Yes |
