# MmsParams (System API)

Defines the MMS message param.

**Since:** 11

<!--Device-sms-export interface MmsParams--><!--Device-sms-export interface MmsParams-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## data

```TypeScript
data: string
```

Indicates the MMS pdu url used for sending the MMS message.

**Type:** string

**Since:** 11

<!--Device-MmsParams-data: string--><!--Device-MmsParams-data: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## mmsConfig

```TypeScript
mmsConfig?: MmsConfig
```

Indicates the MMS UA and MMS UaProf used for sending the MMS message.

**Type:** MmsConfig

**Since:** 11

<!--Device-MmsParams-mmsConfig?: MmsConfig--><!--Device-MmsParams-mmsConfig?: MmsConfig-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## mmsc

```TypeScript
mmsc: string
```

Indicates the MMSC used for sending the MMS message.

**Type:** string

**Since:** 11

<!--Device-MmsParams-mmsc: string--><!--Device-MmsParams-mmsc: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## slotId

```TypeScript
slotId: number
```

Indicates the ID of the SIM card slot used for sending the MMS message.

**Type:** number

**Since:** 11

<!--Device-MmsParams-slotId: int--><!--Device-MmsParams-slotId: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

