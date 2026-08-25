# getId

## 导入模块

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## getId

```TypeScript
function getId(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void
```

获取指定类型壁纸的ID。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## getId

```TypeScript
function getId(wallpaperType: WallpaperType): Promise<number>
```

获取指定类型壁纸的ID。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wallpaperType | [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
