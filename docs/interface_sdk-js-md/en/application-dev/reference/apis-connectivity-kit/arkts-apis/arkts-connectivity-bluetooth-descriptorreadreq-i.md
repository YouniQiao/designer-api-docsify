# DescriptorReadReq

Describes the parameters of the Gatt client's descriptor read request.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** DescriptorReadRequest

<!--Device-bluetooth-interface DescriptorReadReq--><!--Device-bluetooth-interface DescriptorReadReq-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of the characteristic to which the descriptor belongs

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicUuid

<!--Device-DescriptorReadReq-characteristicUuid: string--><!--Device-DescriptorReadReq-characteristicUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## descriptorUuid

```TypeScript
descriptorUuid: string
```

The UUID of a DescriptorReadReq instance

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** descriptorUuid

<!--Device-DescriptorReadReq-descriptorUuid: string--><!--Device-DescriptorReadReq-descriptorUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the address of the client that initiates the read request

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** deviceId

<!--Device-DescriptorReadReq-deviceId: string--><!--Device-DescriptorReadReq-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## offset

```TypeScript
offset: number
```

Indicates the byte offset of the start position for reading characteristic value

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** offset

<!--Device-DescriptorReadReq-offset: number--><!--Device-DescriptorReadReq-offset: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the descriptor belongs

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** serviceUuid

<!--Device-DescriptorReadReq-serviceUuid: string--><!--Device-DescriptorReadReq-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## transId

```TypeScript
transId: number
```

The Id of the read request

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** transId

<!--Device-DescriptorReadReq-transId: number--><!--Device-DescriptorReadReq-transId: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

