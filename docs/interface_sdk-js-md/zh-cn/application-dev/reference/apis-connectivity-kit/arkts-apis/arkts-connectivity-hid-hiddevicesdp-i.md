# HidDeviceSdp

Describe the HID device capability fields of this endpoint being queried.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-hid-interface HidDeviceSdp--><!--Device-hid-interface HidDeviceSdp-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { hid } from 'kits/@kit.ConnectivityKit';
```

## description

```TypeScript
description: string
```

description for this Bluetooth hid device. Maximum length is 50 bytes.

**类型：** string

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceSdp-description: string--><!--Device-HidDeviceSdp-description: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## descriptors

```TypeScript
descriptors: Uint8Array
```

descriptors identifies the descriptors associated with the bluetooth hid device.

**类型：** Uint8Array

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceSdp-descriptors: Uint8Array--><!--Device-HidDeviceSdp-descriptors: Uint8Array-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## name

```TypeScript
name: string
```

name of this Bluetooth hid device. Maximum length is 50 bytes.

**类型：** string

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceSdp-name: string--><!--Device-HidDeviceSdp-name: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## provider

```TypeScript
provider: string
```

provider of this Bluetooth hid device. Maximum length is 50 bytes.

**类型：** string

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceSdp-provider: string--><!--Device-HidDeviceSdp-provider: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## subclass

```TypeScript
subclass: Subclass
```

Subclass of this Bluetooth HID device. Subclass represents the specific HID device type.

**类型：** [Subclass](arkts-connectivity-hid-subclass-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HidDeviceSdp-subclass: Subclass--><!--Device-HidDeviceSdp-subclass: Subclass-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

