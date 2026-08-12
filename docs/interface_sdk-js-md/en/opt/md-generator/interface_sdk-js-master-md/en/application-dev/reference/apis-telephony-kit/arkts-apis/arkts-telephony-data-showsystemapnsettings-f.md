# showSystemApnSettings

## Modules to Import

```TypeScript
import { data } from '@kit.TelephonyKit';
```

## showSystemApnSettings

```TypeScript
function showSystemApnSettings(context: Context): Promise<void>
```

Open the system APN selection menu, which is presented in a semi-modal form and can be used to select a specific APN. This API uses a promise to return the result.If there is no SIM card or the device does not support the APN menu, the menu cannot be displayed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-data-function showSystemApnSettings(context: Context): Promise<void>--><!--Device-data-function showSystemApnSettings(context: Context): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
