# CharacteristicWriteReq

Describes the parameters of the of the Gatt client's characteristic write request.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** CharacteristicWriteRequest

<!--Device-bluetooth-interface CharacteristicWriteReq--><!--Device-bluetooth-interface CharacteristicWriteReq-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of a CharacteristicWriteReq instance

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicUuid

<!--Device-CharacteristicWriteReq-characteristicUuid: string--><!--Device-CharacteristicWriteReq-characteristicUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the address of the client that initiates the write request

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** deviceId

<!--Device-CharacteristicWriteReq-deviceId: string--><!--Device-CharacteristicWriteReq-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## isPrep

```TypeScript
isPrep: boolean
```

Whether this request should be pending for later operation

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** isPrep

<!--Device-CharacteristicWriteReq-isPrep: boolean--><!--Device-CharacteristicWriteReq-isPrep: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## needRsp

```TypeScript
needRsp: boolean
```

Whether the remote client need a response

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** needRsp

<!--Device-CharacteristicWriteReq-needRsp: boolean--><!--Device-CharacteristicWriteReq-needRsp: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## offset

```TypeScript
offset: number
```

Indicates the byte offset of the start position for writing characteristic value

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** offset

<!--Device-CharacteristicWriteReq-offset: number--><!--Device-CharacteristicWriteReq-offset: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the characteristic belongs

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** serviceUuid

<!--Device-CharacteristicWriteReq-serviceUuid: string--><!--Device-CharacteristicWriteReq-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## transId

```TypeScript
transId: number
```

The Id of the write request

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** transId

<!--Device-CharacteristicWriteReq-transId: number--><!--Device-CharacteristicWriteReq-transId: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## value

```TypeScript
value: ArrayBuffer
```

Indicates the value to be written

**Type:** ArrayBuffer

**Since:** 7

**Deprecated since:** 9

**Substitutes:** value

<!--Device-CharacteristicWriteReq-value: ArrayBuffer--><!--Device-CharacteristicWriteReq-value: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

