# NfcBTag

Provides interfaces to create an {@code NfcBTag} and perform I/O operations on the tag.&lt;p&gt;This class inherits from the {@link TagSession} abstract class and provides interfaces to create an{@code NfcBTag} and obtain the tag information.

**继承/实现关系：** NfcBTag extends [TagSession](arkts-connectivity-tagsession-tagsession-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface NfcBTag extends TagSession--><!--Device-unnamed-export interface NfcBTag extends TagSession-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## getRespAppData

ArkTS-Dyn:
```TypeScript
getRespAppData(): number[]
```

ArkTS-Sta:
```TypeScript
getRespAppData(): int[]
```

Obtains the application data of a tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NfcBTag-getRespAppData(): int[]--><!--Device-NfcBTag-getRespAppData(): int[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | Returns the application data of the tag. |

## getRespProtocol

ArkTS-Dyn:
```TypeScript
getRespProtocol(): number[]
```

ArkTS-Sta:
```TypeScript
getRespProtocol(): int[]
```

Obtains the protocol information of a tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NfcBTag-getRespProtocol(): int[]--><!--Device-NfcBTag-getRespProtocol(): int[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | Returns the protocol information of the tag. |

