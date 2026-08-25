# isChangePermitted

## 导入模块

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## isChangePermitted

```TypeScript
function isChangePermitted(callback: AsyncCallback<boolean>): void
```

是否允许应用改变当前用户的壁纸。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isChangePermitted

```TypeScript
function isChangePermitted(): Promise<boolean>
```

是否允许应用改变当前用户的壁纸。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
