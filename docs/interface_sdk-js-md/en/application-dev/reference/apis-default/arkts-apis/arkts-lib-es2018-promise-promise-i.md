# Promise

Represents the completion of an asynchronous operation

## Modules to Import

```TypeScript
```

## finally

```TypeScript
finally(onfinally?: (() => void) | undefined | null): Promise<T>
```

Attaches a callback that is invoked when the Promise is settled (fulfilled or rejected). The resolved value cannot be modified from the callback.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onfinally | (() =&gt; void) \| undefined \| null | No |  |

**Return value:**

| Type | Description |
| --- | --- |
