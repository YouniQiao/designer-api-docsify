# getMinWidth

## 导入模块

```TypeScript
import { wallpaper } from '@kit.BasicServicesKit';
```

## getMinWidth

```TypeScript
function getMinWidth(callback: AsyncCallback<number>): void
```

获取壁纸的最小宽度值。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**系统能力：** SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth((error: BusinessError, data: number) => {
    if (error) {
        console.error(`Failed to getMinWidth. Code: ${error.code}, message: ${error.message}`);
        return;
    }
    console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth().then((data: number) => {
    console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to getMinWidth. Code: ${error.code}, message: ${error.message}`);
});
```


## getMinWidth

```TypeScript
function getMinWidth(): Promise<number>
```

获取壁纸的最小宽度值。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**系统能力：** SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**示例**

参见 [getMinWidth](#getminwidth)
