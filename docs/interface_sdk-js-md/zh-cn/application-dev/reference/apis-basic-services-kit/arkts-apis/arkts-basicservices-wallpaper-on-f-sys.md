# on（系统接口）

## 导入模块

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## on('wallpaperChange')

```TypeScript
function on(
    type: 'wallpaperChange',
    callback: (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) => void
  ): void
```

订阅壁纸变化通知事件。不支持多线程并发调用。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'wallpaperChange' | 是 |
| callback | (wallpaperType: WallpaperType, resourceType: WallpaperResourceType, uri?: string) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
