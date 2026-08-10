# hasRight

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## hasRight

```TypeScript
function hasRight(deviceName: string): boolean
```

判断是否有权访问该设备。如果“使用者”（如各种App或系统）有权访问设备则返回true；无权访问设备则返回false。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usbManager-function hasRight(deviceName: string): boolean--><!--Device-usbManager-function hasRight(deviceName: string): boolean-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceName | string | Yes | 设备名称，来自[usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getdevices)获取的设备列表USBDevice的name。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示有访问设备的权限，false表示没有访问设备的权限。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes:  &lt;br&gt;1.Mandatory parameters are left unspecified.  &lt;br&gt;2.Incorrect parameter types. |
| 801 | Capability not supported.<br>**Applicable version:** 18 and later |

## Examples

```TypeScript
function hasRight(): boolean {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return false;
  }

  let device: usbManager.USBDevice = devicesList?.[0];
  usbManager.requestRight(device.name);
  let right: boolean = usbManager.hasRight(device.name);
  console.info(`${right}`);
  return right;
}
```

