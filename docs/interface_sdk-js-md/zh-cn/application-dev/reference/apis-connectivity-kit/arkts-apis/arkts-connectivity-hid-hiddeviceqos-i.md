# HidDeviceQos

Represents the Quality of Service (QoS) settings for a bluetooth hid device application.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-hid-interface HidDeviceQos--><!--Device-hid-interface HidDeviceQos-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { hid } from 'kits/@kit.ConnectivityKit';
```

## delayVariation

```TypeScript
delayVariation?: int
```

L2CAP delay variation, default = -1.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceQos-delayVariation?: int--><!--Device-HidDeviceQos-delayVariation?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## latency

```TypeScript
latency?: int
```

L2CAP latency, default = -1.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceQos-latency?: int--><!--Device-HidDeviceQos-latency?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## peakBandwidth

```TypeScript
peakBandwidth?: int
```

L2CAP peak bandwidth, default = 0.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceQos-peakBandwidth?: int--><!--Device-HidDeviceQos-peakBandwidth?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceType

```TypeScript
serviceType?: ServiceType
```

L2CAP service type, default = SERVICE_BEST_EFFORT.

**类型：** [ServiceType](../../apis-calendar-kit/arkts-apis/arkts-calendar-calendarmanager-servicetype-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceQos-serviceType?: ServiceType--><!--Device-HidDeviceQos-serviceType?: ServiceType-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## tokenBucketSize

```TypeScript
tokenBucketSize?: int
```

L2CAP token bucket size, default = 0.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceQos-tokenBucketSize?: int--><!--Device-HidDeviceQos-tokenBucketSize?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## tokenRate

```TypeScript
tokenRate?: int
```

L2CAP tokenRate, means transmission rate, default = 0.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceQos-tokenRate?: int--><!--Device-HidDeviceQos-tokenRate?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

