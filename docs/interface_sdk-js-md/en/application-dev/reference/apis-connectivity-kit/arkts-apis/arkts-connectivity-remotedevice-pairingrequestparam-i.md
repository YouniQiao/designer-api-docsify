# PairingRequestParam

```TypeScript
interface PairingRequestParam
```

Describes pairing request parameters.

**Since:** 26.0.0

<!--Device-remoteDevice-interface PairingRequestParam--><!--Device-remoteDevice-interface PairingRequestParam-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from '@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

Indicates the device address. The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PairingRequestParam-address: string--><!--Device-PairingRequestParam-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## pairingType

```TypeScript
pairingType: PairingType
```

Indicates the pairing type.

**Type:** [PairingType](arkts-connectivity-remotedevice-pairingtype-e.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PairingRequestParam-pairingType: PairingType--><!--Device-PairingRequestParam-pairingType: PairingType-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## passkey

```TypeScript
passkey: string
```

Pass code for device pairing, which is displayed to the user for confirmation. The value is a string of six digits. This parameter is valid only when pairingType is set to PAIRING_TYPE_PASSCODE or PAIRING_TYPE_NUMBER_COMPARE.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PairingRequestParam-passkey: string--><!--Device-PairingRequestParam-passkey: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base
