# createPicture

## createPicture

```TypeScript
function createPicture(mainPixelmap : PixelMap): Picture
```

通过主图的PixelMap创建一个Picture对象。 由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-image-image-picture-i.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-image-function createPicture(mainPixelmap : PixelMap): Picture--><!--Device-image-function createPicture(mainPixelmap : PixelMap): Picture-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mainPixelmap | [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Picture](arkts-image-image-picture-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
async function CreatePicture(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let opts: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, opts);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  if (pictureObj != null) {
    console.info('Succeeded in creating picture');
  } else {
    console.error('Failed to create picture');
  }
}
```
