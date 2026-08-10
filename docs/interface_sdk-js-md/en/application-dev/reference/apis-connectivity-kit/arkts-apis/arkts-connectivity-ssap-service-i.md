# Service

SSAP服务。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-interface Service--><!--Device-ssap-interface Service-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## properties

```TypeScript
properties: Property[]
```

属于此服务的属性。

**Type:** [Property](arkts-connectivity-ssap-property-i.md)[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Service-properties: Property[]--><!--Device-Service-properties: Property[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

服务的UUID。长度必须为36，由16进制数字字符和连字符共36个字符组成，形如“FFFFFFFF-1234-5678-ABCD-000000001234”，代表128比特标识。&lt;br&gt;禁止使用星闪标准服务UUID。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Service-serviceUuid: string--><!--Device-Service-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

