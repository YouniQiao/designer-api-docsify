# URI

URI Represents a Uniform Resource Identifier (URI) reference.

**Since:** 8

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { uri } from 'kits/@kit.ArkTS';
```

## addEncodedSegment

```TypeScript
addEncodedSegment(pathSegment: string): URI
```

Appends an encoded field to the path component of this URI to create a new URI and returns the new URI, while keeping the existing URI unchanged.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathSegment | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## addQueryValue

```TypeScript
addQueryValue(key: string, value: string): URI
```

Adds a query parameter to this URI to create a new URI, while keeping the existing URI unchanged.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## addSegment

```TypeScript
addSegment(pathSegment: string): URI
```

Encodes a given field, appends it to the path component of this URI to create a new URI, and returns the new URI, while keeping the existing URI unchanged.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathSegment | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## checkHierarchical

```TypeScript
checkHierarchical(): boolean
```

Checks whether this URI is a hierarchical URI. The URI that starts with a slash (/) in scheme-specific-part is a hierarchical URI. Relative URIs are also hierarchical.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## checkIsAbsolute

```TypeScript
checkIsAbsolute(): boolean
```

Checks whether this URI is an absolute URI (whether the scheme component is defined).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## checkOpaque

```TypeScript
checkOpaque(): boolean
```

Checks whether this URI is an opaque URI. The URI that does not start with a slash (/) is an opaque URI.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## checkRelative

```TypeScript
checkRelative(): boolean
```

Determine whether URI is Relative.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## clearQuery

```TypeScript
clearQuery(): URI
```

Clears the query component of this URI to create a new URI, while keeping the existing URI object unchanged.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## constructor

```TypeScript
constructor(uri: string)
```

A constructor used to create a URI instance.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [uri](arkts-uri.md) | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-parameter-parsing-error) |

## createFromParts

```TypeScript
static createFromParts(scheme: string, ssp: string, fragment: string): URI
```

Creates a URI based on the provided scheme, scheme-specific-part, and fragment components.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [scheme](#scheme) | string | Yes |
| [ssp](arkts-arkts-uri-uri-c.md) | string | Yes |
| [fragment](arkts-arkts-uri-uri-c.md) | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## equals

```TypeScript
equals(other: URI): boolean
```

Check whether this URI is equivalent to other URI objects.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [equalsTo](#equalsto)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [URI](arkts-arkts-uri-uri-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## equalsTo

```TypeScript
equalsTo(other: URI): boolean
```

Checks whether this URI is the same as another URI object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [URI](arkts-arkts-uri-uri-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getBooleanQueryValue

```TypeScript
getBooleanQueryValue(key: string, defaultValue: boolean): boolean
```

Obtains the value of the Boolean type of a query parameter in this URI.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| defaultValue | boolean | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getLastSegment

```TypeScript
getLastSegment(): string
```

Obtains the last segment of this URI.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## getQueryNames

```TypeScript
getQueryNames(): string[]
```

Obtains all non-repeated keys in the query component of this URI.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string[] |

## getQueryValue

```TypeScript
getQueryValue(key: string): string
```

Obtains the first value of a given key from the query component of this URI. If the query component contains encoded content, this API decodes the key before obtaining the value.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## getQueryValues

```TypeScript
getQueryValues(key: string): string[]
```

Obtains the values of a given key from the query component of this URI.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string[] |

## getSegment

```TypeScript
getSegment(): string[]
```

Gets the decoded path segments.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string[] |

## normalize

```TypeScript
normalize(): URI
```

Normalizes the path of this URI.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [URI](arkts-arkts-uri-uri-c.md) |

## toString

```TypeScript
toString(): string
```

Converts this URI into an encoded string.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## authority

```TypeScript
authority: string
```

Gets/Sets the decoding permission component part of this URI.

**Type:** string

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## encodedAuthority

```TypeScript
encodedAuthority: string
```

Gets/Sets the encoded authority part of this URI.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## encodedFragment

```TypeScript
encodedFragment: string
```

Gets/Sets the encoded fragment part of this URI, everything after the '#'.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## encodedPath

```TypeScript
encodedPath: string
```

Gets/Sets the encoded path portion of the URI.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## encodedQuery

```TypeScript
encodedQuery: string
```

Gets/Sets the encoded query component from this URI.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## encodedSSP

```TypeScript
encodedSSP: string
```

Gets/Sets the scheme-specific part of this URI, i.e. everything between the scheme separator ':' and the fragment separator '#'.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## encodedUserInfo

```TypeScript
encodedUserInfo: string
```

Gets/Sets Obtains the encoded user information part of the URI.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## fragment

```TypeScript
fragment: string
```

Gets/Sets the fragment part of the URI.

**Type:** string

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## host

```TypeScript
host: string
```

Gets the hostname portion of the URI without a port.

**Type:** string

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## path

```TypeScript
path: string
```

Gets/Sets the path portion of the URI.

**Type:** string

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## port

```TypeScript
port: string
```

Gets the port portion of the URI.

**Type:** string

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## query

```TypeScript
query: string
```

Gets/Sets the query portion of the URI

**Type:** string

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## scheme

```TypeScript
scheme: string
```

Gets/Sets the protocol part of the URI.

**Type:** string

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## ssp

```TypeScript
ssp: string
```

Gets/Sets the decoding scheme-specific part of the URI.

**Type:** string

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## userInfo

```TypeScript
userInfo: string
```

Gets/Sets Obtains the user information part of the URI.

**Type:** string

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang
