# Transform

A special duplex stream that supports data conversion and result output. The **Transform** class inherits from [Duplex](arkts-arkts-stream-duplex-c.md) and supports all the APIs in **Duplex**.

**Inheritance/Implementation:** Transform extends [Duplex](arkts-arkts-stream-duplex-c.md)

**Since:** 12

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { stream } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Transform** object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## doFlush

```TypeScript
doFlush(callback: Function): void
```

Called at the end of the stream to process the remaining data. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Function | Yes |

## doTransform

```TypeScript
doTransform(chunk: string, encoding: string, callback: Function): void
```

Converts or processes input data chunks and uses a callback to notify that the processing is complete.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chunk | string | Yes |
| encoding | string | Yes |
| callback | Function | Yes |
