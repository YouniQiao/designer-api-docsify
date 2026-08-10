# BarcodeTag

Provides methods for accessing Barcode tag.

**继承/实现关系：** BarcodeTag extends [TagSession](arkts-connectivity-tagsession-tagsession-i.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface BarcodeTag extends TagSession--><!--Device-unnamed-export interface BarcodeTag extends TagSession-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## getBarcode

```TypeScript
getBarcode(): Promise<ArrayBuffer>
```

Returns the barcode of a Barcode tag.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-BarcodeTag-getBarcode(): Promise<ArrayBuffer>--><!--Device-BarcodeTag-getBarcode(): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | The barcode of tag. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

