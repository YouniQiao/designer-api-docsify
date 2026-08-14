# onWallpaperChange (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'wallpaper';
```

## onWallpaperChange

```TypeScript
function onWallpaperChange(callback: WallpaperChangeObserver): void
```

Registers a listener for wallpaper changes to receive notifications about the changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-wallpaper-function onWallpaperChange(callback: WallpaperChangeObserver): void--><!--Device-wallpaper-function onWallpaperChange(callback: WallpaperChangeObserver): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [WallpaperChangeObserver](arkts-basicservices-wallpaper-wallpaperchangeobserver-t.md) | Yes | The observer of wallpaper change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |

