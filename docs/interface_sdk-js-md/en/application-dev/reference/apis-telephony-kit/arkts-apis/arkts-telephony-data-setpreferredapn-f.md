# setPreferredApn

## Modules to Import

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## setPreferredApn

```TypeScript
function setPreferredApn(apnId: number): Promise<boolean>
```

Sets the APN corresponding to the specified **apnId** as the preferred APN. This API returns the result asynchronously.

> **NOTE：**&gt;
> If the input APN ID is invalid, the default preferred APN configured by the carrier is used.

**Since:** 16

**Required permissions:** ohos.permission.MANAGE_APN_SETTING

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| apnId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
