# WallpaperExtensionAbility（系统接口）

class of wallpaper extension ability.

**起始版本：** 10

**废弃版本：** 23

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { WallpaperExtensionAbility } from 'kits/@kit.BasicServicesKit';
```

## onCreate

```TypeScript
onCreate(want: object): void
```

初始化壁纸扩展应用。在拉起Extension壁纸扩展应用时触发回调，执行初始化应用操作。不支持多线程并发调用。

**起始版本：** 10

**废弃版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | object | 是 |

## onDestroy

```TypeScript
onDestroy(): void
```

清理壁纸扩展应用资源。在销毁壁纸扩展应用时触发回调，执行资源清理。不支持多线程并发调用。

**起始版本：** 10

**废弃版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

## onWallpaperChange

```TypeScript
onWallpaperChange(wallpaperType: number): void
```

监听壁纸变化。在壁纸变化时触发回调。不支持多线程并发调用。

**起始版本：** 10

**废弃版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | number | 是 |
