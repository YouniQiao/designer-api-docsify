# NumberMarkInfo（系统接口）

Indicates the mark information of the phone number.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-call-export interface NumberMarkInfo--><!--Device-call-export interface NumberMarkInfo-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## isCloud

```TypeScript
isCloud?: boolean
```

Indicates if this is a number mark from cloud.

**类型：** boolean

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-NumberMarkInfo-isCloud?: boolean--><!--Device-NumberMarkInfo-isCloud?: boolean-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## markContent

```TypeScript
markContent?: string
```

Indicates the content of number mark.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-NumberMarkInfo-markContent?: string--><!--Device-NumberMarkInfo-markContent?: string-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## markCount

```TypeScript
markCount?: int
```

Indicates the count of number mark.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-NumberMarkInfo-markCount?: int--><!--Device-NumberMarkInfo-markCount?: int-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## markDetails

```TypeScript
markDetails?: string
```

Indicates the details of number mark.

**类型：** string

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

<!--Device-NumberMarkInfo-markDetails?: string--><!--Device-NumberMarkInfo-markDetails?: string-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## markSource

```TypeScript
markSource?: string
```

Indicates the source of number mark.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-NumberMarkInfo-markSource?: string--><!--Device-NumberMarkInfo-markSource?: string-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## markType

```TypeScript
markType: MarkType
```

Indicates the type of number mark.

**类型：** [MarkType](arkts-telephony-call-marktype-e-sys.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-NumberMarkInfo-markType: MarkType--><!--Device-NumberMarkInfo-markType: MarkType-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

