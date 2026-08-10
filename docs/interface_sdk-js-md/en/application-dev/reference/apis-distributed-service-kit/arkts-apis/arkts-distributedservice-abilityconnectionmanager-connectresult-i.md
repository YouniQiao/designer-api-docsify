# ConnectResult

连接的结果。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-abilityConnectionManager-interface ConnectResult--><!--Device-abilityConnectionManager-interface ConnectResult-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## errorCode

```TypeScript
errorCode?: ConnectErrorCode
```

表示连接错误码。

**Type:** [ConnectErrorCode](arkts-distributedservice-abilityconnectionmanager-connecterrorcode-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectResult-errorCode?: ConnectErrorCode--><!--Device-ConnectResult-errorCode?: ConnectErrorCode-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## isConnected

```TypeScript
isConnected: boolean
```

true表示连接成功，false表示连接失败。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectResult-isConnected: boolean--><!--Device-ConnectResult-isConnected: boolean-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## reason

```TypeScript
reason?: string
```

表示拒绝连接的原因。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectResult-reason?: string--><!--Device-ConnectResult-reason?: string-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

