# WallpaperExtensionAbility (System API)

class of wallpaper extension ability.

**Since:** 10

**Deprecated since:** 23

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { WallpaperExtensionAbility } from 'kits/@kit.BasicServicesKit';
```

## onCreate

```TypeScript
onCreate(want: object): void
```

Called once to initialize the extension ability.

**Since:** 10

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | object | Yes |

## onDestroy

```TypeScript
onDestroy(): void
```

Called once to destroy the extension ability.

**Since:** 10

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

## onWallpaperChange

```TypeScript
onWallpaperChange(wallpaperType: number): void
```

The onWallpaperChange callback is triggered when the user modifies the wallpaper settings.

**Since:** 10

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wallpaperType | number | Yes |
