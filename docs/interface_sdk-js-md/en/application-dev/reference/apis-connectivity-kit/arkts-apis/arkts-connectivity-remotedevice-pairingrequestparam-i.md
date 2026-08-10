# PairingRequestParam

配对请求参数说明。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-remoteDevice-interface PairingRequestParam--><!--Device-remoteDevice-interface PairingRequestParam-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from 'kits/@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

设备地址。长度必须为17，由16进制数字和冒号组成，形如 "11:22:33:AA:BB:FF"。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PairingRequestParam-address: string--><!--Device-PairingRequestParam-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## pairingType

```TypeScript
pairingType: PairingType
```

配对类型。

**Type:** [PairingType](arkts-connectivity-remotedevice-pairingtype-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PairingRequestParam-pairingType: PairingType--><!--Device-PairingRequestParam-pairingType: PairingType-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## passkey

```TypeScript
passkey: string
```

设备配对的密钥。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PairingRequestParam-passkey: string--><!--Device-PairingRequestParam-passkey: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

