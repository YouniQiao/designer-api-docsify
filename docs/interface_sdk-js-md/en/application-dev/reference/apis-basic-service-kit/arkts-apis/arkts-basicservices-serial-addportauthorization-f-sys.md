# addPortAuthorization (System API)

## Modules to Import

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## addPortAuthorization

```TypeScript
function addPortAuthorization(tokenId: string, deviceId: string): Promise<void>
```

添加应用访问串口端口的权限仅面向串口授权弹窗系统应用开放

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-serial-function addPortAuthorization(tokenId: string, deviceId: string): Promise<void>--><!--Device-serial-function addPortAuthorization(tokenId: string, deviceId: string): Promise<void>-End-->

**System capability:** SystemCapability.BusManager.Serial

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenId | string | Yes | 被授权应用的tokenId |
| deviceId | string | Yes | 串口设备ID &lt;br&gt;对于板载串口，取值为portName；对于USB虚拟串口，取值为vid+pid+SN拼接。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700002 | Invalid parameter. |
| 35700008 | Permission denied. |
| 202 | Permission denied. Called by non-system application |

