# Promise

Represents the completion of an asynchronous operation

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-interface Promise--><!--Device-unnamed-interface Promise-End-->

## finally

```TypeScript
finally(onfinally?: (() => void) | undefined | null): Promise<T>
```

Attaches a callback that is invoked when the Promise is settled (fulfilled or rejected). The resolved value cannot be modified from the callback.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-Promise-finally(onfinally?: (() => void) | undefined | null): Promise<T>--><!--Device-Promise-finally(onfinally?: (() => void) | undefined | null): Promise<T>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onfinally | (() =&gt; void) \| undefined \| null | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; |  |

