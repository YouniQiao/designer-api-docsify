# ConnectOptions

应用连接时所需的连接选项。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-abilityConnectionManager-interface ConnectOptions--><!--Device-abilityConnectionManager-interface ConnectOptions-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## needSendData

```TypeScript
needSendData?: boolean
```

true代表需要传输数据，false代表不需要传输数据。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-needSendData?: boolean--><!--Device-ConnectOptions-needSendData?: boolean-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## parameters

```TypeScript
parameters?: Record<string, string>
```

配置连接所需的额外信息。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-parameters?: Record<string, string>--><!--Device-ConnectOptions-parameters?: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## startOptions

```TypeScript
startOptions?: StartOptionParams
```

配置应用启动选项。

**Type:** [StartOptionParams](arkts-distributedservice-abilityconnectionmanager-startoptionparams-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-startOptions?: StartOptionParams--><!--Device-ConnectOptions-startOptions?: StartOptionParams-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

