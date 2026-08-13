# CharacteristicReadReq

Describes the parameters of the Gatt client's characteristic read request.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [CharacteristicReadRequest](arkts-connectivity-bluetoothmanager-characteristicreadrequest-i.md#CharacteristicReadRequest)

<!--Device-bluetooth-interface CharacteristicReadReq--><!--Device-bluetooth-interface CharacteristicReadReq-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of a CharacteristicReadReq instance

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [characteristicUuid](arkts-connectivity-bluetoothmanager-characteristicreadrequest-i.md#characteristicUuid)

<!--Device-CharacteristicReadReq-characteristicUuid: string--><!--Device-CharacteristicReadReq-characteristicUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the address of the client that initiates the read request

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [deviceId](arkts-connectivity-bluetoothmanager-characteristicreadrequest-i.md#deviceId)

<!--Device-CharacteristicReadReq-deviceId: string--><!--Device-CharacteristicReadReq-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## offset

```TypeScript
offset: number
```

Indicates the byte offset of the start position for reading characteristic value

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [offset](arkts-connectivity-bluetoothmanager-characteristicreadrequest-i.md#offset)

<!--Device-CharacteristicReadReq-offset: number--><!--Device-CharacteristicReadReq-offset: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the characteristic belongs

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [serviceUuid](arkts-connectivity-bluetoothmanager-characteristicreadrequest-i.md#serviceUuid)

<!--Device-CharacteristicReadReq-serviceUuid: string--><!--Device-CharacteristicReadReq-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## transId

```TypeScript
transId: number
```

The Id of the read request

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [transId](arkts-connectivity-bluetoothmanager-characteristicreadrequest-i.md#transId)

<!--Device-CharacteristicReadReq-transId: number--><!--Device-CharacteristicReadReq-transId: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

