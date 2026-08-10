# ConnectSettings

Describes the settings for Wi-Fi connection.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-wifiManager-interface ConnectSettings--><!--Device-wifiManager-interface ConnectSettings-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## addNetworkToSystem

```TypeScript
addNetworkToSystem?: boolean
```

Whether to add the network to the system for connection.Default is false, if set to true, the network will be added to the system before connection and cannot be retrieved again.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ConnectSettings-addNetworkToSystem?: boolean--><!--Device-ConnectSettings-addNetworkToSystem?: boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## networkId

```TypeScript
networkId: int
```

The ID (uniquely identifies) of a Wi-Fi connection.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ConnectSettings-networkId: int--><!--Device-ConnectSettings-networkId: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## userActionTimeout

```TypeScript
userActionTimeout?: int
```

User action timeout threshold(unit is seconds).The maximum value cannot exceed 30, and default is 10.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ConnectSettings-userActionTimeout?: int--><!--Device-ConnectSettings-userActionTimeout?: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## withUserAction

```TypeScript
withUserAction?: boolean
```

Returned with user action, default value is false.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ConnectSettings-withUserAction?: boolean--><!--Device-ConnectSettings-withUserAction?: boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

