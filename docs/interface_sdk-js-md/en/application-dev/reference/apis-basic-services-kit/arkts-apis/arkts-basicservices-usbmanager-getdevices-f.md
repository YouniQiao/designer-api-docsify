# getDevices

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## getDevices

```TypeScript
function getDevices(): Array<Readonly<USBDevice>>
```

Obtains the list of USB devices connected to the host.

> **NOTE：**&gt;
> Third-party applications are not allowed to obtain the device serial number from the **serial** field unless they
> request permission using [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md)
> and then initiate a control transfer to obtain it.

**Since:** 9

**System capability:** SystemCapability.USB.USBManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Readonly & lt;USBDevice & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
