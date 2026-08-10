# @ohos.FusionConnectivity.partnerAgent

Provides APIs for managing partner agents.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace partnerAgent--><!--Device-unnamed-declare namespace partnerAgent-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## 导入模块

```TypeScript
import { partnerAgent } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [bindDevice](arkts-connectivity-partneragent-binddevice-f.md#binddevice) | Bind the partner device.After successfully binding the device, if the device meets the discovery requirements,the {@link PartnerAgentExtensionAbility} of the application will be launched.  - If the {@link DeviceCapability.supportBR} in the capability variable is set to true,   the application's ability will be launched when the device is connected via Bluetooth.  - If the {@link DeviceCapability.supportBleAdvertiser} in the capability variable is set to true,   the application's ability will be launched when the device is detected via Bluetooth scanning.  Note: The device must be paired first. |
| [getBoundDevices](arkts-connectivity-partneragent-getbounddevices-f.md#getbounddevices) | Gets the list of addresses of the bound partner device for this application. |
| [isDeviceBound](arkts-connectivity-partneragent-isdevicebound-f.md#isdevicebound) | Checks whether a device is bound to this application. |
| [isDeviceControlEnabled](arkts-connectivity-partneragent-isdevicecontrolenabled-f.md#isdevicecontrolenabled) | Checks whether device control is enabled. |
| [isPartnerAgentSupported](arkts-connectivity-partneragent-ispartneragentsupported-f.md#ispartneragentsupported) | Checks whether the current device supports the partner agent feature. |
| [unbindDevice](arkts-connectivity-partneragent-unbinddevice-f.md#unbinddevice) | Unbinds a partner device. |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [disableDeviceControl](arkts-connectivity-partneragent-disabledevicecontrol-f-sys.md#disabledevicecontrol) | Disables device control for a bound device. |
| [enableDeviceControl](arkts-connectivity-partneragent-enabledevicecontrol-f-sys.md#enabledevicecontrol) | Enables device control for a bound device. |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [BusinessCapability](arkts-connectivity-partneragent-businesscapability-i.md) | Describes the business capabilities of the application. |
| [DeviceCapability](arkts-connectivity-partneragent-devicecapability-i.md) | Describes the capability of a partner device. |
| [PartnerDeviceAddress](arkts-connectivity-partneragent-partnerdeviceaddress-i.md) | Describes the partner device address. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [PartnerAgentExtensionAbilityDestroyReason](arkts-connectivity-partneragent-partneragentextensionabilitydestroyreason-e.md) | The enum of reasons for destroying partner agent extension ability. |

