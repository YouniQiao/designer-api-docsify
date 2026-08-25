# setValue (System API)

## Modules to Import

```TypeScript
import { brightness } from 'kits/@kit.BasicServicesKit';
```

## setValue

```TypeScript
function setValue(value: number): void
```

Sets the screen brightness.

**Since:** 7

**System capability:** SystemCapability.PowerManager.DisplayPowerManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [4700101](../errorcode-brightness.md#4700101-service-connection-failure) |


## setValue

```TypeScript
function setValue(value: number, continuous: boolean): void
```

Sets the screen brightness. This API is used for continuous brightness adjustment. To achieve a better performance, set **continuous** to **true** when you start, and set it to **false** after you finish.

**Since:** 11

**System capability:** SystemCapability.PowerManager.DisplayPowerManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| continuous | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [4700101](../errorcode-brightness.md#4700101-service-connection-failure) |
