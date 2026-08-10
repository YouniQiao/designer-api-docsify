# WallpaperChangeObserver

```TypeScript
type WallpaperChangeObserver = (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void
```

定义壁纸变化的监听回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-wallpaper-type WallpaperChangeObserver = (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void--><!--Device-wallpaper-type WallpaperChangeObserver = (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes | 壁纸类型。 |
| resourceType | [WallpaperResourceType](arkts-basicservices-wallpaper-wallpaperresourcetype-e-sys.md) | Yes | 壁纸资源类型。 |
| uri | string | No | 壁纸资源地址。 |

