# IInputer (System API)

Provides callbacks for credential inputers.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-osAccount-interface IInputer--><!--Device-osAccount-interface IInputer-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## onGetData

```TypeScript
onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void
```

Called to notify the caller that data is obtained.

**Type:** (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-IInputer-onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void--><!--Device-IInputer-onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

