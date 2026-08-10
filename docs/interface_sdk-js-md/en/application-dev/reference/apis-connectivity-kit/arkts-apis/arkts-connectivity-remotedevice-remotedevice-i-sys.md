# RemoteDevice

远程设备操作方法。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-remoteDevice-interface RemoteDevice--><!--Device-remoteDevice-interface RemoteDevice-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from 'kits/@kit.ConnectivityKit';
```

## cancelDevicePairing

```TypeScript
cancelDevicePairing(): Promise<void>
```

取消正在进行的配对请求。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-cancelDevicePairing(): Promise<void>--><!--Device-RemoteDevice-cancelDevicePairing(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 返回promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

## connect

```TypeScript
connect(): Promise<void>
```

连接所有允许的profile。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-connect(): Promise<void>--><!--Device-RemoteDevice-connect(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 将profile连接结果作为Promise返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

## disconnect

```TypeScript
disconnect(): Promise<void>
```

断开所有已连接的profile。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-disconnect(): Promise<void>--><!--Device-RemoteDevice-disconnect(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 将profile连接结果作为Promise返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

## getDeviceAlias

```TypeScript
getDeviceAlias(): string
```

获取远程设备的别名。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getDeviceAlias(): string--><!--Device-RemoteDevice-getDeviceAlias(): string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回远程设备的别名。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

## getDeviceModel

```TypeScript
getDeviceModel(): DeviceModel
```

获取远端设备的型号信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getDeviceModel(): DeviceModel--><!--Device-RemoteDevice-getDeviceModel(): DeviceModel-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [DeviceModel](arkts-connectivity-remotedevice-devicemodel-i-sys.md) | 返回远程设备的型号信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 202 | Non-system applications are not allowed to use system APIs. |

## getRssiValue

ArkTS-Dyn:
```TypeScript
getRssiValue(): Promise<number>
```

ArkTS-Sta:
```TypeScript
getRssiValue(): Promise<int>
```

获取远程设备的RSSI值。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getRssiValue(): Promise<int>--><!--Device-RemoteDevice-getRssiValue(): Promise<int>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | 返回RSSI值的promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

## removePairedDevice

```TypeScript
removePairedDevice(): Promise<void>
```

删除已配对的远端设备。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-removePairedDevice(): Promise<void>--><!--Device-RemoteDevice-removePairedDevice(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 返回promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

## setConnectionInterval

```TypeScript
setConnectionInterval(interval: ConnectionInterval): void
```

设置与远端设备的连接时间间隔。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-setConnectionInterval(interval: ConnectionInterval): void--><!--Device-RemoteDevice-setConnectionInterval(interval: ConnectionInterval): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| interval | [ConnectionInterval](arkts-connectivity-remotedevice-connectioninterval-t-sys.md) | Yes | 要设置的连接间隔 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

## setDeviceAlias

```TypeScript
setDeviceAlias(alias: string): void
```

设置远端设备的别名。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-setDeviceAlias(alias: string): void--><!--Device-RemoteDevice-setDeviceAlias(alias: string): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alias | string | Yes | 远端设备的别名 &lt;br&gt;最大长度为64且不能为空。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 36100046 | String exceeds maximum length. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

## setPairingConfirmation

```TypeScript
setPairingConfirmation(accept: boolean): void
```

设置配对请求的确认信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-setPairingConfirmation(accept: boolean): void--><!--Device-RemoteDevice-setPairingConfirmation(accept: boolean): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| accept | boolean | Yes | 如果配对请求被接受，则设置为true。否则，设置为false |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

## setPairingPasscode

```TypeScript
setPairingPasscode(passcode: string): Promise<void>
```

如果配对类型为通行码，配对时设置通行码

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-setPairingPasscode(passcode: string): Promise<void>--><!--Device-RemoteDevice-setPairingPasscode(passcode: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| passcode | string | Yes | 用户输入的通行码。必须是6位数字 &lt;br&gt;长度必须为6，6个10以内数字。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 返回promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 36100045 | Passcode must be a 6-digit number. |

## startCrediblePairing

```TypeScript
startCrediblePairing(): Promise<void>
```

发起与可信的远端星闪设备的配对。该接口不触发对话框，不需要用户授权。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-startCrediblePairing(): Promise<void>--><!--Device-RemoteDevice-startCrediblePairing(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 返回promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |

