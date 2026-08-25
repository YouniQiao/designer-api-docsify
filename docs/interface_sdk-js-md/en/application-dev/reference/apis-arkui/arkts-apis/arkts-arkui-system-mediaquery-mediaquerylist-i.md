# MediaQueryList

Represents media query list information.

**Since:** 3

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SystemMediaQuery, MediaQueryEvent, MediaQueryList } from 'kits/@kit.ArkUI';
```

## addListener

```TypeScript
addListener(callback: (event: MediaQueryEvent) => void): void
```

Adds a listener for this **MediaQueryList** object. The listener must be added before **onShow** is called, that is, it must be added in the **onInit** or **onReady** API.

**Since:** 3

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event: MediaQueryEvent) = & gt; void | Yes |

## onchange

```TypeScript
onchange?: (matches: boolean) => void
```

Callback invoked when the match result changes. **matches** indicates whether the media query condition is met. The value **true** means that the query condition is met, and **false** means the opposite.

**Since:** 3

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matches](#matches) | boolean | Yes |

## removeListener

```TypeScript
removeListener(callback: (event: MediaQueryEvent) => void): void
```

Removes the listener for this **MediaQueryList** object.

**Since:** 3

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event: MediaQueryEvent) = & gt; void | Yes |

## matches

```TypeScript
matches?: boolean
```

Matching result. The value **true** means that the query condition is met, and **false** means the opposite.

**Type:** boolean

**Since:** 3

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## media

```TypeScript
media?: string
```

Serialized media query condition.

**Type:** string

**Since:** 3

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
