# off

## 导入模块

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## off('colorChange')

```TypeScript
function off(type: 'colorChange', callback?: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void
```

取消订阅壁纸颜色变化结果上报事件。不支持多线程并发调用。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'colorChange' | 是 |
| callback | (colors: Array&lt;[RgbaColor](arkts-basicservices-wallpaper-rgbacolor-i.md)&gt;, wallpaperType: WallpaperType) =&gt; void | 否 |
