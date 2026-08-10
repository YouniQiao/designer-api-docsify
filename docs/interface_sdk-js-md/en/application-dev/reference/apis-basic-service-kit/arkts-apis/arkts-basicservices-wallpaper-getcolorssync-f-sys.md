# getColorsSync (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## getColorsSync

```TypeScript
function getColorsSync(wallpaperType: WallpaperType): Array<RgbaColor>
```

获取指定类型壁纸的主要颜色信息。

> **说明：**
> 
> 从 API version 9开始支持，从API version 23开始废弃。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

<!--Device-wallpaper-function getColorsSync(wallpaperType: WallpaperType): Array<RgbaColor>--><!--Device-wallpaper-function getColorsSync(wallpaperType: WallpaperType): Array<RgbaColor>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;RgbaColor&gt; | 返回壁纸的主要颜色信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 202 | permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
try {
    let colors = wallpaper.getColorsSync(wallpaper.WallpaperType.WALLPAPER_SYSTEM);
    console.info(`success to getColorsSync: ${JSON.stringify(colors)}`);
} catch (error) {
    console.error(`failed to getColorsSync. Code: ${error.code}, Message: ${error.message}`);
}
```

