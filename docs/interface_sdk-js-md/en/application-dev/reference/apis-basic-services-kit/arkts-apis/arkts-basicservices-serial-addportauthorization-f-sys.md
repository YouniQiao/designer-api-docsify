# addPortAuthorization (System API)

## Modules to Import

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## addPortAuthorization

```TypeScript
function addPortAuthorization(tokenId: string, deviceId: string): Promise<void>
```

Adds the permission for applications to access the serial port. This API is open only to system applications that display a pop-up window for serial port authorization.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenId | string | Yes |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [35700001](../errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [35700002](../errorcode-busmanager-serial.md#35700002-parameter-error) |
| [35700008](../errorcode-busmanager-serial.md#35700008-permission-denied) |
