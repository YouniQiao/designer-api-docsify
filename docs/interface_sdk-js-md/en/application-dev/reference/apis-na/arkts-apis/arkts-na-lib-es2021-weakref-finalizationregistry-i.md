# FinalizationRegistry

**Since:** -1

<!--Device-unnamed-interface FinalizationRegistry--><!--Device-unnamed-interface FinalizationRegistry-End-->

## register

```TypeScript
register(target: object, heldValue: T, unregisterToken?: object): void
```

Registers an object with the registry.

**Since:** -1

<!--Device-FinalizationRegistry-register(target: object, heldValue: T, unregisterToken?: object): void--><!--Device-FinalizationRegistry-register(target: object, heldValue: T, unregisterToken?: object): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | object | Yes |  |
| heldValue | T | Yes |  |
| unregisterToken | object | No |  |

## unregister

```TypeScript
unregister(unregisterToken: object): void
```

Unregisters an object from the registry.

**Since:** -1

<!--Device-FinalizationRegistry-unregister(unregisterToken: object): void--><!--Device-FinalizationRegistry-unregister(unregisterToken: object): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unregisterToken | object | Yes |  |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "FinalizationRegistry"
```

**Type:** "FinalizationRegistry"

**Since:** -1

<!--Device-FinalizationRegistry-readonly [Symbol.toStringTag]: "FinalizationRegistry"--><!--Device-FinalizationRegistry-readonly [Symbol.toStringTag]: "FinalizationRegistry"-End-->

