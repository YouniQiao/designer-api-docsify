# ProxyConstructor

## [[Construct]]

```TypeScript
new <T extends object>(target: T, handler: ProxyHandler<T>): T
```

Creates a Proxy object. The Proxy object allows you to create an object that can be used in place of the original object, but which may redefine fundamental Object operations like getting, setting, and defining properties. Proxy objects are commonly used to log property accesses, validate, format, or sanitize inputs.

<!--Device-ProxyConstructor-new <T extends object>(target: T, handler: ProxyHandler<T>): T--><!--Device-ProxyConstructor-new <T extends object>(target: T, handler: ProxyHandler<T>): T-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | T | Yes |
| handler | ProxyHandler&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## revocable

```TypeScript
revocable<T extends object>(target: T, handler: ProxyHandler<T>): { proxy: T; revoke: () => void; }
```

Creates a revocable Proxy object.

<!--Device-ProxyConstructor-revocable<T extends object>(target: T, handler: ProxyHandler<T>): { proxy: T; revoke: () => void; }--><!--Device-ProxyConstructor-revocable<T extends object>(target: T, handler: ProxyHandler<T>): { proxy: T; revoke: () => void; }-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | T | Yes |
| handler | ProxyHandler&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| { proxy: T; revoke: () =&gt; void; } |
