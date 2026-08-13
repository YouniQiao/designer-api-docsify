# WallpaperChangeObserver

```TypeScript
type WallpaperChangeObserver = (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void
```

定义壁纸变化的监听回调函数。

**起始版本：** 23

**废弃版本：** -1

<!--Device-wallpaper-type WallpaperChangeObserver = (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void--><!--Device-wallpaper-type WallpaperChangeObserver = (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-na-wallpaper-wallpapertype-e.md) | 是 |
| [resourceType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-sceneresource-i.md) | [WallpaperResourceType](arkts-na-wallpaper-wallpaperresourcetype-e-sys.md) | 是 |
| uri | string | 否 |
