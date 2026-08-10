# AsyncLockCallback

```TypeScript
type AsyncLockCallback<T> = () => T | Promise<T>
```

这是一个补充类型别名，表示lockAsync函数所有重载中的回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-locks-type AsyncLockCallback<T> = () => T | Promise<T>--><!--Device-locks-type AsyncLockCallback<T> = () => T | Promise<T>-End-->

**System capability:** SystemCapability.Utils.Lang

