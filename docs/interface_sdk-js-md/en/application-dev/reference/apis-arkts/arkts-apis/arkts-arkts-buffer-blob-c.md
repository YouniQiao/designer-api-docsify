# Blob

Process data as blob type

**Since:** 9

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## arrayBuffer

```TypeScript
arrayBuffer(): Promise<ArrayBuffer>
```

Puts the **Blob** data into an **ArrayBuffer** object. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## constructor

```TypeScript
constructor(sources: string[] | ArrayBuffer[] | TypedArray[] | DataView[] | Blob[], options?: Object)
```

A constructor used to create a **Blob** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sources | string[] \| ArrayBuffer[] \| TypedArray[] \| DataView[] \| [Blob](arkts-arkts-buffer-blob-c.md)[] | Yes |
| options | Object | No |

## slice

```TypeScript
slice(start?: number, end?: number, type?: string): Blob
```

Creates and returns a **Blob** object that contains specified data from this **Blob** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |
| [type](#type) | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Blob](arkts-arkts-buffer-blob-c.md) |

## text

```TypeScript
text(): Promise<string>
```

Decodes data using UTF-8 and returns a string. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## size

```TypeScript
get size(): number
```

Total size of the Blob instance, in bytes.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## type

```TypeScript
get type(): string
```

Type of the data in the Blob instance.

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang
