# sendableResourceToResource

## Modules to Import

```TypeScript
import { sendableResourceManager } from '@kit.LocalizationKit';
```

## sendableResourceToResource

```TypeScript
export function sendableResourceToResource(resource: SendableResource): Resource
```

Converts a `SendableResource` object transmitted across threads to a `Resource` object.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-sendableResourceManager-export function sendableResourceToResource(resource: SendableResource): Resource--><!--Device-sendableResourceManager-export function sendableResourceToResource(resource: SendableResource): Resource-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [SendableResource](arkts-localization-sendableresource-sendableresource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Resource](arkts-localization-resource-resource-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
// Resource file path: src/main/resources/base/element/string.json
{
  "string": [
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  ]
}
```

```TypeScript
import { sendableResourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let resource: sendableResourceManager.Resource = sendableResourceManager.sendableResourceToResource(sendableResourceManager.resourceToSendableResource($r('app.string.test')));
} catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error(`sendableResourceToResource failed, error code: ${code}, message: ${message}.`);
}
```
