# WeakRef

**ArkTS mode:** ArkTS-Dyn only

<!--Device-unnamed-interface WeakRef<T extends object>--><!--Device-unnamed-interface WeakRef<T extends object>-End-->

## deref

```TypeScript
deref(): T | undefined
```

Returns the WeakRef instance's target object, or undefined if the target object has been reclaimed.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-WeakRef-deref(): T | undefined--><!--Device-WeakRef-deref(): T | undefined-End-->

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "WeakRef"
```

**Type:** "WeakRef"

**ArkTS mode:** ArkTS-Dyn only

<!--Device-WeakRef-readonly [Symbol.toStringTag]: "WeakRef"--><!--Device-WeakRef-readonly [Symbol.toStringTag]: "WeakRef"-End-->

