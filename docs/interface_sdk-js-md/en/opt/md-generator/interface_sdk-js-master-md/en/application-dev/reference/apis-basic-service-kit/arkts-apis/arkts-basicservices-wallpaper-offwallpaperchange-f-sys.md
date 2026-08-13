# offWallpaperChange (System API)

## Modules to Import

```TypeScript
import { wallpaper } from '@kit.BasicServicesKit';
```

## offWallpaperChange

```TypeScript
function offWallpaperChange(callback?: WallpaperChangeObserver): void
```

Unregisters a listener for wallpaper changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-wallpaper-function offWallpaperChange(callback?: WallpaperChangeObserver): void--><!--Device-wallpaper-function offWallpaperChange(callback?: WallpaperChangeObserver): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [WallpaperChangeObserver](arkts-basicservices-wallpaper-wallpaperchangeobserver-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
