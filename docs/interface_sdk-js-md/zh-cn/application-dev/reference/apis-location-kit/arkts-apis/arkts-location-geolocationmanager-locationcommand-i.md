# LocationCommand

Location subsystem command structure.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface LocationCommand--><!--Device-geoLocationManager-export interface LocationCommand-End-->

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## command

```TypeScript
command: string
```

Sent command content.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-LocationCommand-command: string--><!--Device-LocationCommand-command: string-End-->

**系统能力：** SystemCapability.Location.Location.Core

## scenario

```TypeScript
scenario: LocationRequestScenario
```

Information about the scenario where the command is sent.

**类型：** [LocationRequestScenario](arkts-location-geolocationmanager-locationrequestscenario-e.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-LocationCommand-scenario: LocationRequestScenario--><!--Device-LocationCommand-scenario: LocationRequestScenario-End-->

**系统能力：** SystemCapability.Location.Location.Core

