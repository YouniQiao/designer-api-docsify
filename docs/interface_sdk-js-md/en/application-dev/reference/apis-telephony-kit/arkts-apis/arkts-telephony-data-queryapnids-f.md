# queryApnIds

## Modules to Import

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## queryApnIds

```TypeScript
function queryApnIds(apnInfo: ApnInfo): Promise<Array<number>>
```

Obtains the APN ID corresponding to the specified **ApnInfo**. This API returns the result asynchronously.

**Since:** 16

**Required permissions:** ohos.permission.MANAGE_APN_SETTING

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| apnInfo | [ApnInfo](arkts-telephony-data-apninfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
