# getCurrentFoldCreaseRegion

## Modules to Import

```TypeScript
```

## getCurrentFoldCreaseRegion

```TypeScript
function getCurrentFoldCreaseRegion(): FoldCreaseRegion
```

Obtains the crease region of the foldable device in the current display mode.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function getCurrentFoldCreaseRegion(): FoldCreaseRegion--><!--Device-display-function getCurrentFoldCreaseRegion(): FoldCreaseRegion-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FoldCreaseRegion](arkts-arkui-display-foldcreaseregion-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

**Examples**

```TypeScript
let data: display.FoldCreaseRegion = display.getCurrentFoldCreaseRegion();
console.info(`Succeeded in obtaining current fold crease region. Data: ${JSON.stringify(data)}`);
```
