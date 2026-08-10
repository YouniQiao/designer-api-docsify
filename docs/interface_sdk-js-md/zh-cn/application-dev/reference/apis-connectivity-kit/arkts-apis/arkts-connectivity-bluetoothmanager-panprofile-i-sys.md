# PanProfile

Manager pan profile.

**继承/实现关系：** PanProfile extends [BaseProfile](arkts-connectivity-bluetoothmanager-baseprofile-i.md)

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.pan/pan.PanProfile

<!--Device-bluetoothManager-interface PanProfile extends BaseProfile--><!--Device-bluetoothManager-interface PanProfile extends BaseProfile-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## disconnect

```TypeScript
disconnect(device: string): void
```

Disconnect to device with pan.On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.pan/pan.PanProfile#disconnect

**需要权限：** 
- API版本10+：ohos.permission.ACCESS_BLUETOOTH
- API版本9：ohos.permission.USE_BLUETOOTH

<!--Device-PanProfile-disconnect(device: string): void--><!--Device-PanProfile-disconnect(device: string): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | The address of the remote device to disconnect. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900004 | Profile not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## isTetheringOn

```TypeScript
isTetheringOn(): boolean
```

Obtains the tethering enable or disable.On API 10 and above, the permission required by this interface is changed to ACCESS_BLUETOOTH.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.pan/pan.PanProfile#isTetheringOn

**需要权限：** 
- API版本10+：ohos.permission.ACCESS_BLUETOOTH

<!--Device-PanProfile-isTetheringOn(): boolean--><!--Device-PanProfile-isTetheringOn(): boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns the value { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 202 | Non-system applications are not allowed to use system APIs. |

## setTethering

```TypeScript
setTethering(enable: boolean): void
```

Enable bluetooth tethering.On API 10 and above, the permission required by this interface is changed from DISCOVER_BLUETOOTH to ACCESS_BLUETOOTH and MANAGE_BLUETOOTH.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.pan/pan.PanProfile#setTethering

**需要权限：** 
- API版本10+：ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH
- API版本9：ohos.permission.DISCOVER_BLUETOOTH

<!--Device-PanProfile-setTethering(enable: boolean): void--><!--Device-PanProfile-setTethering(enable: boolean): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Specifies whether to enable tethering. The value {@code true} indicates that tethering is enabled, and the value {@code false} indicates that tethering is disabled. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900004 | Profile not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

