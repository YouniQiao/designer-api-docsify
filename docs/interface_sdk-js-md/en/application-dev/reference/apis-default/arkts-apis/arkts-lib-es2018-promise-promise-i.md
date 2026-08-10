# Promise

Represents the completion of an asynchronous operation

**ArkTS mode:** ArkTS-Dyn only

<!--Device-unnamed-interface Promise<T>--><!--Device-unnamed-interface Promise<T>-End-->

## finally

```TypeScript
finally(onfinally?: (() => void) | undefined | null): Promise<T>
```

Attaches a callback that is invoked when the Promise is settled (fulfilled or rejected). The resolved value cannot be modified from the callback.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Promise-finally(onfinally?: (() => void) | undefined | null): Promise<T>--><!--Device-Promise-finally(onfinally?: (() => void) | undefined | null): Promise<T>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onfinally | (() =&gt; void) \| undefined \| null | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; |  |

