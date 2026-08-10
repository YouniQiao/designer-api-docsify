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

## needReceiveStream

```TypeScript
needReceiveStream?: boolean
```

接收流数据的配置选项。需要开启WiFi。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-needReceiveStream?: boolean--><!--Device-ConnectOptions-needReceiveStream?: boolean-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## needSendStream

```TypeScript
needSendStream?: boolean
```

发送流数据的配置选项。需要开启WiFi。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-needSendStream?: boolean--><!--Device-ConnectOptions-needSendStream?: boolean-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

