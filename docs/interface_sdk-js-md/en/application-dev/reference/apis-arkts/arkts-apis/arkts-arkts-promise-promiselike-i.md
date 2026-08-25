# PromiseLike

Represents a thenable object.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## then

```TypeScript
then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,
        onRejected?: (error: Error) => PromiseLike<E> | E): PromiseLike<Awaited<U | E>>
```

Attaches callbacks for the resolution and/or rejection of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onFulfilled | (value: T) = & gt; PromiseLike & lt;U & gt; \ | U | Yes |
| onRejected | (error: Error) = & gt; PromiseLike & lt;E & gt; \ | E | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| PromiseLike & lt;Awaited & lt;U \ | E & gt; & gt; |
