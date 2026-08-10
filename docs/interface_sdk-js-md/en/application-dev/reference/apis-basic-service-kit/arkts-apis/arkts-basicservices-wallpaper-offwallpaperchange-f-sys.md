# offWallpaperChange (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## offWallpaperChange

```TypeScript
function offWallpaperChange(callback?: WallpaperChangeObserver): void
```

取消订阅壁纸变化通知事件。不支持多线程并发调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-wallpaper-function offWallpaperChange(callback?: WallpaperChangeObserver): void--><!--Device-wallpaper-function offWallpaperChange(callback?: WallpaperChangeObserver): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [WallpaperChangeObserver](arkts-basicservices-wallpaper-wallpaperchangeobserver-t.md) | No |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | permission verification failed, application which is not a system application uses system API. |

