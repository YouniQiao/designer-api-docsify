# URL

The interface of URL is used to parse, construct, normalize, and encode URLs.

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { url } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(url: string, base?: string | URL)
```

URL constructor, which is used to instantiate a URL object. url: Absolute or relative input URL to resolve. Base is required if input is relative. If input is an absolute value, base ignores the value. base: Base URL to parse if input is not absolute.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [parseURL](#parseurl)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [url](arkts-url.md) | string | Yes |
| base | string \| URL | No |

## constructor

```TypeScript
constructor()
```

A no-argument constructor used to create a URL. It returns a URL object after parseURL is called. It is not used independently.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## parseURL

```TypeScript
static parseURL(url: string, base?: string | URL): URL
```

Parses a URL.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [url](arkts-url.md) | string | Yes |
| base | string \| URL | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| URL |

**Error codes:**

| Error Code ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-parameter-parsing-error) |

## toJSON

```TypeScript
toJSON(): string
```

Converts the parsed URL into a JSON string.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toString

```TypeScript
toString(): string
```

Converts the parsed URL into a string.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## hash

```TypeScript
hash: string
```

Gets and sets the fragment portion of the URL.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## host

```TypeScript
host: string
```

Gets and sets the host portion of the URL.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## hostname

```TypeScript
hostname: string
```

Gets and sets the host name portion of the URL，not include the port.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## href

```TypeScript
href: string
```

Gets and sets the serialized URL.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## origin

```TypeScript
readonly origin: string
```

Gets the read-only serialization of the URL's origin.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## params

```TypeScript
readonly params: URLParams
```

Gets the URLParams object that represents the URL query parameter. This property is read-only, but URLParams provides an object that can be used to change the URL instance. To replace the entire query parameter for a URL, use url.searchsetter.

**Type:** [URLParams](arkts-arkts-url-urlparams-c.md)

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## password

```TypeScript
password: string
```

Gets and sets the password portion of the URL.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## pathname

```TypeScript
pathname: string
```

Gets and sets the path portion of the URL.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## port

```TypeScript
port: string
```

Gets and sets the port portion of the URL.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## protocol

```TypeScript
protocol: string
```

Gets and sets the protocol portion of the URL.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## search

```TypeScript
search: string
```

Gets and sets the serialized query portion of the URL.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## searchParams

```TypeScript
readonly searchParams: URLSearchParams
```

Gets the URLSearchParams object that represents the URL query parameter. This property is read-only, but URLSearchParams provides an object that can be used to change the URL instance. To replace the entire query parameter for a URL, use url.searchsetter.

**Type:** URLSearchParams

**Since:** 7

**Deprecated since:** 9

**Substitutes:** params

**System capability:** SystemCapability.Utils.Lang

## username

```TypeScript
username: string
```

Gets and sets the username portion of the URL.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang
