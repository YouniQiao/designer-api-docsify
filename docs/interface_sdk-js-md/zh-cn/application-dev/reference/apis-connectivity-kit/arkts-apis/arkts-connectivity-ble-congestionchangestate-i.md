# CongestionChangeState

```TypeScript
interface CongestionChangeState
```

描述GATT连接的GATT流控拥塞状态。

**起始版本：** 26.1.0

<!--Device-ble-interface CongestionChangeState--><!--Device-ble-interface CongestionChangeState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## congested

```TypeScript
congested: boolean
```

GATT连接是否拥塞。

**类型：** boolean

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CongestionChangeState-congested: boolean--><!--Device-CongestionChangeState-congested: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

对端设备地址。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CongestionChangeState-deviceId: string--><!--Device-CongestionChangeState-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core
