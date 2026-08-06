# QRCode

The **QRCode** component is used to display a QR code.

> **NOTE**
>
> - The pixel count of the **QRCode** component is subject to the content. If the component size is not large enough,
> the content may fail to be displayed. In this case, you need to resize the component.

## Child Components

Not supported

## QRCode

```TypeScript
QRCode(value: ResourceStr)
```

Creates a **QRCode** component. The displayed QR code can be scanned to obtain the encoded string information.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-QRCodeInterface-(value: ResourceStr): QRCodeAttribute--><!--Device-QRCodeInterface-(value: ResourceStr): QRCodeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Content of the QR code. A maximum of 512 characters are supported. If this limit is exceeded, the first 512 characters are used.\_\_\_HTML\_TAG\_USD\_0\_\_\_The Resource type is supported since API version 20.\_\_\_HTML\_TAG\_USD\_1\_\_\_ **NOTE**\_\_\_HTML\_TAG\_USD\_2\_\_\_If this parameter is set to **null**, it is equivalent to passing the string **"null"**. If it is set to **undefined**, it is equivalent to passing the string **"undefined"**. Passing an empty string will result in an invalid QR code. |

## Summary

