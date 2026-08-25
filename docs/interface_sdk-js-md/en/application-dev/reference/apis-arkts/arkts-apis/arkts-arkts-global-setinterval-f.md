# setInterval

## Modules to Import

```TypeScript
```

## setInterval

```TypeScript
function setInterval(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int
```

Repeatedly call the function with delayMs interval between calls. The first call will be after delayMs.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| func | Function | Yes |
| delayMs | int \| null \| undefined | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | FixedArray & lt;Any & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |
