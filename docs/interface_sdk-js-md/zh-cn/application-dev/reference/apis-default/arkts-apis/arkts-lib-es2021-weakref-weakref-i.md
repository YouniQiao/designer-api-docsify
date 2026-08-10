# WeakRef

**ArkTS模式：** 仅支持ArkTS-Dyn

## deref

```TypeScript
deref(): T | undefined
```

Returns the WeakRef instance's target object, or undefined if the target object has been reclaimed.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-WeakRef-deref(): T | undefined--><!--Device-WeakRef-deref(): T | undefined-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "WeakRef"
```

**类型：** "WeakRef"

**ArkTS模式：** 仅支持ArkTS-Dyn

