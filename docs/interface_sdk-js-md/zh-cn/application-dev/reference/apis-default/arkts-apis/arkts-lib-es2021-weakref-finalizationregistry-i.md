# FinalizationRegistry

**ArkTS模式：** 仅支持ArkTS-Dyn

## register

```TypeScript
register(target: object, heldValue: T, unregisterToken?: object): void
```

Registers an object with the registry.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-FinalizationRegistry-register(target: object, heldValue: T, unregisterToken?: object): void--><!--Device-FinalizationRegistry-register(target: object, heldValue: T, unregisterToken?: object): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | object | 是 |  |
| heldValue | T | 是 |  |
| unregisterToken | object | 否 |  |

## unregister

```TypeScript
unregister(unregisterToken: object): void
```

Unregisters an object from the registry.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-FinalizationRegistry-unregister(unregisterToken: object): void--><!--Device-FinalizationRegistry-unregister(unregisterToken: object): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unregisterToken | object | 是 |  |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "FinalizationRegistry"
```

**类型：** "FinalizationRegistry"

**ArkTS模式：** 仅支持ArkTS-Dyn

