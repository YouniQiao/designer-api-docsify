# MmsParams (System API)

Defines the parameters for sending SMS messages.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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

MMS PDU address.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## mmsc

```TypeScript
mmsc: string
```

MMSC address.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## mmsConfig

```TypeScript
mmsConfig?: MmsConfig
```

MMS configuration file. For details, see [MmsParams](#mmsparams-system-api).

**Type:** [MmsConfig](arkts-telephony-sms-mmsconfig-i-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## slotId

```TypeScript
slotId: int
```

Slot ID of the SIM card used for sending SMS messages.  
- **0**: card slot 1 - **1**: card slot 2

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.
