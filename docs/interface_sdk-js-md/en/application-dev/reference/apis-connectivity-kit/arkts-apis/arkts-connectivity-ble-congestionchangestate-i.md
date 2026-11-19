# CongestionChangeState

```TypeScript
interface CongestionChangeState
```

Describes the GATT flow control congestion state of a GATT connection.

**Since:** 26.1.0

<!--Device-ble-interface CongestionChangeState--><!--Device-ble-interface CongestionChangeState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## congested

```TypeScript
congested: boolean
```

Indicates whether the GATT connection is congested.

**Type:** boolean

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CongestionChangeState-congested: boolean--><!--Device-CongestionChangeState-congested: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the peer device address.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CongestionChangeState-deviceId: string--><!--Device-CongestionChangeState-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core
