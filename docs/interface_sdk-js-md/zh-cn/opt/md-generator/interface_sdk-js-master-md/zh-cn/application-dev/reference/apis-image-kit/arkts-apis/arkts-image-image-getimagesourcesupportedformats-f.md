# getImageSourceSupportedFormats

## 导入模块

```TypeScript
```

## getImageSourceSupportedFormats

```TypeScript
function getImageSourceSupportedFormats(): string[]
```

获取支持解码的图片格式，图片格式以mime type表示。

**起始版本：** 23

<!--Device-image-function getImageSourceSupportedFormats(): string[]--><!--Device-image-function getImageSourceSupportedFormats(): string[]-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| string[] |

**示例**

```TypeScript
async function GetImageSourceSupportedFormats() {
    let formats = image.getImageSourceSupportedFormats();
    console.info('formats:', formats);
}

async function IsSupportedTiffFormat() {
    let formats = image.getImageSourceSupportedFormats();
    return formats.includes("image/tiff");
}
```
