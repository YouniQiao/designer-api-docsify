# WallpaperExtensionAbility (System API)

class of wallpaper extension ability.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

<!--Device-unnamed-declare class WallpaperExtensionAbility--><!--Device-unnamed-declare class WallpaperExtensionAbility-End-->

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

初始化壁纸扩展应用。在拉起Extension壁纸扩展应用时触发回调，执行初始化应用操作。不支持多线程并发调用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WallpaperExtensionAbility-onCreate(want: object): void--><!--Device-WallpaperExtensionAbility-onCreate(want: object): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | object | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

## Examples

```TypeScript
import { WallpaperExtensionAbility } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

class WallpaperExt extends WallpaperExtensionAbility {
    onCreate(want: Want): void {
        console.info('onCreate, want:' + want.abilityName);
    }
}
```

## onDestroy

```TypeScript
onDestroy(): void
```

清理壁纸扩展应用资源。在销毁壁纸扩展应用时触发回调，执行资源清理。不支持多线程并发调用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WallpaperExtensionAbility-onDestroy(): void--><!--Device-WallpaperExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

## Examples

```TypeScript
import { WallpaperExtensionAbility } from '@kit.BasicServicesKit';

class WallpaperExt extends WallpaperExtensionAbility {
    onDestroy(): void {
        console.info('onDestroy');
    }
}
```

## onWallpaperChange

```TypeScript
onWallpaperChange(wallpaperType: number): void
```

监听壁纸变化。在壁纸变化时触发回调。不支持多线程并发调用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WallpaperExtensionAbility-onWallpaperChange(wallpaperType: number): void--><!--Device-WallpaperExtensionAbility-onWallpaperChange(wallpaperType: number): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wallpaperType | number | Yes | 壁纸类型。主屏幕壁纸为0，锁屏壁纸为1。 |

## Examples

```TypeScript
import { WallpaperExtensionAbility } from '@kit.BasicServicesKit';
import { wallpaper } from '@kit.BasicServicesKit';

class WallpaperExt extends WallpaperExtensionAbility {
    onWallpaperChange(wallpaperType: wallpaper.WallpaperType): void {
        console.info('onWallpaperChange, wallpaperType:' + wallpaperType);
    }
}
```

