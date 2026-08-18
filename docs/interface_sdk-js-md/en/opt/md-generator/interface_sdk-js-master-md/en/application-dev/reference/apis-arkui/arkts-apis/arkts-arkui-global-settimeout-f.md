# setTimeout

## setTimeout

```TypeScript
export declare function setTimeout(
  handler: Function,
  delay?: number,
  ...arguments: any[]
): number
```

Sets a timer after which a function will be executed.

**Since:** 5

**Model restriction:** This API can be used only in the FA model.

<!--Device-unnamed-export declare function setTimeout(  handler: Function,  delay?: number,  ...arguments: any[]): number--><!--Device-unnamed-export declare function setTimeout(  handler: Function,  delay?: number,  ...arguments: any[]): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | Function | Yes |
| delay | number | No |
| arguments | any[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
