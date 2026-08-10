# MmsAcknowledgeInd（系统接口）

Defines an MMS confirmation indication.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface MmsAcknowledgeInd--><!--Device-sms-export interface MmsAcknowledgeInd-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## reportAllowed

```TypeScript
reportAllowed?: ReportType
```

Indicates the report allowed for the MMS confirmation indication.

**类型：** [ReportType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-hid-reporttype-e.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAcknowledgeInd-reportAllowed?: ReportType--><!--Device-MmsAcknowledgeInd-reportAllowed?: ReportType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## transactionId

```TypeScript
transactionId: string
```

Indicates the transaction ID for the MMS confirmation indication.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAcknowledgeInd-transactionId: string--><!--Device-MmsAcknowledgeInd-transactionId: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## version

```TypeScript
version: MmsVersionType
```

Indicates the version for the MMS confirmation indication.

**类型：** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAcknowledgeInd-version: MmsVersionType--><!--Device-MmsAcknowledgeInd-version: MmsVersionType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

