# NfcATag

Provides interfaces to control the read and write of tags that support the NFC-A technology.&lt;p&gt;This class is inherited from the {@link TagSession} abstract class, and provides methods to create{@code NfcATag} objects and obtain the ATQA and SAK.

**继承/实现关系：** NfcATag extends [TagSession](arkts-connectivity-tagsession-tagsession-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface NfcATag extends TagSession--><!--Device-unnamed-export interface NfcATag extends TagSession-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## getAtqa

ArkTS-Dyn:
```TypeScript
getAtqa(): number[]
```

ArkTS-Sta:
```TypeScript
getAtqa(): int[]
```

Obtains the ATQA of an NFC-A tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NfcATag-getAtqa(): int[]--><!--Device-NfcATag-getAtqa(): int[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | Returns the ATQA of the NFC-A tag. |

## getSak

ArkTS-Dyn:
```TypeScript
getSak(): number
```

ArkTS-Sta:
```TypeScript
getSak(): int
```

Obtains the SAK of an NFC-A tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NfcATag-getSak(): int--><!--Device-NfcATag-getSak(): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the SAK of the NFC-A tag. |

