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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-wallpaper-function offWallpaperChange(callback?: WallpaperChangeObserver): void--><!--Device-wallpaper-function offWallpaperChange(callback?: WallpaperChangeObserver): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [WallpaperChangeObserver](arkts-basicservices-wallpaper-wallpaperchangeobserver-t.md) | No | The observer of wallpaper change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |

