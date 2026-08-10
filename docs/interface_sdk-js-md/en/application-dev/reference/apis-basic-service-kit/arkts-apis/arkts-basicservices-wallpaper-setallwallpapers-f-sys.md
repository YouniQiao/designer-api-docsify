# setAllWallpapers (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## setAllWallpapers

```TypeScript
function setAllWallpapers(wallpaperInfos: Array<WallpaperInfo>, wallpaperType: WallpaperType): Promise<void>
```

设置设备所有形态的壁纸。使用promise异步回调。（包括折展状态、横竖屏状态、资源路径，其中NORMAL-PORT为必选）

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_WALLPAPER

<!--Device-wallpaper-function setAllWallpapers(wallpaperInfos: Array<WallpaperInfo>, wallpaperType: WallpaperType): Promise<void>--><!--Device-wallpaper-function setAllWallpapers(wallpaperInfos: Array<WallpaperInfo>, wallpaperType: WallpaperType): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wallpaperInfos | Array&lt;WallpaperInfo&gt; | Yes | 所有壁纸的信息结构。 |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | Yes | 壁纸类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.The first parameter type must be Array&lt;WallpaperInfo&gt;. The second type must be WallpaperType. 3.The first parameter type must be Array&lt;WallpaperInfo&gt;, must include wallpaper with FoldState NORMAL and RotateState PORTRAIT. |
| 201 | permission denied. |
| 202 | permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { wallpaper } from '@kit.BasicServicesKit';

let wallpaperInfos: Array<wallpaper.WallpaperInfo>
wallpaperInfos = [
  {
    foldState: wallpaper.FoldState.NORMAL,
    rotateState: wallpaper.RotateState.PORTRAIT,
    source: '/data/storage/el2/base/haps/entry/files/normal.jpeg'
  },
  {
    foldState: wallpaper.FoldState.UNFOLD_ONCE_STATE,
    rotateState: wallpaper.RotateState.LANDSCAPE,
    source: '/data/storage/el2/base/haps/entry/files/unfold_once_state.jpeg'
  },
  {
    foldState: wallpaper.FoldState.UNFOLD_TWICE_STATE,
    rotateState: wallpaper.RotateState.PORTRAIT,
    source: '/data/storage/el2/base/haps/entry/files/unfold_twice_state.jpeg'
  }
];
wallpaper.setAllWallpapers(wallpaperInfos, wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
  console.info(`success to setAllWallpapers.`);
}).catch((error: BusinessError) => {
  console.error(`failed to setAllWallpapers. Code: ${error.code}, Message: ${error.message}`);
});
```

