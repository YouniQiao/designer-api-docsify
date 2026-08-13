# WallpaperChangeObserver

```TypeScript
type WallpaperChangeObserver = (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void
```

Defines a callback used to return wallpaper change.

**Since:** 23

**Deprecated since:** -1

<!--Device-wallpaper-type WallpaperChangeObserver = (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void--><!--Device-wallpaper-type WallpaperChangeObserver = (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |
| [resourceType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-sceneresource-i.md) | [WallpaperResourceType](arkts-basicservices-wallpaper-wallpaperresourcetype-e-sys.md) | Yes |
| uri | string | No |
