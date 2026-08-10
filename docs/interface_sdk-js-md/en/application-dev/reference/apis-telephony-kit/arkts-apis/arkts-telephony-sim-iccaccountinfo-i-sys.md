# IccAccountInfo

Defines the ICC account information.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-sim-export interface IccAccountInfo--><!--Device-sim-export interface IccAccountInfo-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## operatorName

```TypeScript
operatorName?: string
```

表示卡的操作员名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IccAccountInfo-operatorName?: string--><!--Device-IccAccountInfo-operatorName?: string-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## simLabelIndex

```TypeScript
simLabelIndex?: int
```

卡的simLabelIndex。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IccAccountInfo-simLabelIndex?: int--><!--Device-IccAccountInfo-simLabelIndex?: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

