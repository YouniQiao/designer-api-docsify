# @ohos.bluetooth.hid

Provides methods to accessing bluetooth HID(Human Interface Device)-related capabilities.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace hid--><!--Device-unnamed-declare namespace hid-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { hid } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [createHidDeviceProfile](arkts-connectivity-hid-createhiddeviceprofile-f.md#createhiddeviceprofile) | Creates the instance of HID device profile. |
| [createHidHostProfile](arkts-connectivity-hid-createhidhostprofile-f.md#createhidhostprofile) | create the instance of hid profile. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [GetReportData](arkts-connectivity-hid-getreportdata-i.md) | Describe the GET_REPORT data is received from remote host. |
| [HidDeviceProfile](arkts-connectivity-hid-hiddeviceprofile-i.md) | Manager HID device profile. |
| [HidDeviceQos](arkts-connectivity-hid-hiddeviceqos-i.md) | Represents the Quality of Service (QoS) settings for a bluetooth hid device application. |
| [HidDeviceSdp](arkts-connectivity-hid-hiddevicesdp-i.md) | Describe the HID device capability fields of this endpoint being queried. |
| [InterruptData](arkts-connectivity-hid-interruptdata-i.md) | Describe the interrupt data is received from remote host. |
| [ProtocolData](arkts-connectivity-hid-protocoldata-i.md) | Describe the protocol data is received from remote host. |
| [SetReportData](arkts-connectivity-hid-setreportdata-i.md) | Describe the SET_REPORT data is received from remote host. |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [HidHostProfile](arkts-connectivity-hid-hidhostprofile-i-sys.md) | Manager hid host profile. |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ErrorReason](arkts-connectivity-hid-errorreason-e.md) | Describe the error reason. |
| [ProtocolType](arkts-connectivity-hid-protocoltype-e.md) | Describe the protocol type. |
| [ReportType](arkts-connectivity-hid-reporttype-e.md) | Describe the report type. |
| [ServiceType](arkts-connectivity-hid-servicetype-e.md) | Describe the l2cap service type. |
| [Subclass](arkts-connectivity-hid-subclass-e.md) | Describe the subclass. |

### 类型

| 名称 | 说明 |
| --- | --- |
| [BaseProfile](arkts-connectivity-hid-baseprofile-t.md) | Base interface of profile. |
| [BluetoothAddress](arkts-connectivity-hid-bluetoothaddress-t.md) | Bluetooth device address. |

