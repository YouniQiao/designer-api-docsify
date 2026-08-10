# ConnectSettings

Describes the settings for Wi-Fi connection.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-wifiManager-interface ConnectSettings--><!--Device-wifiManager-interface ConnectSettings-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## addNetworkToSystem

```TypeScript
addNetworkToSystem?: boolean
```

Whether to add the network to the system for connection.Default is false, if set to true, the network will be added to the system before connection and cannot be retrieved again.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ConnectSettings-addNetworkToSystem?: boolean--><!--Device-ConnectSettings-addNetworkToSystem?: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## networkId

```TypeScript
networkId: int
```

The ID (uniquely identifies) of a Wi-Fi connection.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ConnectSettings-networkId: int--><!--Device-ConnectSettings-networkId: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## userActionTimeout

```TypeScript
userActionTimeout?: int
```

User action timeout threshold(unit is seconds).The maximum value cannot exceed 30, and default is 10.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ConnectSettings-userActionTimeout?: int--><!--Device-ConnectSettings-userActionTimeout?: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## withUserAction

```TypeScript
withUserAction?: boolean
```

Returned with user action, default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ConnectSettings-withUserAction?: boolean--><!--Device-ConnectSettings-withUserAction?: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

