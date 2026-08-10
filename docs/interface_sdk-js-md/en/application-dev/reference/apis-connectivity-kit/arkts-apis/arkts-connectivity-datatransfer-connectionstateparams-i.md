# ConnectionStateParams

获取连接状态所需的参数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-dataTransfer-interface ConnectionStateParams--><!--Device-dataTransfer-interface ConnectionStateParams-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { dataTransfer } from 'kits/@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

连接的设备地址。长度必须为17，由十六进制数字和冒号组成，例如：11:22:33:AA:BB:FF。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParams-address: string--><!--Device-ConnectionStateParams-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## uuid

```TypeScript
uuid: string
```

服务UUID。长度必须为36，由16进制数字字符和连字符共36个字符组成，形如“FFFFFFFF-1234-5678-ABCD-000000001234”，代表128比特标识。&lt;br&gt;禁止使用星闪标准服务UUID。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParams-uuid: string--><!--Device-ConnectionStateParams-uuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

