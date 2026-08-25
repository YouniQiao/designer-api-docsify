# resourceToSendableResource

## Modules to Import

```TypeScript
import { sendableResourceManager } from 'kits/@kit.LocalizationKit';
```

## resourceToSendableResource

```TypeScript
export function resourceToSendableResource(resource: Resource): SendableResource
```

Converts a `Resource` object to a `SendableResource` object that can be used for cross-thread transmission.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
