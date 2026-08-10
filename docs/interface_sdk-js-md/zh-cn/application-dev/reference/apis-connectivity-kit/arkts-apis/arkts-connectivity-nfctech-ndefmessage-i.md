# NdefMessage

Provides methods for Message of NDEF.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface NdefMessage--><!--Device-unnamed-export interface NdefMessage-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## getNdefRecords

```TypeScript
getNdefRecords(): tag.NdefRecord[]
```

Obtains all records of an NDEF message.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NdefMessage-getNdefRecords(): tag.NdefRecord[]--><!--Device-NdefMessage-getNdefRecords(): tag.NdefRecord[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| tag.NdefRecord[] | Records the list of NDEF records. |

