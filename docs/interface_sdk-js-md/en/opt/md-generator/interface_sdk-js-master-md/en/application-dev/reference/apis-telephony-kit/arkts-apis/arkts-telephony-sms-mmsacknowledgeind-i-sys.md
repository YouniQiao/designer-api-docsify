# MmsAcknowledgeInd (System API)

Defines an MMS confirmation indication.

**Since:** 8

<!--Device-sms-export interface MmsAcknowledgeInd--><!--Device-sms-export interface MmsAcknowledgeInd-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## reportAllowed

```TypeScript
reportAllowed?: ReportType
```

Indicates the report allowed for the MMS confirmation indication.

**Type:** [ReportType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-hid-reporttype-e.md)

**Since:** 8

<!--Device-MmsAcknowledgeInd-reportAllowed?: ReportType--><!--Device-MmsAcknowledgeInd-reportAllowed?: ReportType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## transactionId

```TypeScript
transactionId: string
```

Indicates the transaction ID for the MMS confirmation indication.

**Type:** string

**Since:** 8

<!--Device-MmsAcknowledgeInd-transactionId: string--><!--Device-MmsAcknowledgeInd-transactionId: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## version

```TypeScript
version: MmsVersionType
```

Indicates the version for the MMS confirmation indication.

**Type:** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**Since:** 8

<!--Device-MmsAcknowledgeInd-version: MmsVersionType--><!--Device-MmsAcknowledgeInd-version: MmsVersionType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.
