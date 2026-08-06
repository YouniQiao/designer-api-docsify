# controlTransfer

## controlTransfer

```TypeScript
function controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout?: number): Promise<number>
```

Performs control transfer.

Before you do this, call [usb.getDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to obtain the USB device list, call  
[usb.requestRight]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to request the device access permission, and call  
[usb.connectDevice]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to obtain **devicepipe** as an input parameter.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.controlTransfer](arkts-basicservices-usbmanager-controltransfer-f.md#controltransfer)

<!--Device-usb-function controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout?: number): Promise<number>--><!--Device-usb-function controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout?: number): Promise<number>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | USB device pipe, which is used to determine the USB device. |
| controlparam | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Control transfer parameters. |
| timeout | number | No | Timeout duration in ms. This parameter is optional. The default value is **0**, indicating no timeout. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the result, which is the size of the transmitted or received data block if the transfer is successful, or **-1** if an exception has occurred. |

**Example**

```TypeScript
let param = {
  request: 0,
  reqType: 0,
  target:0,
  value: 0,
  index: 0,
  data: null
};
usb.controlTransfer(devicepipe, param).then((ret) => {
 console.info(`controlTransfer = ${ret}`);
})
```

