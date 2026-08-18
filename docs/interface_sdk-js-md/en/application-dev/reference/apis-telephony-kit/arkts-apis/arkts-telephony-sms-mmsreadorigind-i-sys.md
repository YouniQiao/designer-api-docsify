# MmsReadOrigInd (System API)

Defines the original MMS message reading index.

**Since:** 23

<!--Device-sms-export interface MmsReadOrigInd--><!--Device-sms-export interface MmsReadOrigInd-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## date

```TypeScript
date: long
```

Date.

**Type:** long

**Since:** 23

<!--Device-MmsReadOrigInd-date: long--><!--Device-MmsReadOrigInd-date: long-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## from

```TypeScript
from: MmsAddress
```

Source address.

**Type:** [MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)

**Since:** 23

<!--Device-MmsReadOrigInd-from: MmsAddress--><!--Device-MmsReadOrigInd-from: MmsAddress-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## messageId

```TypeScript
messageId: string
```

Message ID.

**Type:** string

**Since:** 23

<!--Device-MmsReadOrigInd-messageId: string--><!--Device-MmsReadOrigInd-messageId: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## readStatus

```TypeScript
readStatus: int
```

Read status.

**Type:** int

**Since:** 23

<!--Device-MmsReadOrigInd-readStatus: int--><!--Device-MmsReadOrigInd-readStatus: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## to

```TypeScript
to: Array<MmsAddress>
```

Destination address.

**Type:** Array&lt;[MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)&gt;

**Since:** 23

<!--Device-MmsReadOrigInd-to: Array<MmsAddress>--><!--Device-MmsReadOrigInd-to: Array<MmsAddress>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## version

```TypeScript
version: MmsVersionType
```

Version.

**Type:** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**Since:** 23

<!--Device-MmsReadOrigInd-version: MmsVersionType--><!--Device-MmsReadOrigInd-version: MmsVersionType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

