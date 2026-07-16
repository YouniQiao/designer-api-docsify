# DownloadProfileResult (System API)

Result of the given downloadable Profile.

**Since:** 18

<!--Device-eSIM-export interface DownloadProfileResult--><!--Device-eSIM-export interface DownloadProfileResult-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## cardId

```TypeScript
cardId: number
```

Gets the card Id. This value comes from EuiccService and is used when resolving solvable errors.

**Type:** number

**Since:** 18

<!--Device-DownloadProfileResult-cardId: int--><!--Device-DownloadProfileResult-cardId: int-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## responseResult

```TypeScript
responseResult: ResultCode
```

Gets the result of the operation.

**Type:** ResultCode

**Since:** 18

<!--Device-DownloadProfileResult-responseResult: ResultCode--><!--Device-DownloadProfileResult-responseResult: ResultCode-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## solvableErrors

```TypeScript
solvableErrors: SolvableErrors
```

Gets the solvable errors.

**Type:** SolvableErrors

**Since:** 18

<!--Device-DownloadProfileResult-solvableErrors: SolvableErrors--><!--Device-DownloadProfileResult-solvableErrors: SolvableErrors-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

