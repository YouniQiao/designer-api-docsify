# ValueType

```TypeScript
type ValueType = string | image.PixelMap | Want | ArrayBuffer | VirtualFileInfo
```

Indicates type of value. On API 26.1.0 and above, it can also support using [VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md) in [createData](arkts-basicservices-pasteboard-createdata-f.md#createdata-1), [createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createrecord-1) and [addEntry](arkts-basicservices-pasteboard-pastedatarecord-i.md#addentry).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-pasteboard-type ValueType = string | image.PixelMap | Want | ArrayBuffer | VirtualFileInfo--><!--Device-pasteboard-type ValueType = string | image.PixelMap | Want | ArrayBuffer | VirtualFileInfo-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

| Type | Description |
| --- | --- |
| string | The value is of the string type. |
| [image.PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | The value is of the [image.PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) type. |
| [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | The value is of the [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) type. |
| ArrayBuffer | The value is of the **ArrayBuffer** type. |
| [VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md) | The value is of the [VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md) type.<br>**Since:** 26.1.0 |
