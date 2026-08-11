# FinalizationRegistry

## register

```TypeScript
register(target: object, heldValue: T, unregisterToken?: object): void
```

Registers an object with the registry.

<!--Device-FinalizationRegistry-register(target: object, heldValue: T, unregisterToken?: object): void--><!--Device-FinalizationRegistry-register(target: object, heldValue: T, unregisterToken?: object): void-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | object | Yes |
| heldValue | T | Yes |
| unregisterToken | object | No |

## unregister

```TypeScript
unregister(unregisterToken: object): void
```

Unregisters an object from the registry.

<!--Device-FinalizationRegistry-unregister(unregisterToken: object): void--><!--Device-FinalizationRegistry-unregister(unregisterToken: object): void-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| unregisterToken | object | Yes |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "FinalizationRegistry"
```

**Type:** "FinalizationRegistry"
