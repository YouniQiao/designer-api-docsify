# NfcVTag

Provides methods for creating an NFC-V tag, obtaining tag information, and controlling tag read and write.&lt;p&gt;This class inherits from the {@link TagSession} abstract class and provides interfaces to create an{@code NfcVTag} and obtain the tag information.

**继承/实现关系：** NfcVTag extends [TagSession](arkts-connectivity-tagsession-tagsession-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface NfcVTag extends TagSession--><!--Device-unnamed-export interface NfcVTag extends TagSession-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## getDsfId

ArkTS-Dyn:
```TypeScript
getDsfId(): number
```

ArkTS-Sta:
```TypeScript
getDsfId(): int
```

Obtains the response flags from this {@code NfcVTag} instance.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NfcVTag-getDsfId(): int--><!--Device-NfcVTag-getDsfId(): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the response flags. |

## getResponseFlags

ArkTS-Dyn:
```TypeScript
getResponseFlags(): number
```

ArkTS-Sta:
```TypeScript
getResponseFlags(): int
```

Obtains the response flags from this {@code NfcVTag} instance.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NfcVTag-getResponseFlags(): int--><!--Device-NfcVTag-getResponseFlags(): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the response flags. |

