# DeviceSelectCallback (System API)

```TypeScript
type DeviceSelectCallback = (selectPurpose: int) => DeviceSelectResult
```

伴随设备选择回调函数类型。当系统需要用户选择伴随设备时（如添加模板或执行认证），会调用此回调，应用需返回用户选择的设备信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-companionDeviceAuth-type DeviceSelectCallback = (selectPurpose: int) => DeviceSelectResult--><!--Device-companionDeviceAuth-type DeviceSelectCallback = (selectPurpose: int) => DeviceSelectResult-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectPurpose | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 选择目的。用于标识当前设备选择的意图，取值参见[SelectPurpose](arkts-userauthentication-companiondeviceauth-selectpurpose-e-sys.md)。 SELECT_ADD_DEVICE(1)表示选择添加模板的设备，SELECT_AUTH_DEVICE(2)表示选择认证设备。厂商可自定义扩展值（大于等于10000）。应用应根据selectPurpose返回包含对应设备信息 的DeviceSelectResult。 |

**Return value:**

| Type | Description |
| --- | --- |
| [DeviceSelectResult](arkts-userauthentication-companiondeviceauth-deviceselectresult-i-sys.md) | 用于向系统返回用户选择的设备信息，以便系统执行后续的添加模板或认证操作。包含用户选择的设备信息列表（deviceKeys）和可选的扩展上下文（ selectionContext）。 |

