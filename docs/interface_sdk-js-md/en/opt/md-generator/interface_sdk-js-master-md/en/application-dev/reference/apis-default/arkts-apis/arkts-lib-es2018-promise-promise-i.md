# Promise

Represents the completion of an asynchronous operation

<!--Device-unnamed-interface Promise<T>--><!--Device-unnamed-interface Promise<T>-End-->

## finally

```TypeScript
finally(onfinally?: (() => void) | undefined | null): Promise<T>
```

Attaches a callback that is invoked when the Promise is settled (fulfilled or rejected). The resolved value cannot be modified from the callback.

<!--Device-Promise-finally(onfinally?: (() => void) | undefined | null): Promise<T>--><!--Device-Promise-finally(onfinally?: (() => void) | undefined | null): Promise<T>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onfinally | (() = & gt; void) \ | undefined \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |
