# Callback

Defines a common callback used to return the processing result when an asynchronous operation is successful. You need to define the callback type.

**Since:** 6

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { AsyncCallback, BusinessError, Callback, ErrorCallback } from 'kits/@kit.BasicServicesKit';
import { AsyncCallback, BusinessError, Callback, ErrorCallback, RecordData } from 'kits/@kit.BasicServicesKit';
```

## [[Call]]

```TypeScript
(data: T): void
```

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | T | Yes |
