# QuickImageDataHandler

媒体资源处理器，应用在onDataPrepared方法中可自定义媒体资源处理逻辑。 > **说明：** > > - 本Interface首批接口从API version 13开始支持。

**起始版本：** 23

<!--Device-photoAccessHelper-interface QuickImageDataHandler--><!--Device-photoAccessHelper-interface QuickImageDataHandler-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
```

## onDataPrepared

```TypeScript
onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void
```

当请求的图片资源准备就绪时，系统会回调媒体资源就绪通知方法。如果资源准备出错，回调的data将为undefined。 map支持返回的信息： | map键名 | 值说明 | |----------|-------| | 'quality' | 图片质量。高质量为'high'，低质量为'low'。 |

**起始版本：** 13

<!--Device-QuickImageDataHandler-onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void--><!--Device-QuickImageDataHandler-onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | T | 是 |
| imageSource | image.ImageSource | 是 |
| map | Map & lt;string, string & gt; | 是 |

## onDataPrepared

```TypeScript
onDataPrepared(data: T | undefined, imageSource: image.ImageSource | null, map: Map<string, string>): void
```

所需的媒体资产数据已快速准备就绪。

**起始版本：** 23

<!--Device-QuickImageDataHandler-onDataPrepared(data: T | undefined, imageSource: image.ImageSource | null, map: Map<string, string>): void--><!--Device-QuickImageDataHandler-onDataPrepared(data: T | undefined, imageSource: image.ImageSource | null, map: Map<string, string>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | T \| undefined | 是 |
| imageSource | image.ImageSource \| null | 是 |
| map | Map & lt;string, string & gt; | 是 |
