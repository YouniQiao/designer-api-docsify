# BluetoothScanResult

Describes the contents of the bluetooth scan results.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## connectable

```TypeScript
connectable: boolean
```

Connectable of the scanned device

**Type:** boolean

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Location.Location.Core

## data

```TypeScript
data?: ArrayBuffer
```

The raw data of broadcast packet

**Type:** ArrayBuffer

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Location.Location.Core

## deviceId

```TypeScript
deviceId: string
```

Address of the scanned device

**Type:** string

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Location.Location.Core

## deviceName

```TypeScript
deviceName: string
```

The local name of the scanned device

**Type:** string

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Location.Location.Core

## rssi

```TypeScript
rssi: int
```

RSSI of the scanned device

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Location.Location.Core
