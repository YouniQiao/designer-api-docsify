# getMinWidth

## 导入模块

```TypeScript
```

## getMinWidth

```TypeScript
function getMinWidth(callback: AsyncCallback<number>): void
```

获取壁纸的最小宽度值。

**起始版本：** 7

**废弃版本：** 9

<!--Device-wallpaper-function getMinWidth(callback: AsyncCallback<number>): void--><!--Device-wallpaper-function getMinWidth(callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth((error: BusinessError, data: Number) => {
    if (error) {
        console.error(`failed to getMinWidth because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
});
```


## getMinWidth

```TypeScript
function getMinWidth(): Promise<number>
```

获取壁纸的最小宽度值。

**起始版本：** 7

**废弃版本：** 9

<!--Device-wallpaper-function getMinWidth(): Promise<number>--><!--Device-wallpaper-function getMinWidth(): Promise<number>-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth().then((data: Number) => {
    console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to getMinWidth because: ${JSON.stringify(error)}`);
});
```
