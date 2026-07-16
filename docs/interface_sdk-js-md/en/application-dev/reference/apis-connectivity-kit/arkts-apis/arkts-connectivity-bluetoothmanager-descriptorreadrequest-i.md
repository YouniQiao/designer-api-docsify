# DescriptorReadRequest

Describes the parameters of the Gatt client's descriptor read request.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** DescriptorReadRequest

<!--Device-bluetoothManager-interface DescriptorReadRequest--><!--Device-bluetoothManager-interface DescriptorReadRequest-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of the characteristic to which the descriptor belongs

**Type:** string

**Since:** 9

**Deprecated since:** 10

**Substitutes:** characteristicUuid

<!--Device-DescriptorReadRequest-characteristicUuid: string--><!--Device-DescriptorReadRequest-characteristicUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## descriptorUuid

```TypeScript
descriptorUuid: string
```

The UUID of a DescriptorReadRequest instance

**Type:** string

**Since:** 9

**Deprecated since:** 10

**Substitutes:** descriptorUuid

<!--Device-DescriptorReadRequest-descriptorUuid: string--><!--Device-DescriptorReadRequest-descriptorUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the address of the client that initiates the read request

**Type:** string

**Since:** 9

**Deprecated since:** 10

**Substitutes:** deviceId

<!--Device-DescriptorReadRequest-deviceId: string--><!--Device-DescriptorReadRequest-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## offset

```TypeScript
offset: number
```

Indicates the byte offset of the start position for reading characteristic value

**Type:** number

**Since:** 9

**Deprecated since:** 10

**Substitutes:** offset

<!--Device-DescriptorReadRequest-offset: number--><!--Device-DescriptorReadRequest-offset: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the descriptor belongs

**Type:** string

**Since:** 9

**Deprecated since:** 10

**Substitutes:** serviceUuid

<!--Device-DescriptorReadRequest-serviceUuid: string--><!--Device-DescriptorReadRequest-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## transId

```TypeScript
transId: number
```

The Id of the read request

**Type:** number

**Since:** 9

**Deprecated since:** 10

**Substitutes:** transId

<!--Device-DescriptorReadRequest-transId: number--><!--Device-DescriptorReadRequest-transId: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

