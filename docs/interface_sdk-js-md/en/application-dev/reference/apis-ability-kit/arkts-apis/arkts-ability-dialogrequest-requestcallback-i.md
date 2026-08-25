# RequestCallback

Provides a callback for setting the modal dialog box request result.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { dialogRequest } from 'kits/@kit.AbilityKit';
```

## setRequestResult

```TypeScript
setRequestResult(result: RequestResult): void
```

Sets the result of the request for the modal dialog box.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | [RequestResult](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-requestresult-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
