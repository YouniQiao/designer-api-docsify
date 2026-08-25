# ErrorCallback

Defines a common callback that carries an error parameter. It is used to return error information when an asynchronous operation fails. The specific error code is defined by each API. For details, please refer to the error code description of the corresponding API.The information returned by the callback is an error parameter of the [BusinessError](arkts-basicservices-base-businesserror-i.md) type.

**Since:** 6

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { AsyncCallback, BusinessError, Callback, ErrorCallback } from 'kits/@kit.BasicServicesKit';
import { AsyncCallback, BusinessError, Callback, ErrorCallback, RecordData } from 'kits/@kit.BasicServicesKit';
```

## [[Call]]

```TypeScript
(err: T): void
```

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| err | T | Yes |
