# DialOptions

Indicates the options of placing a call.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-call-export interface DialOptions--><!--Device-call-export interface DialOptions-End-->

**System capability:** SystemCapability.Telephony.CallManager

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## accountId

```TypeScript
accountId?: int
```

Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-DialOptions-accountId?: int--><!--Device-DialOptions-accountId?: int-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## dialScene

```TypeScript
dialScene?: DialScene
```

Indicates the scenario of the call to be made.

**Type:** [DialScene](arkts-telephony-call-dialscene-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-DialOptions-dialScene?: DialScene--><!--Device-DialOptions-dialScene?: DialScene-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## dialType

```TypeScript
dialType?: DialType
```

Indicates the type of the call to be made.

**Type:** [DialType](arkts-telephony-call-dialtype-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-DialOptions-dialType?: DialType--><!--Device-DialOptions-dialType?: DialType-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## videoState

```TypeScript
videoState?: VideoStateType
```

Indicates the type of Video state.

**Type:** [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-DialOptions-videoState?: VideoStateType--><!--Device-DialOptions-videoState?: VideoStateType-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

