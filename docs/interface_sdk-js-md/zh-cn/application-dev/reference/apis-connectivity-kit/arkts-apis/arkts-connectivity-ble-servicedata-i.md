# ServiceData

Describes the service data.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ble-interface ServiceData--><!--Device-ble-interface ServiceData-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## serviceUuid

```TypeScript
serviceUuid: string
```

Indicates the UUID of the service data to add

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ServiceData-serviceUuid: string--><!--Device-ServiceData-serviceUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceValue

```TypeScript
serviceValue: ArrayBuffer
```

Indicates the service data to add

**类型：** ArrayBuffer

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ServiceData-serviceValue: ArrayBuffer--><!--Device-ServiceData-serviceValue: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

