# ValueType

```TypeScript
type ValueType = string | image.PixelMap | Want | ArrayBuffer | VirtualFileInfo
```

用于表示允许的数据字段类型。从API 26.1.0开始，支持在[createData](arkts-basicservices-pasteboard-createdata-f.md#createdata-1)、[createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createrecord-1)和[addEntry](arkts-basicservices-pasteboard-pastedatarecord-i.md#addentry)中，使用[VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md)类型。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

<!--Device-pasteboard-type ValueType = string | image.PixelMap | Want | ArrayBuffer | VirtualFileInfo--><!--Device-pasteboard-type ValueType = string | image.PixelMap | Want | ArrayBuffer | VirtualFileInfo-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 类型 | 说明 |
| --- | --- |
| string | 表示string的类型。 |
| [image.PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | 表示[image.PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)的类型。 |
| [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 表示[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)的类型。 |
| ArrayBuffer | 表示ArrayBuffer的类型。 |
| [VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md) | 表示[VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md)的类型。<br>**起始版本：** 26.1.0 |
