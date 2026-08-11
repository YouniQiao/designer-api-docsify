# WeakRef

## deref

```TypeScript
deref(): T | undefined
```

Returns the WeakRef instance's target object, or undefined if the target object has been reclaimed.

<!--Device-WeakRef-deref(): T | undefined--><!--Device-WeakRef-deref(): T | undefined-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "WeakRef"
```

**Type:** "WeakRef"
