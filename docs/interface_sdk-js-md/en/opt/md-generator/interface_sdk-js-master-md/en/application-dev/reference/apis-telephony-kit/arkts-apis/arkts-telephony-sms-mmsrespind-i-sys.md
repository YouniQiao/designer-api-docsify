# MmsRespInd (System API)

Defines an MMS response indication.

**Since:** 8

<!--Device-sms-export interface MmsRespInd--><!--Device-sms-export interface MmsRespInd-End-->

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

Indicates the report allowed for the MMS response indication.

**Type:** [ReportType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-hid-reporttype-e.md)

**Since:** 8

<!--Device-MmsRespInd-reportAllowed?: ReportType--><!--Device-MmsRespInd-reportAllowed?: ReportType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## status

```TypeScript
status: number
```

Indicates the status for the MMS response indication.

**Type:** number

**Since:** 8

<!--Device-MmsRespInd-status: int--><!--Device-MmsRespInd-status: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## transactionId

```TypeScript
transactionId: string
```

Indicates the event ID for the MMS response indication.

**Type:** string

**Since:** 8

<!--Device-MmsRespInd-transactionId: string--><!--Device-MmsRespInd-transactionId: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## version

```TypeScript
version: MmsVersionType
```

Indicates the version for the MMS response indication.

**Type:** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**Since:** 8

<!--Device-MmsRespInd-version: MmsVersionType--><!--Device-MmsRespInd-version: MmsVersionType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.
