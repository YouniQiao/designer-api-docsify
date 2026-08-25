# BusinessError

Defines an error parameter. This API inherits from the **Error** class and is used to pass standard error information, including the error code and optional additional information.

**Inheritance/Implementation:** BusinessError extends Error

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { AsyncCallback, BusinessError, Callback, ErrorCallback } from '@kit.BasicServicesKit';
import { AsyncCallback, BusinessError, Callback, ErrorCallback, RecordData } from '@kit.BasicServicesKit';
```

## constructor

```TypeScript
constructor()
```

Defines a constructor used to create a BusinessError object.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Base

## constructor

```TypeScript
constructor(code: int, error: Error)
```

Defines a constructor used to create a **BusinessError** object.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [code](#code) | int | Yes |
| error | Error | Yes |

## constructor

```TypeScript
constructor(code: int, data: T, error: Error)
```

Defines a constructor used to create a **BusinessError** object.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [code](#code) | int | Yes |
| [data](#data) | T | Yes |
| error | Error | Yes |

## constructor

```TypeScript
constructor(code: int, message: string, data?: T)
```

Defines a constructor used to create a **BusinessError** object.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [code](#code) | int | Yes |
| message | string | Yes |
| [data](#data) | T | No |

## code

```TypeScript
code: number
```

Error code returned when the API fails to be called. The specific error code is defined by each API. For details, see the error code description of the corresponding API.

**Type:** number

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Base

## data

```TypeScript
data?: T
```

Error message returned when the API fails to be called. If this parameter is left empty, the error object does not contain additional data.

**Type:** T

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Base
