# ProxyConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## [[Construct]]

```TypeScript
new <T extends object>(target: T, handler: ProxyHandler<T>): T
```

Creates a Proxy object. The Proxy object allows you to create an object that can be used in place of the original object, but which may redefine fundamental Object operations like getting, setting, and defining properties. Proxy objects are commonly used to log property accesses, validate, format, or sanitize inputs.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ProxyConstructor-new <T extends object>(target: T, handler: ProxyHandler<T>): T--><!--Device-ProxyConstructor-new <T extends object>(target: T, handler: ProxyHandler<T>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | T | 是 |  |
| handler | ProxyHandler&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## revocable

```TypeScript
revocable<T extends object>(target: T, handler: ProxyHandler<T>): { proxy: T; revoke: () => void; }
```

Creates a revocable Proxy object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ProxyConstructor-revocable<T extends object>(target: T, handler: ProxyHandler<T>): { proxy: T; revoke: () => void; }--><!--Device-ProxyConstructor-revocable<T extends object>(target: T, handler: ProxyHandler<T>): { proxy: T; revoke: () => void; }-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | T | 是 |  |
| handler | ProxyHandler&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| { proxy: T; revoke: () =&gt; void; } |  |

