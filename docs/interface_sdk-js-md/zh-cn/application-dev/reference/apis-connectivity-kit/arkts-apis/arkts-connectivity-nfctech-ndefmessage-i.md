# NdefMessage

**起始版本：** 23

<!--Device-unnamed-export interface NdefMessage--><!--Device-unnamed-export interface NdefMessage-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## getNdefRecords

```TypeScript
getNdefRecords(): tag.NdefRecord[]
```

获取NDEF消息中的所有记录。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NdefMessage-getNdefRecords(): tag.NdefRecord[]--><!--Device-NdefMessage-getNdefRecords(): tag.NdefRecord[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| tag.NdefRecord[] | NDEF标签的Record列表，详见NDEF技术规范《NFCForum-TS-NDEF_1.0》。 |

