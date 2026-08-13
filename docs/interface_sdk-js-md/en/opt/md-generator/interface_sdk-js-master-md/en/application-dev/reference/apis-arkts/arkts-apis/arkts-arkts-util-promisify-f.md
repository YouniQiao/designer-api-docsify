# promisify

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## promisify

```TypeScript
function promisify(original: (err: Object, value: Object) => void): Function
```

Receives a function that uses the error-first callback mode, that is, uses `(err, value) => callback` as the last parameter, and uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-util-function promisify(original: (err: Object, value: Object) => void): Function--><!--Device-util-function promisify(original: (err: Object, value: Object) => void): Function-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| original | (err: Object, value: Object) = & gt; void | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [function](arkts-arkts-taskpool-task-c.md) |
| Function |

## Examples

```TypeScript
async function fn() {
  return 'hello world';
}
const addCall = util.promisify(util.callbackWrapper(fn));
(async () => {
  try {
    let res: string = await addCall();
    console.info(res);
    // Output: hello world
  } catch (err) {
    console.info(err);
  }
})();
```
