# ErrorCallback(Public Callback Information)

Defines a common callback that carries an error parameter. It is used to return error information when an asynchronous operation fails. The specific error code is defined by each API. For details, please refer to the error code description of the corresponding API. The information returned by the callback is an error parameter of the [BusinessError](arkts-basicservices-base-businesserror-i.md#businesserror) type.

**Since:** 6

<!--Device-unnamed-export interface ErrorCallback--><!--Device-unnamed-export interface ErrorCallback-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { AsyncCallback, BusinessError, Callback, ErrorCallback } from '@kit.BasicServicesKit';
import { AsyncCallback, BusinessError, Callback, ErrorCallback, RecordData } from '@kit.BasicServicesKit';
```

## constructor

```TypeScript
(err: T): void
```

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorCallback-(err: T): void--><!--Device-ErrorCallback-(err: T): void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | T | Yes | Common error information returned when the API fails to be called. The default type is **BusinessError**, including the error code (**code**) and optional additional data (**data**). |

