# resourceToSendableResource

## Modules to Import

```TypeScript
import { sendableResourceManager } from 'kits/@kit.LocalizationKit';
```

## resourceToSendableResource

```TypeScript
export function resourceToSendableResource(resource: Resource): SendableResource
```

将Resource对象转换为可用于跨线程传输的SendableResource对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-sendableResourceManager-export function resourceToSendableResource(resource: Resource): SendableResource--><!--Device-sendableResourceManager-export function resourceToSendableResource(resource: Resource): SendableResource-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes | Resource对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SendableResource](arkts-localization-sendableresource-sendableresource-i.md) | 转换后的SendableResource对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

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
    let sendableResource: sendableResourceManager.SendableResource = sendableResourceManager.resourceToSendableResource($r('app.string.test'));
} catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error(`resourceToSendableResource failed, error code: ${code}, message: ${message}.`);
}
```

