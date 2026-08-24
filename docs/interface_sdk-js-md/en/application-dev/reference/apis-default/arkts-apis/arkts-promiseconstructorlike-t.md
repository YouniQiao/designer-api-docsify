# PromiseConstructorLike

```TypeScript
declare type PromiseConstructorLike = new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void) => PromiseLike<T>
```

**Since:** -1

<!--Device-unnamed-declare type PromiseConstructorLike = new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void) => PromiseLike<T>--><!--Device-unnamed-declare type PromiseConstructorLike = new <T>(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason?: any) => void) => void) => PromiseLike<T>-End-->

**Property type:** new&lt;T&gt;(executor: (resolve: (value: T | PromiseLike&lt;T&gt;) =&gt; void, reject: (reason?: any) =&gt; void) =&gt; void) =&gt; PromiseLike&lt;T&gt;

