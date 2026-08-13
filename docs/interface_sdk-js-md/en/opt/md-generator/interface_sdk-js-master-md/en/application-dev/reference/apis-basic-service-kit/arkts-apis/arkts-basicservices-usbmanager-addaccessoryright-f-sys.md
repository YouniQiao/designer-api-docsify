# addAccessoryRight (System API)

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## addAccessoryRight

```TypeScript
function addAccessoryRight(tokenId: number, accessory: USBAccessory): void
```

Adds the permission to applications for accessing USB accessories. [usbManager.requestAccessoryRight]{(@link usbManager.requestAccessoryRight)} triggers a dialog box to request user authorization. **addAccessoryRight** does not trigger a dialog box but directly adds the device access permission for the application.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function addAccessoryRight(tokenId: int, accessory: USBAccessory): void--><!--Device-usbManager-function addAccessoryRight(tokenId: int, accessory: USBAccessory): void-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenId | number | Yes |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14400005](../../apis-basic-services-kit/errorcode-usb.md#14400005-database-operation-exception) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) |
