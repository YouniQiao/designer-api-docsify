# setAutoTimeStatus (System API)

## Modules to Import

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## setAutoTimeStatus

```TypeScript
function setAutoTimeStatus(status: boolean): Promise<void>
```

Sets the status of the automatic time setting. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.SET_TIME

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13000001](../errorcode-time.md#13000001-network-or-os-error) |
| [204](../../errorcode-universal.md#204-access-denied-by-user-access-control-policy) |
