# isAppKioskAllowed

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## isAppKioskAllowed

```TypeScript
function isAppKioskAllowed(appIdentifier: string): boolean
```

Checks whether an application is allowed to run in kiosk mode.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function isAppKioskAllowed(appIdentifier: string): boolean--><!--Device-applicationManager-function isAppKioskAllowed(appIdentifier: string): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appIdentifier | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { applicationManager } from '@kit.MDMKit';

try {
  // Replace it as required.
  let isAllowed: boolean = applicationManager.isAppKioskAllowed('6917****3569');
  console.info(`Succeeded in querying if the app is allowed kiosk, isAllowed: ${isAllowed}`);
} catch (err) {
  console.error(`Failed to query if the app is allowed kiosk. Code is ${err.code}, message is ${err.message}`);
}
```
